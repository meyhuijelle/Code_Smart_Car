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
    # print("benner")
    global count  # delcear the count variable global so we can edit it
    global KMH
    global steps
    global steps_old

    # if not count:
    #     set_start()  # create start time
    #     count = count + 1  # increase counter by 1
    # else:
    #     count = count + 1

    # print(count)

    starteeee = time.time()*1000
    # print("start")
    # print(starteeee)
    einde = starteeee + 1000.0
    while (time.time()*1000 < einde):
        #     steps = steps + 1
        # if(GPIO.input(sensor)):
        steps = steps + 1

    # print(steps)

    temp = steps - steps_old
    steps_old = steps
    rps = (temp/20)
    print(RPM_TO_KMH(rps*60))

    # print("einde")
    # print(einde)

    # print(einde - starteeee)

    # if count == sample:
    #     set_end()  # create end time
    #     delta = end - start  # time taken to do a half rotation in seconds
    #     delta = delta / 60  # converted to minutes
    #     # converted to time for a full single rotation
    #     rpm = (sample / delta) / 2
    #     KMH = RPM_TO_KMH(rpm)
    #     print(rpm)
    #     print(KMH)
    #     count = 0  # reset the count to 0


# execute the get_rpm function when a HIGH signal is detected
GPIO.add_event_detect(sensor, GPIO.RISING, callback=get_rpm)
try:
    while True:  # create an infinte loop to keep the script running
        # get_rpm()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("  Quit")
    GPIO.cleanup()
