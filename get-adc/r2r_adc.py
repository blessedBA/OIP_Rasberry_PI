import RPi.GPIO as GPIO
import time

class R2R_ADC:

    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):

        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time 

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
        
    def number_to_dac(self, number):
        bits = [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for i in range(0, 255):
            self.number_to_dac(i)
            time.sleep(0.01)
            if (GPIO.input(self.comp_gpio) == 1):
                return i

        return 255

    def get_sc_voltage(self):
        value = self.sequential_counting_adc()
        return (value / 255) * self.dynamic_range

    def successive_approximation_adc(self):
        number = 0

        for bit_index in range(7, -1, -1):
            trial_number = number | (1 << bit_index)
            self.number_to_dac(trial_number)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 0:
                if self.verbose:
                    print(f"bit {bit_index}: reset, trial = {trial_number}")
            else:
                number = trial_number
                if self.verbose:
                    print(f"bit {bit_index}: keep, number = {number}")

        self.number_to_dac(number)

        if self.verbose:
            print(f"Successive approximation ADC number: {number}")

        return number

    def get_sar_voltage(self):
        number = self.successive_approximation_adc()
        return number * self.dynamic_range / 255
            
                        

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.3, 0.01)
        while True:
            voltage = adc.get_sar_voltage()
            print (f"Напряжение: {voltage}")

    finally:
        adc.deinit()
