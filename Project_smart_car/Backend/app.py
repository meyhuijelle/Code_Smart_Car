# _start_ ***imports*** these are the imports that need to be done. This to work with some parts.

from io import StringIO
from os import getegid, stat, truncate
import re
import time
from RPi import GPIO
from flask.globals import request
from flask.wrappers import Request
from flask_cors.core import CONFIG_OPTIONS
from helpers.klasseknop import Button
import threading
from serial import Serial, PARITY_NONE
import math
import sys
import datetime
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify
from repositories.DataRepository import DataRepository
from helpers.LCD_klasse import LCD
from subprocess import check_output
import subprocess

# _end_


# _start_ ***declaration section*** This is where i declare all my pins of the Raspberry PI.

LCD = LCD()

waardeLDR = 0
temperatuur = 0

waardeAfstand1 = 0
waardeAfstand2 = 0
waardeAfstand3 = 0
waardeAfstand4 = 0

vorigeWaardeAfstand1 = 0
vorigeWaardeAfstand2 = 0
vorigeWaardeAfstand3 = 0
vorigeWaardeAfstand4 = 0

waardeSpeedSensor = 0

KMH = 0
rps = 0
rpm = 0

vorige_starttijd = int(round(time.time() * 1000))


led = 6
speedSensor = 13
button = 17
buttonIP = 18
LEDSTRING = 19
triggerPIN = 22

vorige_snelheid = 0

state_LEDs = False
vorige_state_leds = False
status_for_front = False
buzzerState = False
send_LCD = False

counterButton = 0

ips = check_output(['hostname', '--all-ip-addresses'])

# _end_


# _start_ ***setup section*** This is where i do the setup of all my pins for the Raspberry PI.

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN, GPIO.OUT)
GPIO.setup(LEDSTRING, GPIO.OUT)
GPIO.setup(speedSensor, GPIO.IN)

pwm = GPIO.PWM(LEDSTRING, 100)
pwm.start(LEDSTRING)

