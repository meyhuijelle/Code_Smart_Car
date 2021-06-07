from io import StringIO
from os import getegid
import re
import time
from RPi import GPIO
from flask.globals import request
from flask.wrappers import Request

import threading
from serial import Serial, PARITY_NONE
import math
import sys


from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify


s = 13
start_time = 0
end_time = 0
steps = 0
steps_old = 0
temp = 0
rps = 0

RPM = 0
KMH = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(s, GPIO.IN)

milliseconds = int(round(time.time() * 1000))

# while True:
#     print(milliseconds)

# start_time = milliseconds
# end_time = start_time + 1000

# while (milliseconds < end_time):
#     data = GPIO.input(s)
#     if(data):
#         steps = steps + 1

#     temp = steps - steps_old
#     steps_old = steps

#     rps = (temp / 20)
#     RPM = rps * 60

#     print(RPM)

while True:
    data = GPIO.input(s)
    print(data)
    time.sleep(0.05)
