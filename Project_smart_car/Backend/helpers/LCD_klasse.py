from RPi import GPIO
import time
from subprocess import check_output
# import ALGEMEEN

lijst_pinnen = [16, 12, 25, 24, 23, 26, 5, 27]  # laagste bits eerst

RS = 21
E = 20

ips = check_output(['hostname', '--all-ip-addresses'])


class LCD:
    def __init__(self, RS_pin=RS, E_pin=E, par_lijst_pinnen=lijst_pinnen):
        self.RS = RS_pin
        self.E = E_pin
        self.lijst_pinnen = par_lijst_pinnen

        GPIO.setmode(GPIO.BCM)
        GPIO.setup([self.RS, self.E] + self.lijst_pinnen,
                   GPIO.OUT, initial=GPIO.LOW)

    def set_data_bits(self, value):
        mask = 1
        for pin in lijst_pinnen:
            GPIO.output(pin, value & mask > 0)
            mask = mask << 1

    def send_instruction(self, value):
        # instructies naar de displaycontroller sturen.
        GPIO.output(RS, GPIO.LOW)
        self.set_data_bits(value)
        # staat hoog in de setup | plaatsen hem hier laag, zodat de data door de displaycontroller kan worden verwerkt!
        GPIO.output(E, GPIO.LOW)
        GPIO.output(E, GPIO.HIGH)
        time.sleep(0.01)

    def send_character(self, value):
        # krijgt dus 1 dus een karakter versturen !# karakters sturen naar de displaycontroller.
        GPIO.output(RS, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(E, GPIO.LOW)
        GPIO.output(E, GPIO.HIGH)
        time.sleep(0.1)

    def nieuwe_lijn(self):
        self.send_instruction(0x80 | 0x40)

    def stuur_letters(self, thing):
        for letter in thing:
            letter = ord(letter)
            self.send_character(letter)

    def init_LCD(self):
        self.send_instruction(0b00111000)  # FunctionQ set
        self.send_instruction(0b00001111)  # Display on
        self.send_instruction(0b00000001)  # clear display/cursor home

    def write_message(self, message):
        aantalchars = 1
        for char in message:
            self.send_character(ord(char))
            aantalchars += 1
            if aantalchars == 17:
                self.send_instruction(0x80 | 0x40)
                aantalchars += 1

    def write_message_met_error(self, message):
        aantalchars = 1
        for char in message:
            if(aantalchars <= 34):
                self.send_character(ord(char))
                aantalchars += 1
                if aantalchars == 17:
                    self.send_instruction(0x80 | 0x40)
                if aantalchars == 34:
                    # telang = "Tekst is te lang"
                    # self.send_instruction(0b00000001)
                    self.init_LCD()
                    self.send_character(ord(char))
                    # for char in telang:
                    #     self.send_character(ord(char))

    # def zend_in_1_keer(self,woord):
    #     lijst = []
    #     for letter in woord:
    #         lijst += letter
    #     for i in lijst:
    #         self.send_character(lijst[i])

    def stuur_letters_snel(self, thing):
        # lijst = []
        for letter in thing:
            letter = ord(letter)
            # lijst += int(letter)
            self.send_character_snel(letter)

    def send_character_snel(self, value):
        # krijgt dus 1 dus een karakter versturen !# karakters sturen naar de displaycontroller.
        GPIO.output(RS, GPIO.HIGH)
        self.set_data_bits(value)
        GPIO.output(E, GPIO.LOW)
        GPIO.output(E, GPIO.HIGH)
        time.sleep(0.1)

    def reken_blocks(self, value):
        aantal = (value/1023.0)*16
        return round(aantal)

    def send_blocks(self, aantal):
        aantal = aantal
        for _ in range(aantal):
            self.send_character(219)
