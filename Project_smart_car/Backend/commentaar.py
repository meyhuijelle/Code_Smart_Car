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

 <!-- < section class = "o-row o-row--sm " >
            <!-- < div class = "o-container umax-width-sm" > - ->
        <div class="o-container u-max-width-sm">
            <div class="o-layout o-layout--align-center">
                <div class="o-layout__item u-1-of-2 u-1-of-4-bp3">
                    <div class="c-button__style js-buttonHistory">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 0 24 24" width="24px" fill="#000000">
                                <path d="M0 0h24v24H0z" fill="none" />
                                <path d="M10 20h4V4h-4v16zm-6 0h4v-8H4v8zM16 9v11h4V9h-4z" />
                            </svg>
                        </div>
                        <div>
                            <p class="u-mb-clear">HISTORY</p>
                        </div>
                        <!-- </div> -->
                    </div>
                </div>

                <div class="o-layout__item u-1-of-2 u-1-of-4-bp3">
                    <div class="c-button__style js-parkingSensButton">
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" width="37.591" height="24" viewBox="0 0 37.591 24">
                                <g id="Group_446" data-name="Group 446" transform="translate(-319.046 -336)">
                                    <g id="directions_car_black_24dp" transform="translate(326 336)">
                                        <path id="Path_12" data-name="Path 12" d="M0,0H24V24H0Z" fill="none" />
                                        <path id="Path_13" data-name="Path 13"
                                            d="M18.92,6.01A1.494,1.494,0,0,0,17.5,5H6.5A1.5,1.5,0,0,0,5.08,6.01L3,12v8a1,1,0,0,0,1,1H5a1,1,0,0,0,1-1V19H18v1a1,1,0,0,0,1,1h1a1,1,0,0,0,1-1V12ZM6.5,16A1.5,1.5,0,1,1,8,14.5,1.5,1.5,0,0,1,6.5,16Zm11,0A1.5,1.5,0,1,1,19,14.5,1.5,1.5,0,0,1,17.5,16ZM5,11,6.5,6.5h11L19,11Z" />
                                    </g>
                                    <line id="Line_2" data-name="Line 2" y1="2" x2="6" transform="translate(349.5 341.5)" fill="none" stroke="#707070"
                                        stroke-width="1" />
                                    <line id="Line_3" data-name="Line 3" x2="4" transform="translate(350 348)" fill="none" stroke="#707070"
                                        stroke-width="1" />
                                    <line id="Line_4" data-name="Line 4" x2="7" y2="2" transform="translate(349.5 351.5)" fill="none" stroke="#707070"
                                        stroke-width="1" />
                                    <line id="Line_5" data-name="Line 5" x1="5.303" y1="2" transform="translate(320.197 341.5)" fill="none"
                                        stroke="#707070" stroke-width="1" />
                                    <line id="Line_6" data-name="Line 6" x1="4" transform="translate(321 348)" fill="none" stroke="#707070"
                                        stroke-width="1" />
                                    <line id="Line_7" data-name="Line 7" x1="6.303" y2="2" transform="translate(319.197 351.5)" fill="none"
                                        stroke="#707070" stroke-width="1" />
                                </g>
                            </svg>

                        </div>
                        <div>
                            <p class="c-text__layout-btn u-mb-clear">PARKING SENSORS</p>
                        </div>
                        <!-- </div> -->
                    </div>
                </div>
            </div>
        </div>
        </section>

        <section class="o-row o-row--sm ">
            <!-- <div class="o-container umax-width-sm"> -->
            <div class="o-container u-max-width-sm">
                <div class="o-layout o-layout--align-center ">
                    <!-- <div class="o-layout__item u-1-of-2-bp3 u-2-of-5-bp4"> -->
                    <div class="c-button__style js-buttonHistory">
                        <div>
                            <svg id="volume_off_black_24dp_1_" data-name="volume_off_black_24dp (1)" xmlns="http://www.w3.org/2000/svg" width="24"
                                height="24" viewBox="0 0 24 24">
                                <path id="Path_30" data-name="Path 30" d="M0,0H24V24H0Z" fill="none" />
                                <path id="Path_31" data-name="Path 31"
                                    d="M16.5,12A4.5,4.5,0,0,0,14,7.97v2.21l2.45,2.45A4.232,4.232,0,0,0,16.5,12ZM19,12a6.843,6.843,0,0,1-.54,2.64l1.51,1.51A8.8,8.8,0,0,0,21,12a9,9,0,0,0-7-8.77V5.29A7.005,7.005,0,0,1,19,12ZM4.27,3,3,4.27,7.73,9H3v6H7l5,5V13.27l4.25,4.25A6.924,6.924,0,0,1,14,18.7v2.06a8.99,8.99,0,0,0,3.69-1.81L19.73,21,21,19.73l-9-9ZM12,4,9.91,6.09,12,8.18Z" />
                            </svg>

                        </div>
                        <div>
                            <p class="u-mb-clear">BUZZER ON/OFF</p>
                        </div>
                        <!-- </div> -->
                    </div>
                    <!-- </div> -->

                    <!-- <div class=" o-layout__item u-1-of-2-bp3 u-2-of-5-bp4"> -->
                    <div class="c-button__style js-parkingSensButton">
                        <div>
                            <svg id="lightbulb_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                                <path id="Path_18" data-name="Path 18" d="M0,0H24V24H0Z" fill="none" />
                                <path id="Path_19" data-name="Path 19"
                                    d="M9,21a1,1,0,0,0,1,1h4a1,1,0,0,0,1-1V20H9ZM12,2A6.957,6.957,0,0,0,5,9a6.827,6.827,0,0,0,3,5.7V17a1,1,0,0,0,1,1h6a1,1,0,0,0,1-1V14.7A7.1,7.1,0,0,0,19,9,6.957,6.957,0,0,0,12,2Z" />
                            </svg>

                        </div>
                        <div>
                            <p class="c-text__layout-btn u-mb-clear">HEADLIGHTS ON/OFF</p>
                        </div>
                        <!-- </div> -->
                        <!-- </div> -->
                    </div>
                </div>
            </div>
        </section>

        <section class="o-row o-row--sm ">
            <!-- <div class="o-container umax-width-sm"> -->
            <div class="o-container u-max-width-sm">
                <div class="o-layout o-layout--align-center ">
                    <!-- <div class=" o-layout__item u-1-of-2-bp3 u-2-of-5-bp4"> -->
                    <div class="c-button__style js-parkingSensButton">
                        <div>
                            <!-- <svg id="power_settings_new_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                            <path id="Path_10" data-name="Path 10" d="M0,0H24V24H0Z" fill="none" />
                            <path id="Path_11" data-name="Path 11"
                                d="M13,3H11V13h2Zm4.83,2.17L16.41,6.59A6.92,6.92,0,0,1,19,12,7,7,0,1,1,7.58,6.58L6.17,5.17A8.992,8.992,0,1,0,21,12,8.932,8.932,0,0,0,17.83,5.17Z"
                                fill="#4d00b3" />
                        </svg> -->

                            <svg id="power_settings_new_black_24dp" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                                <path id="Path_10" data-name="Path 10" d="M0,0H24V24H0Z" fill="none" />
                                <path id="Path_11" data-name="Path 11"
                                    d="M13,3H11V13h2Zm4.83,2.17L16.41,6.59A6.92,6.92,0,0,1,19,12,7,7,0,1,1,7.58,6.58L6.17,5.17A8.992,8.992,0,1,0,21,12,8.932,8.932,0,0,0,17.83,5.17Z" />
                            </svg>

                        </div>
                        <div>
                            <p class="c-text__layout-btn u-mb-clear">APPLICATION ON/OFF</p>
                        </div>
                        <!-- </div> -->
                        <!-- </div> -->
                    </div>
                </div>
            </div>
        </section>




