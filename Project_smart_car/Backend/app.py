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


# led3 = 21
knop1 = Button(20)

waardeLDR = 0
temperatuur = 0
waardeAfstand1 = 0
waardeAfstand2 = 0
waardeAfstand3 = 0
waardeAfstand4 = 0

triggerPIN = 22

# Code voor Hardware
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPIN, GPIO.OUT)

buzzer = GPIO.PWM(triggerPIN, 100)
buzzer.stop()

# buzzer = GPIO.PWM(triggerPIN, 1000)
# buzzer.start(10)
# buzzer.stop


sensor_file_name = '/sys/bus/w1/devices/28-00000b6cfae9/w1_slave'


# ser = serial.Serial('/dev/ttyS0')

# GPIO.setup(led3, GPIO.OUT)
# GPIO.output(led3, GPIO.LOW)


def lees_knop(pin):
    if knop1.pressed:
        print("**** button pressed ****")


knop1.on_press(lees_knop)


# Code voor Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim!'
socketio = SocketIO(app, cors_allowed_origins="*", logger=False,
                    engineio_logger=False, ping_timeout=1)

CORS(app)


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    print(e)


# ***LDR***

def get_data_serieel():
    while True:
        global waardeLDR
        global waardeAfstand1
        global waardeAfstand2
        global waardeAfstand3
        global waardeAfstand4
        print("LDR haalt data op van de Arduino")
        with Serial('/dev/serial0', 9600, bytesize=8, parity=PARITY_NONE, stopbits=1) as poort:
            string = "DATA"
            bericht = string.encode(encoding='UTF-8', errors='strict')
            poort.write(bericht)
            val = poort.readline()
            vall = val.decode()
            # waardeLDR = vall.rstrip()

        # print("De lichtintensiteit van de LDR bedraagt: " + vall.rstrip() + " %")

        data_arduino = vall.rstrip().split("/")
        waardeLDR = data_arduino[0]
        waardeAfstand1 = data_arduino[1]
        waardeAfstand2 = data_arduino[2]
        waardeAfstand3 = data_arduino[3]
        waardeAfstand4 = data_arduino[4]

        print(waardeLDR)
        print(waardeAfstand1)
        print(waardeAfstand2)
        print(waardeAfstand3)
        print(waardeAfstand4)
        # time.sleep(1)

        print(geef_temp())
        # print(temperatuur[0:5])

        DataRepository.create_historiek(
            3, 2, '2017-05-31 19:19:09', waardeLDR, "Dit is voorbeeldcommentaar ")

        DataRepository.create_historiek(
            7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")

        time.sleep(0.005)


thread = threading.Timer(0.005, get_data_serieel)
thread.start()


# def get_data_niet_serieel():
#     print(geef_temp())
#     # print(temperatuur[0:5])
#     DataRepository.create_historiek(
#         7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")


# thread_niet_serieel = threading.Timer(0.005, get_data_niet_serieel)
# thread_niet_serieel.start()


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

# def buzzer1():
#     # buzzer = GPIO.PWM(triggerPIN, 100)
#     while True:
#         if (int(waardeAfstand1) == -1):
#             buzzer.stop()
#         elif(int(waardeAfstand1) == 0):
#             buzzer.start(10)
#             time.sleep(0.05)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.05)
#         elif (int(waardeAfstand1) <= 30):
#             buzzer.start(10)
#             time.sleep(0.1)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.1)
#         elif (int(waardeAfstand1) <= 50):
#             buzzer.start(10)
#             time.sleep(0.15)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.15)


# thread_buzzer1 = threading.Timer(1, buzzer1)
# thread_buzzer1.start()


# def buzzer2():
#     # buzzer = GPIO.PWM(triggerPIN, 100)
#     while True:
#         if (int(waardeAfstand2) == -1):
#             buzzer.stop()
#         elif(int(waardeAfstand2) == 0):
#             buzzer.start(10)
#             time.sleep(0.05)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.05)
#         elif (int(waardeAfstand2) <= 30):
#             buzzer.start(10)
#             time.sleep(0.1)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.1)
#         elif (int(waardeAfstand2) <= 50):
#             buzzer.start(10)
#             time.sleep(0.15)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.15)
#         elif (int(waardeAfstand2) > 50):
#             buzzer.start(10)
#             time.sleep(0.20)
#             buzzer.ChangeFrequency(100)
#             # time.sleep(0.5)
#             buzzer.stop()
#             time.sleep(0.20)


# thread_buzzer2 = threading.Timer(1, buzzer2)
# thread_buzzer2.start()


# def get_data_JSN():
#     while True:
#         global waardeAfstand
#         print("JSN haalt data op van de Arduino")
#         with Serial('/dev/serial0', 9600, bytesize=8, parity=PARITY_NONE, stopbits=1) as poort:
#             string = "JSN"
#             bericht = string.encode(encoding='UTF-8', errors='strict')
#             poort.write(bericht)
#             val = poort.readline()
#             vall = val.decode()
#             waardeLDR = vall.rstrip()
#             # DataRepository.create_historiek(
#             #     3, 2, '2017-05-31 19:19:09', waardeLDR, "Dit is voorbeeldcommentaar ")
#         print("Distance " + vall.rstrip() + " CM")
#         time.sleep(0.5)


# thread_JSN = threading.Timer(1, get_data_JSN)
# thread_JSN.start()

# ***LDR***

# ***Temperatuur***


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


# def get_temp():
#     while True:
#         print(geef_temp())
#         # print(temperatuur[0:5])
#         DataRepository.create_historiek(
#             7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")
#         time.sleep(1)


# thread_temp = threading.Timer(1, get_temp)
# thread_temp.start()

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


# def send_data_dallas():
#     while is_sending:
#         print('Verstuurd ***DALLAS*** data')
#         status = temperatuur
#         socketio.emit('B2F_verstuur_data_dallas', {
#                       'temperatuur': status}, broadcast=True)
#         time.sleep(5)


# verstuurd_data_dallas_thread = threading.Timer(1, send_data_dallas)
# verstuurd_data_dallas_thread.start()


@ app.route(endpoint + '/historiek', methods=['GET', 'POST'])
def get_historiek():
    if request.method == 'GET':
        return jsonify(historiek=DataRepository.read_historiek()), 200
    elif request.method == 'POST':
        gegevens = DataRepository.json_or_formdata(request)
        nieuwe_historiek = DataRepository.create_historiek(
            gegevens['DeviceID'], gegevens['ActieID'], gegevens['Actiedatum'], gegevens['Waarde'], gegevens['Commentaar'])
        return jsonify(historiekID=nieuwe_historiek), 201


# # ANDERE FUNCTIES
if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')
