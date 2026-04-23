import smbus

class MCP4725:
<<<<<<< HEAD
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
=======
    def __init__(self, dynamic_range, address=0x61, verbose=True):
>>>>>>> 447250de48cb5461c68fd26b4eb02dcbe73aa054
        self.bus = smbus.SMBus(1)
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")
            return

        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
<<<<<<< HEAD
        self.bus.write_i2c_block_data(0x61, first_byte, [second_byte])
=======
>>>>>>> 447250de48cb5461c68fd26b4eb02dcbe73aa054

        try: 
            self.bus.write_i2c_block_data(self.address, first_byte, [second_byte])

<<<<<<< HEAD
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            voltage = 0.0

        number = int((voltage/self.dynamic_range) * 4095)
        self.set_number(number)

if __name__ == "__main__":
    try:
        mcp = MCP4725(5.0, 0x61, True)

        while True:
            try:
                voltage = float(input("Enter voltage in Volts: "))
                mcp.set_voltage(voltage)
=======
            if self.verbose:
                print(f"Число: {number}, отправленные по I2C данные:[0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")

        except OSError as e:    
             print(f"Ошибка ввода-вывода (Errno {e.errno}). Проверьте контакты на плате!")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение выходит за диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            return

        number = int((voltage / self.dynamic_range) * 4095)
        self.set_number(number)


if __name__ == "__main__":
    try:
        dac = MCP4725(5.0, 0x61, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
>>>>>>> 447250de48cb5461c68fd26b4eb02dcbe73aa054

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

            except KeyboardInterrupt:
                break

    finally:
<<<<<<< HEAD
        mcp.deinit()   
=======
        dac.deinit()
>>>>>>> 447250de48cb5461c68fd26b4eb02dcbe73aa054
