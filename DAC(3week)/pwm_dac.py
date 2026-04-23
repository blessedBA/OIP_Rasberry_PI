import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dymanic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_number(self, number):
        GPIO.output(self.gpio_pin, number)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.pwm_frequency):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            return 0

        self.set_number(int(voltage / self.pwm_frequency * 255))


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Enter voltage in Volts: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("You entered not a number. Try again!!!\n")

    finally:
        dac.deinit()   