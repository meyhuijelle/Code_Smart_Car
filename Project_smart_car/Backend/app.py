from io import StringIO
from os import getegid
import re
import time
from RPi import GPIO
from flask.globals import request
from flask.wrappers import Request
from helpers.klasseknop import Button
import threading
from serial import Serial, PARITY_NONE
import math
import sys


from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify
from repositories.DataRepository import DataRepository
import LCD_klasse
from subprocess import check_output


# led3 = 21
# knop1 = Button(20)

waardeLDR = 0
temperatuur = 0
waardeAfstand1 = 0
waardeAfstand2 = 0
waardeAfstand3 = 0
waardeAfstand4 = 0

waardeSpeedSensor = 0

KMH = 0
rps = 0
rpm = 0

vorige_starttijd = int(round(time.time() * 1000))

triggerPIN = 22
button = 17
# LED1 = 5
# LED2 = 6
# LEDs = [5, 6]
led = 6

LEDSTRING = 19


speedSensor = 13

buttonIP = 18

vorige_snelheid = 0

# state_LED1 = False
# state_LED2 = False
state_LEDs = False

counterButton = 0


# Code voor Hardware
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN, GPIO.OUT)
GPIO.setup(LEDSTRING, GPIO.OUT)
GPIO.setup(speedSensor, GPIO.IN)


# GPIO.output(LEDSTRING, GPIO.HIGH)
# time.sleep(1)
# GPIO.output(LEDSTRING, GPIO.LOW)

pwm = GPIO.PWM(LEDSTRING, 100)
pwm.start(LEDSTRING)