opkuisen!!!!

# led3 = 21
# knop1 = Button(20)



# Code voor Hardware

# GPIO.output(LEDSTRING, GPIO.HIGH)
# time.sleep(1)
# GPIO.output(LEDSTRING, GPIO.LOW)

# LED1 = 5
# LED2 = 6
# LEDs = [5, 6]

# state_LED1 = False
# state_LED2 = False

# state = False

# def thread_send_to_lCD():
#     while counterButton == 2:
#         LCD.stuur_letters(str(round(KMH)))
#         time.sleep(0.3)
#         LCD.init_LCD()


# thread_LCD = threading.Timer(0.1, thread_send_to_lCD)

     # while (counterButton == 2):

        # LCD.nieuwe_lijn()
        # stuur1 = f"{temperatuur}"
        # stuur2 = "    "
        # stuur3 = f"{waardeLDR}%"
        # LCD.stuur_letters(stuur1)
        # LCD.stuur_letters(stuur2)
        # LCD.stuur_letters(stuur3)

        # thread_LCD.start()

        # localTeller = 0
        # while True:
        #     localTeller = localTeller + 1
        # teVersturen = vorige_snelheid
        #     LCD.stuur_letters(str(vorige_snelheid))
        #     LCD.init_LCD()
        #     time.sleep(0.05)
        # # print(localTeller)
        # time.sleep(0.5)

    # thread_JSN.start()

       lines = str.rstrip(line)  # weghalen van newlines \n.
        # juiste regel vinden. --> indien niet voorkomt, geeft het -1 terug.

                # waardeLDR = vall.rstrip()

        # print("De lichtintensiteit van de LDR bedraagt: " + vall.rstrip() + " %")

         # waardeSpeedSensor = data_arduino[1]

                 # print(waardeSpeedSensor + "KM/H")

                       # time.sleep(1)

        # print(geef_temp())
        # print(temperatuur[0:5])

                # DataRepository.create_historiek(
        #     7, 3, '2017-05-31 19:19:09', temperatuur[0:5], "Dit is temperatuurdata")

        # DataRepository.create_historiek(
        #     7, 3, '2017-05-31 19:19:09', temperatuur, "Dit is temperatuurdata")

           # buzzer = GPIO.PWM(triggerPIN, 100)

           # ***LDR***

