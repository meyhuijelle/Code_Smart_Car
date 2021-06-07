# print("dfmoqidsjfmlqjdmlj" + vall.rstrip())
# return vall.rstrip()

# print("JSN1 haalt data op van de Arduino")
# with Serial('/dev/serial0', 9600, bytesize=8, parity=PARITY_NONE, stopbits=1) as poort:
#     string = "JSN1"
#     bericht = string.encode(encoding='UTF-8', errors='strict')
#     poort.write(bericht)
#     val = poort.readline()
#     vall = val.decode()
#     waardeAfstand1 = vall.rstrip()
#     # waardeAfstand = int(waardeAfstand)
#     # DataRepository.create_historiek(
#     #     3, 2, '2017-05-31 19:19:09', waardeLDR, "Dit is voorbeeldcommentaar ")
# print("Distance11111111 ----------------------" + vall.rstrip() + " CM")

# print("afstannnnd SENSOR 1 " + waardeAfstand1)

# print("JSN2 haalt data op van de Arduino")
# with Serial('/dev/serial0', 9600, bytesize=8, parity=PARITY_NONE, stopbits=1) as poort:
#     string = "JSN2"
#     bericht = string.encode(encoding='UTF-8', errors='strict')
#     poort.write(bericht)
#     val = poort.readline()
#     vall = val.decode()
#     waardeAfstand2 = vall.rstrip()
#     # waardeAfstand = int(waardeAfstand)
#     # DataRepository.create_historiek(
#     #     3, 2, '2017-05-31 19:19:09', waardeLDR, "Dit is voorbeeldcommentaar ")
# print("Distance222222 -----------------------" + vall.rstrip() + " CM")

# print("afstannnnd SENSOR 2 " + waardeAfstand2)

# buzzer = GPIO.PWM(triggerPIN, 1000)
# buzzer.start(10)
# buzzer.stop

# ser = serial.Serial('/dev/ttyS0')

# GPIO.setup(led3, GPIO.OUT)
# GPIO.output(led3, GPIO.LOW)


# def get_data_niet_serieel():
#     print(geef_temp())
#     # print(temperatuur[0:5])
#     DataRepository.create_historiek(
#         7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")


# thread_niet_serieel = threading.Timer(0.005, get_data_niet_serieel)
# thread_niet_serieel.start()


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


# def get_temp():
#     while True:
#         print(geef_temp())
#         # print(temperatuur[0:5])
#         DataRepository.create_historiek(
#             7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")
#         time.sleep(1)


# thread_temp = threading.Timer(1, get_temp)
# thread_temp.start()


# def send_data_dallas():
#     while is_sending:
#         print('Verstuurd ***DALLAS*** data')
#         status = temperatuur
#         socketio.emit('B2F_verstuur_data_dallas', {
#                       'temperatuur': status}, broadcast=True)
#         time.sleep(5)


# verstuurd_data_dallas_thread = threading.Timer(1, send_data_dallas)
# verstuurd_data_dallas_thread.start()