buzzer = GPIO.PWM(triggerPIN, 100)
buzzer.stop()

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(buttonIP, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LCD = LCD_klasse.LCD()
ips = check_output(['hostname', '--all-ip-addresses'])


def RPM_TO_KMH(value_RPM):
    return (0.1885 * value_RPM) * 0.25


def get_rpm(c):
    global KMH
    global vorige_starttijd
    global rps
    global rpm
    global vorige_snelheid

    start_timer = int(round(time.time() * 1000))

    tijd = start_timer - vorige_starttijd
    if (tijd != 0):
        rps = (1000/tijd)/20
        rpm = rps * 60
    else:
        print('verkeerde meting!')

    KMH = RPM_TO_KMH(rpm)

    vorige_starttijd = start_timer

    if(KMH != vorige_snelheid):
        print(f"{round(KMH)} km/h----------------------------------------")

    if(KMH >= 5 and KMH <= 10):
        # print("beennnnneeeer")
        pwm.ChangeDutyCycle(25)
    elif (KMH >= 11 and KMH <= 20):
        pwm.ChangeDutyCycle(50)
    elif (KMH >= 21 and KMH <= 30):
        pwm.ChangeDutyCycle(75)
    else:
        pwm.ChangeDutyCycle(1)

    vorige_snelheid = KMH


def switch_state_lights(btn):
    global state_LEDs
    # global state_LED2
    state_LEDs = not state_LEDs
    # state_LED2 = not state_LED2
    print(state_LEDs)
    # print(state_LED2)


def callback_IP(btn):
    print("Er is op me gedrukt!!!")
    global counterButton

    counterButton = counterButton + 1

    if (counterButton == 1):
        print("We zitten voor de counterButton bij 1")
        LCD.init_LCD()
        ip_adress = str(ips)
        print(ip_adress)

    elif (counterButton == 2):
        print("We zitten voor de counterButton bij 2")

    elif (counterButton == 3):
        print("We zitten voor de counterButton bi 3")
        counterButton = 0


GPIO.add_event_detect(button, GPIO.RISING,
                      callback=switch_state_lights, bouncetime=200)

GPIO.add_event_detect(speedSensor, GPIO.RISING, callback=get_rpm)

GPIO.add_event_detect(buttonIP, GPIO.RISING,
                      callback=callback_IP, bouncetime=200)

poort = Serial('/dev/serial0', 9600, bytesize=8,
               parity=PARITY_NONE, stopbits=1)


sensor_file_name = '/sys/bus/w1/devices/28-00000b6cfae9/w1_slave'

# Code voor Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim!'
socketio = SocketIO(app, cors_allowed_origins="*", logger=False,
                    engineio_logger=False, ping_timeout=1)

CORS(app)


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    print(e)

# ***DATA***

# thread_JSN.start()


def geef_temp():
    global temperatuur
    sensor_file = open(sensor_file_name, 'r')
    for line in sensor_file:
        lines = str.rstrip(line)  # weghalen van newlines \n.
        # juiste regel vinden. --> indien niet voorkomt, geeft het -1 terug.
        res = lines.find('t=')
        if(res != -1):
            temperatuur = f"{lines[res+2:res+4]}.{lines[res+5:res+7]} °C"
    sensor_file.close()
    return temperatuur


def get_temp():
    while True:
        print(geef_temp())
        # print(temperatuur[0:5])
        DataRepository.create_historiek(
            7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")
        time.sleep(10)


thread_temp = threading.Timer(10, get_temp)
thread_temp.start()


def get_data_serieel():
    while True:
        global poort
        global waardeLDR
        global waardeAfstand1
        global waardeAfstand2
        global waardeAfstand3
        global waardeAfstand4
        global waardeSpeedSensor
        print("LDR haalt data op van de Arduino")

        string = "DATA"
        bericht = string.encode(encoding='UTF-8', errors='strict')
        poort.write(bericht)
        val = poort.readline()
        vall = val.decode()
        # waardeLDR = vall.rstrip()

        # print("De lichtintensiteit van de LDR bedraagt: " + vall.rstrip() + " %")

        data_arduino = vall.rstrip().split("/")
        waardeLDR = data_arduino[0]
        # waardeSpeedSensor = data_arduino[1]
        waardeAfstand1 = data_arduino[1]
        waardeAfstand2 = data_arduino[2]
        waardeAfstand3 = data_arduino[3]
        waardeAfstand4 = data_arduino[4]

        print(f"{waardeLDR} %")
        # print(waardeSpeedSensor + "KM/H")
        print(f"{waardeAfstand1} cm")
        print(f"{waardeAfstand2} cm")
        print(f"{waardeAfstand3} cm")
        print(f"{waardeAfstand4} cm")

        # time.sleep(1)

        # print(geef_temp())
        # print(temperatuur[0:5])

        DataRepository.create_historiek(
            3, 2, '2017-05-31 19:19:09', waardeLDR, "Dit is voorbeeldcommentaar ")

        # DataRepository.create_historiek(
        #     7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")

        time.sleep(0.005)


thread = threading.Timer(0.005, get_data_serieel)
thread.start()


def buzzer1():
    # buzzer = GPIO.PWM(triggerPIN, 100)
    while True:
        if (int(waardeAfstand1) == -1 and int(waardeAfstand2) == -1 and int(waardeAfstand3) == -1 and int(waardeAfstand4) == -1):
            buzzer.stop()
        elif(int(waardeAfstand1) == 0 or int(waardeAfstand2) == 0 or int(waardeAfstand3) == 0 or int(waardeAfstand4) == 0):
            buzzer.start(10)
            time.sleep(0.05)
            buzzer.ChangeFrequency(100)
            # time.sleep(0.5)
            buzzer.stop()
            time.sleep(0.05)
            # print("11111111111111111111111111111111111111111111111111111111111111111")

        elif (int(waardeAfstand1) > 0 and int(waardeAfstand1) <= 30 or int(waardeAfstand2) > 0 and int(waardeAfstand2) <= 30 or int(waardeAfstand3) > 0 and int(waardeAfstand3) <= 30 or int(waardeAfstand4) > 0 and int(waardeAfstand4) <= 30):
            buzzer.start(10)
            time.sleep(0.1)
            buzzer.ChangeFrequency(100)
            # time.sleep(0.5)
            buzzer.stop()
            time.sleep(0.1)
            # print("222222222222222222222222222222222222222222222222222222222222222")

        elif (int(waardeAfstand1) > 0 and int(waardeAfstand1) <= 50 or int(waardeAfstand2) > 0 and int(waardeAfstand2) <= 50 or int(waardeAfstand3) > 0 and int(waardeAfstand3) <= 50 or int(waardeAfstand4) > 0 and int(waardeAfstand4) <= 50):
            buzzer.start(10)
            time.sleep(0.15)
            buzzer.ChangeFrequency(100)
            # time.sleep(0.5)
            buzzer.stop()
            time.sleep(0.15)
            # print(
            #     "33333333333333333333333333333333333333333333333333333333333333333333333333333")
        elif (int(waardeAfstand1) > 50 or int(waardeAfstand2) > 50 or int(waardeAfstand3) > 50 or int(waardeAfstand4) > 50):
            buzzer.start(10)
            time.sleep(0.20)
            buzzer.ChangeFrequency(100)
            # time.sleep(0.5)
            buzzer.stop()
            time.sleep(0.20)
            # print(
            #     "444444444444444444444444444444444444444444444444444444444444444444444444444")


thread_buzzer1 = threading.Timer(1, buzzer1)
thread_buzzer1.start()


# ***LDR***

# ***Temperatuur***


# ***Temperatuur***
endpoint = '/api/v1'


print("**** Program started ****")

# API ENDPOINTS


@ app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."


@ socketio.on('connect')
def initial_connection():
    print('A new client connect')
    status = waardeLDR
    socketio.emit('B2F_verstuur_data_ldr', {'data': status}, broadcast=True)


is_sending = True


def send_data():
    while is_sending:
        print('Verstuurd ***LDR*** data')
        status = waardeLDR
        socketio.emit('B2F_verstuur_data_ldr', {
                      'lichtsterkte': status}, broadcast=True)

        print('Verstuurd ***DALLAS*** data')
        status = temperatuur
        socketio.emit('B2F_verstuur_data_dallas', {
                      'temperatuur': status}, broadcast=True)

        time.sleep(5)


verstuur_data_ldr_thread = threading.Timer(1, send_data)
verstuur_data_ldr_thread.start()


def send_data_fast():
    while is_sending:
        print('Verstuurd ***JSN1*** data')
        status = waardeAfstand1
        socketio.emit('B2F_verstuur_data_JSN1', {
                      'AfstandJSN1': status}, broadcast=True)
        print('Verstuurd ***JSN2*** data')
        status = waardeAfstand2
        socketio.emit('B2F_verstuur_data_JSN2', {
                      'AfstandJSN2': status}, broadcast=True)
        print('Verstuurd ***JSN3*** data')
        status = waardeAfstand3
        socketio.emit('B2F_verstuur_data_JSN3', {
                      'AfstandJSN3': status}, broadcast=True)
        print('Verstuurd ***JSN4*** data')
        status = waardeAfstand4
        socketio.emit('B2F_verstuur_data_JSN4', {
                      'AfstandJSN4': status}, broadcast=True)

        print('Verstuurd ***SPEED*** data')
        status = waardeSpeedSensor
        socketio.emit('B2F_verstuur_data_speed', {
                      'speed': status}, broadcast=True)

        time.sleep(1)


send_data_fast_thread = threading.Timer(0.5, send_data_fast)
send_data_fast_thread.start()


@ app.route(endpoint + '/historiek', methods=['GET', 'POST'])
def get_historiek():
    if request.method == 'GET':
        return jsonify(historiek=DataRepository.read_historiek()), 200
    elif request.method == 'POST':
        gegevens = DataRepository.json_or_formdata(request)
        nieuwe_historiek = DataRepository.create_historiek(
            gegevens['DeviceID'], gegevens['ActieID'], gegevens['Actiedatum'], gegevens['Waarde'], gegevens['Commentaar'])
        return jsonify(historiekID=nieuwe_historiek), 201


# def snelheid():
#     get_rpm()


# snelheid_thread = threading.Timer(0.1, snelheid)
# snelheid_thread.start()


def main():
    try:
        while True:
            if state_LEDs == True:
                GPIO.output(led, 1)
            elif state_LEDs == False:
                GPIO.output(led, 0)

            time.sleep(0.5)

    except KeyboardInterrupt as e:
        print(e)
    finally:
        print("stop")
        GPIO.cleanup()
        poort.close()
        GPIO.output(LEDSTRING, GPIO.LOW)


main_thread = threading.Timer(3, main)
main_thread.start()

# # ANDERE FUNCTIES
if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')
