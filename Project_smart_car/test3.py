# from Project_smart_car.test2 import KMH
import RPi.GPIO as GPIO
import time

from flask.app import setupmethod

sensor = 13  # define the GPIO pin our sensor is attached to

GPIO.setmode(GPIO.BCM)  # set GPIO numbering system to BCM
GPIO.setup(sensor, GPIO.IN)  # set our sensor pin to an input

sample = 10  # how many half revolutions to time
count = 0

start = 0
end = 0

KMH = 0

rps = 0
rpm = 0

vorige_starttijd = int(round(time.time() * 1000))

steps = 0
steps_old = 0


def set_start():
    global start
    start = time.time()


def set_end():
    global end
    end = time.time()


def RPM_TO_KMH(value_RPM):
    return (0.1885 * value_RPM) * 0.25


def get_rpm(c):
    global count  # delcear the count variable global so we can edit it
    global KMH
    global steps
    global steps_old
    global vorige_starttijd
    global rps
    global rpm

    start_timer = int(round(time.time() * 1000))

    tijd = start_timer - vorige_starttijd
    if (tijd != 0):
        rps = (1000/tijd)/20
        rpm = rps * 60
    else:
        print('verkeerde meting!')

    # print(rps/20)

    KMH = 0.1885 * rpm * 1.2

    vorige_starttijd = start_timer


# execute the get_rpm function when a HIGH signal is detected
GPIO.add_event_detect(sensor, GPIO.RISING, callback=get_rpm)
try:
    while True:  # create an infinte loop to keep the script running
        # global gemiddelde

        print(f"{round(KMH)} km/h")
        # print()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("  Quit")
    GPIO.cleanup()