# ***Temperatuur***


# ***Temperatuur***


# socketio.emit('B2F_history', broadcast=True)

# global state_LED_
    # print(state_LEDs)



    # print(f"fddsqfdsf{state}")

    # state_LEDs = state


    # buzzer1()

# subprocess.Popen(["sudo", "poweroff"])



   # @socketio.on('B2F_state_with_button')
    # def send_state():

    # socketio.emit('B2F_state_with_button', {
    #     'state': state_LEDs}, broadcast=True)

    # socketio.emit('B2F_state_with_button', {
    #               'state': state_LEDs}, broadcast=True)
    # print(bool(msg.get('state')))
    # state_LEDs = bool(msg.get('state'))
    # print(state_LEDs)

    # if state_LEDs == True:
    #     GPIO.output(led, 1)
    # elif state_LEDs == False:
    #     GPIO.output(led, 0)

#  temperatuur[0:5]


        # print('Verstuurd ***SPEED*** data')
        # status = round(KMH)
        # socketio.emit('B2F_verstuur_data_speed', {
        #               'speed': status}, broadcast=True)









# def send_speedData():
#     while is_sending:
#         print('Verstuurd ***SPEED*** data')
#         status = round(KMH)
#         socketio.emit('B2F_verstuur_data_speed', {
#                       'speed': status}, broadcast=True)

#         time.sleep(0.05)


# send_speedData_thread = threading.Timer(1, send_speedData)
# send_speedData_thread.start()



# def snelheid():
#     get_rpm()


# snelheid_thread = threading.Timer(0.1, snelheid)
# snelheid_thread.start()

# in de main

  # LCD.init_LCD()

  
            # print(f" leeeeeed {state_LEDs}")
            # print(f" leeeeeedvorig {vorige_state_leds}")


# print('jaaa')
            # print(state_LEDs)
            # print(vorige_state_leds)
            # socketio.emit('B2F_state_with_button', {
            #     'state': state_LEDs}, broadcast=True)

            # if state_LEDs != vorige_state_leds:

            # print(f"temp {str(temperatuur)[0:5]}")
            # code_voor_callback()
            # print(lelteller)

            # print("benner")
                    # LCD.vanaf0()

                    # LCD.vanaf2()

        # LCD.vanaf1()

    # LCD.vanaf0()

# LCD.init_LCD()
                # time.sleep(0.1)
                # LCD.vanaf0()
                # LCD.stuur_letters("   ")
