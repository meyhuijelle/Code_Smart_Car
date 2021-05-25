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


from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify
from repositories.DataRepository import DataRepository


# Code voor Hardware
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# led3 = 21
knop1 = Button(20)

waardeLDR = 0

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


def get_LDR_data():
    while True:
        global waardeLDR
        print("LDR haalt data op van de Arduino")
        with Serial('/dev/serial0', 9600, bytesize=8, parity=PARITY_NONE, stopbits=1) as poort:
            string = "LDR"
            bericht = string.encode(encoding='UTF-8', errors='strict')
            poort.write(bericht)
            val = poort.readline()
            vall = val.decode()
            waardeLDR = vall.rstrip()
        print("De lichtintensiteit van de LDR bedraagt: " + vall.rstrip() + " %")
        # print(vall.rstrip())
        # return vall.rstrip()


thread = threading.Timer(1, get_LDR_data)
thread.start()

endpoint = '/api/v1'


print("**** Program started ****")

# API ENDPOINTS


@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."


@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    # # Send to the client!
    # vraag de status op van de lampen uit de DB
    # status = DataRepository.read_historiek()
    # print(status)
    status = waardeLDR
    socketio.emit('B2F_verstuur_data', {'data': status}, broadcast=True)


is_sending = True


def send_data():
    while is_sending:
        print("data_versturen")
        status = waardeLDR
        socketio.emit('B2F_verstuur_data', {'data': status}, broadcast=True)
        time.sleep(1)


dataThread = threading.Timer(1, send_data)
dataThread.start()


@app.route(endpoint + '/historiek', methods=['GET', 'POST'])
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