buzzer = GPIO.PWM(triggerPIN, 100)
buzzer.stop()

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(buttonIP, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# _end_

# _start_ ***function/callback section*** This is where i declare my functions and callbacks.


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
        KMH = RPM_TO_KMH(rpm)
        # if(counterButton == 2):
        #     LCD.stuur_letters(str(round(KMH)))
        #     LCD.init_LCD()
    else:
        print('verkeerde meting!')

    vorige_starttijd = start_timer

    print('Verstuurd ***SPEED*** data')
    status = round(KMH)
    socketio.emit('B2F_verstuur_data_speed', {
        'speed': status}, broadcast=True)

    DataRepository.create_historiek(
        5, 2, datetime.datetime.now(), round(KMH), "This is speedsensor data")

    if(KMH != vorige_snelheid):
        print(f"{round(KMH)} km/h----------------------------------------")
        # while(counterButton == 2):
        #     LCD.stuur_letters(str(round(KMH)))
        #     LCD.init_LCD()
        #     time.sleep(0.5)

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
    global vorige_snelheid
    global thread_LCD
    global KMH

    print(f"dit is de counter {counterButton}")

    counterButton = counterButton + 1

    code_voor_callback()

# This is for the LCD. The LCD has 3 states. 1 To display the IP-address of the PI, 2 to display the speed (in km/h), temperature and brightness (see main() code) and 3 displays a clear LCD.


def code_voor_callback():
    global counterButton
    global send_LCD
    # while True:
    if (counterButton == 1):
        print("We zitten voor de counterButton bij 1")
        LCD.init_LCD()

        sturenLCD_Lijn1 = "IP-address:"
        LCD.stuur_letters(sturenLCD_Lijn1)

        LCD.nieuwe_lijn()

        # LCD.stuur_letters(letters)
        ip_adress = str(ips)
        sturenLCD_Lijn2 = ip_adress[18:18+14]
        print(f"IP-adress: {ip_adress[18:18+14]}")
        LCD.stuur_letters(sturenLCD_Lijn2)
        # time.sleep(1)

    elif (counterButton == 2):
        print("We zitten voor de counterButton bij 2")
        LCD.init_LCD()
        time.sleep(0.1)
        LCD.vanaf3()
        time.sleep(0.1)
        LCD.stuur_letters("km/h")
        send_LCD = True

    elif (counterButton == 3):
        print("We zitten voor de counterButton bi 3")
        counterButton = 0
        LCD.init_LCD()


# _start_ This is the part where I connect my hardware with callbacks.

GPIO.add_event_detect(button, GPIO.RISING,
                      callback=switch_state_lights, bouncetime=200)

GPIO.add_event_detect(speedSensor, GPIO.RISING, callback=get_rpm)

GPIO.add_event_detect(buttonIP, GPIO.RISING,
                      callback=callback_IP, bouncetime=1000)

# _end_


# Choosing the serial port for the PI
poort = Serial('/dev/serial0', 9600, bytesize=8,
               parity=PARITY_NONE, stopbits=1)

# Finding the file for my DS18B20 temperature sensor
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

# Gives the temperature of my DS18B20 temperature sensor. It opens the previously specified file and cuts it into the right parts to display well.
def geef_temp():
    global temperatuur
    sensor_file = open(sensor_file_name, 'r')
    for line in sensor_file:
        lines = str.rstrip(line)  # removal of newlines.
        # find correct line. --> if not occurring, returns -1.
        res = lines.find('t=')
        if(res != -1):  # if not -1
            temperatuur = f"{lines[res+2:res+4]}.{lines[res+5:res+7]} °C"
    sensor_file.close()  # Close the file properly
    return temperatuur


def get_temp():
    while True:
        print(geef_temp())
        # print(temperatuur[0:5])
        # Send the data to the database.
        DataRepository.create_historiek(
            8, 3, datetime.datetime.now(), temperatuur[0:5], "The dallas is reading data.")
        # Sleep for 10 seconds, because it is not necessary to call up the temperature continuously.
        time.sleep(10)


thread_temp = threading.Timer(10, get_temp)  # Make the thread
thread_temp.start()  # start the thread


# Gets the serial data from the *** Arduino ***.
def get_data_serieel():
    while True:
        global poort
        global waardeLDR
        global waardeAfstand1
        global waardeAfstand2
        global waardeAfstand3
        global waardeAfstand4
        global waardeSpeedSensor
        print("LDR fetches data from the Arduino")

        string = "DATA"  # String that will be send to Arduino.
        bericht = string.encode(encoding='UTF-8', errors='strict')
        poort.write(bericht)  # send DATA to Arduino.
        val = poort.readline()  # Read the incoming.
        vall = val.decode()  # Decode the incoming.

        # Splits the incoming string (you can find the reason in the Arduino code)
        data_arduino = vall.rstrip().split("/")

        # Pass the read-in values to the global variables.
        waardeLDR = data_arduino[0]
        waardeAfstand1 = data_arduino[1]
        waardeAfstand2 = data_arduino[2]
        waardeAfstand3 = data_arduino[3]
        waardeAfstand4 = data_arduino[4]

        # Prin thme out to check if they are correct (optional).
        print(f"{waardeLDR} %")
        print(f"{waardeAfstand1} cm")
        print(f"{waardeAfstand2} cm")
        print(f"{waardeAfstand3} cm")
        print(f"{waardeAfstand4} cm")

        # Send them to the database.
        DataRepository.create_historiek(
            4, 3, datetime.datetime.now(), waardeLDR, "The LDR is reading data.")

        time.sleep(0.005)


thread = threading.Timer(0.005, get_data_serieel)  # Make the thread
thread.start()  # start the thread

# Definition for the buzzer. Called buzzer1 because you can choose to use multiple buzzers. I used one for all the sensors.


def buzzer1():
    global buzzerState
    while True:
        if buzzerState == True:
            # monitors the distance and adjusts the sound of the buzzer as the distance changes (closer = more beeps, farther = fewer beeps).
            if (int(waardeAfstand1) == -1 and int(waardeAfstand2) == -1 and int(waardeAfstand3) == -1 and int(waardeAfstand4) == -1):
                buzzer.stop()
            elif(int(waardeAfstand1) == 0 or int(waardeAfstand2) == 0 or int(waardeAfstand3) == 0 or int(waardeAfstand4) == 0):
                buzzer.start(10)
                time.sleep(0.05)
                buzzer.ChangeFrequency(100)
                # time.sleep(0.5)
                buzzer.stop()
                time.sleep(0.05)
                # print("11111111111111111111111111111111111111111111111111111111111111111") # --> this was to check in which state the buzzer was, you can delete this if u want, I left it there for clarity.

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


thread_buzzer1 = threading.Timer(1, buzzer1)  # Make the thread
thread_buzzer1.start()  # start the thread


endpoint = '/api/v1'


# print("**** Program started ****")


# API ENDPOINTS

# Default endpoint
@ app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."

# On connection


@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    status = waardeLDR
    socketio.emit('B2F_verstuur_data_ldr', {'data': status}, broadcast=True)

# This will refresh the history of my site every 10 seconds.


def sendHistory():
    while True:
        socketio.emit('B2F_history', broadcast=True)
        time.sleep(10)


history_Thread = threading.Timer(1, sendHistory)  # Make the thread
history_Thread.start()  # start the thread

# You can also do while true. I choose is_sending because this can easily be turned off in the future.
is_sending = True

# To switch the lights state with the button on the website.


@socketio.on('F2B_stateLights')
def changeStateLights(msg):
    global state_LEDs

    print(msg.get('stateLights'))  # To check the incoming result.

    # looks at the incoming status and applies it to the lights.
    if(msg.get('stateLights') == "True"):
        state_LEDs = True
    elif(msg.get('stateLights') == "False"):
        state_LEDs = False

# To switch the buzzer state with the button on the website.


@socketio.on('F2B_stateBuzzer')
def changeStateBuzzer(msg):
    global buzzerState

    print(msg.get('stateBuzzer'))  # To check the incoming result.

    # looks at the incoming status and applies it to the buzzer.
    if(msg.get('stateBuzzer') == "True"):
        buzzerState = True
        # Send it to the database.
        DataRepository.create_historiek(
            2, 4, datetime.datetime.now(), buzzerState, "Buzzer turned ON")
    elif(msg.get('stateBuzzer') == "False"):
        buzzerState = False
        # Send it to the database.
        DataRepository.create_historiek(
            2, 5, datetime.datetime.now(), buzzerState, "Buzzer turned OFF")

    print(f"This is now the state of the buzzer {buzzerState}")

# Turns the Raspberry PI off with a button on the website.


@socketio.on('F2B_switchOFF')
def switchOFF():
    subprocess.Popen(["/sbin/poweroff"])

 # Sends the data.


def send_data():
    while is_sending:
        # Sends the LDR data to the frontend for the website.
        print('Verstuurd ***LDR*** data')
        status = waardeLDR
        socketio.emit('B2F_verstuur_data_ldr', {
                      'lichtsterkte': status}, broadcast=True)

        # Sends the LDR data to the database.
        DataRepository.create_historiek(
            4, 2, datetime.datetime.now(), waardeLDR, "The LDR is sending data.")

        # Sends the DALLAS data to the frontend for the website.
        print('Verstuurd ***DALLAS*** data')
        status = temperatuur
        socketio.emit('B2F_verstuur_data_dallas', {
                      'temperatuur': status}, broadcast=True)

        # print(str(temperatuur)[0:5]) --> this is to see what will be send to the database.

        # Sends the LDR data to the database.
        DataRepository.create_historiek(
            8, 2, datetime.datetime.now(),  str(temperatuur)[0:5], "The dallas is sending data.")

        time.sleep(5)  # Sleep for 5 seconds.


verstuur_data_ldr_thread = threading.Timer(1, send_data)  # Make the thread
verstuur_data_ldr_thread.start()  # start the thread


# Sends data faster.
def send_data_fast():
    global vorigeWaardeAfstand1
    global vorigeWaardeAfstand2
    global vorigeWaardeAfstand3
    global vorigeWaardeAfstand4
    while is_sending:

        # Sends the data of the distance sensors to the frontend for the site.

        # print('Verstuurd ***JSN1*** data')
        status = waardeAfstand1
        socketio.emit('B2F_verstuur_data_JSN1', {
            'AfstandJSN1': status}, broadcast=True)
        # print('Verstuurd ***JSN2*** data')
        status = waardeAfstand2
        socketio.emit('B2F_verstuur_data_JSN2', {
            'AfstandJSN2': status}, broadcast=True)
        # print('Verstuurd ***JSN3*** data')
        status = waardeAfstand3
        socketio.emit('B2F_verstuur_data_JSN3', {
            'AfstandJSN3': status}, broadcast=True)
        # print('Verstuurd ***JSN4*** data')
        status = waardeAfstand4
        socketio.emit('B2F_verstuur_data_JSN4', {
            'AfstandJSN4': status}, broadcast=True)

        # Checks if the value has changed. If the value is changed send it to the database.
        if(waardeAfstand1 != vorigeWaardeAfstand1 or waardeAfstand2 != vorigeWaardeAfstand2 or waardeAfstand3 != vorigeWaardeAfstand3 or waardeAfstand4 != vorigeWaardeAfstand4):
            DataRepository.create_historiek(
                3, 2, datetime.datetime.now(),  waardeAfstand1, "JSN1 is sending data.")

            DataRepository.create_historiek(
                3, 2, datetime.datetime.now(),  waardeAfstand2, "JSN2 is sending data.")

            DataRepository.create_historiek(
                3, 2, datetime.datetime.now(),  waardeAfstand3, "JSN3 is sending data.")

            DataRepository.create_historiek(
                3, 2, datetime.datetime.now(),  waardeAfstand4, "JSN4' is sending data.")

        # Declare the previous distance.
        vorigeWaardeAfstand1 = waardeAfstand1
        vorigeWaardeAfstand2 = waardeAfstand2
        vorigeWaardeAfstand3 = waardeAfstand3
        vorigeWaardeAfstand4 = waardeAfstand4

        time.sleep(1)


send_data_fast_thread = threading.Timer(1, send_data_fast)  # Make the thread
send_data_fast_thread.start()  # start the thread


# This is a route to get data from the database. Use 'http://192.168.168.168:5000/api/v1/historiek' to check this in postman.
@ app.route(endpoint + '/historiek', methods=['GET', 'POST'])
def get_historiek():
    if request.method == 'GET':
        return jsonify(historiek=DataRepository.read_historiek()), 200
    elif request.method == 'POST':
        gegevens = DataRepository.json_or_formdata(request)
        nieuwe_historiek = DataRepository.create_historiek(
            gegevens['DeviceID'], gegevens['ActieID'], gegevens['Actiedatum'], gegevens['Waarde'], gegevens['Commentaar'])
        return jsonify(historiekID=nieuwe_historiek), 201


# This is a main part of my code. This is for general things.
def main():
    global send_LCD
    global temperatuur
    global vorige_state_leds
    global status_for_front
    lelteller = 50

    try:
        while True:
            # Checks the state of the leds and puts them on (if True) or off (if False).
            if state_LEDs == True:
                GPIO.output(led, 1)
                status_for_front = 1
            elif state_LEDs == False:
                GPIO.output(led, 0)
                status_for_front = 2

            # If the state of the leds has changed send it to the frontend for the site and send it to the database.
            if(state_LEDs != vorige_state_leds):
                # Send it to frontend for site.
                socketio.emit('B2F_state_with_button', {
                    'state': status_for_front}, broadcast=True)
                # Send it to database.
                if state_LEDs == True:
                    DataRepository.create_historiek(
                        1, 6, datetime.datetime.now(), state_LEDs, "LED turned ON")
                if state_LEDs == False:
                    DataRepository.create_historiek(
                        1, 7, datetime.datetime.now(), state_LEDs, "LED turned OFF")

            # This is for the LCD.
            # If the state is 2, do this.
            if(counterButton == 2 and send_LCD == True):
                if lelteller == 50:
                    LCD.nieuwe_lijn()
                    stuur1 = f"{str(temperatuur)[0:5]}"
                    stuur2 = "*"
                    stuur3 = "C"
                    stuur4 = "  "
                    stuur5 = f"{waardeLDR}%"
                    LCD.stuur_letters(stuur1)
                    # LCD.send_character(ord(stuur2))
                    LCD.send_character(ord(stuur2))
                    LCD.stuur_letters(stuur3)
                    LCD.stuur_letters(stuur4)
                    LCD.stuur_letters(stuur5)
                    lelteller = 0

                LCD.vanaf0()  # Starts at the beginning of the LCD.
                LCD.stuur_letters(str(round(KMH)))
                lelteller = lelteller + 1
                LCD.vanaf0()
                if(KMH) < 10:
                    # Sends spaces for the non-used places
                    LCD.stuur_letters("  ")
                    # Send the km/h's to the LCD.
                    LCD.stuur_letters(str(round(KMH)))
                elif(KMH) < 100:
                    LCD.vanaf0()
                    LCD.stuur_letters(" ")
                    LCD.stuur_letters(str(round(KMH)))
                else:
                    LCD.stuur_letters(str(round(KMH)))
            else:
                send_LCD = False  # When if is not true..
            vorige_state_leds = state_LEDs
            time.sleep(0.1)

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
