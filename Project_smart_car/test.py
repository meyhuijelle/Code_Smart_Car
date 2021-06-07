# import of libraries
from threading import Timer, Thread
import RPi.GPIO as GPIO
import time
import sys

# class which creates a resettable timer as a thread


class ResetTimer(object):
    def __init__(self, time, function, daemon=None):
        self.__time = time
        self.__function = function
        self.__set()
        self.__running = False
        self.__killed = False
        Thread.__init__(self)
        self.__daemon = daemon

    def __set(self):
        self.__timer = Timer(self.__time, self.__function)

    def stop(self):
        self.__daemon = True

    def run(self):
        self.__running = True
        self.__timer.start()

        if self.__daemon == True:
            sys.exit(0)

    def cancel(self):
        self.__running = False
        self.__timer.cancel()

    def reset(self, start=False):
        if self.__running:
            self.__timer.cancel()
            self.__set()
        if self.__running or start:
            self.start()

# method that counts how often the light barrier is triggered


def count(self):
    global counter
    counter = counter + 1
# method for calculating / displaying of rotations


def output():
    global counter
    timer.cancel()  # stopping the timer
    speed = int(((counter/2)*calc)/wheel)  # calculating rotations per minute
    print("Rotations per minute: " + str(speed))  # output
    counter = 0  # resetting the counter
    timer.reset()  # resetting the timer
    timer.run()


# setting variables
counter = 0
pin = 13  # pin assignment
interval = 10.0  # interval of 10 seconds
calc = 60 / int(interval)  # project interval to a minute
wheel = 20  # amounts of holes in the disk
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
# create the timer which will execute the method output after interval seconds
timer = ResetTimer(interval, output)


# main programm
try:
    # executes method count if the voltage drops at the pin
    GPIO.add_event_detect(pin, GPIO.FALLING, count)
    # start timer
    timer.run()


except KeyboardInterrupt:
    timer.stop()
    timer.join()
    GPIO.cleanup()
