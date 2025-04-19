# Credit to StormCPH and SunOne on Github for parts of the Code
from InputMethods.InputMethod import InputMethod
import serial
import serial.tools.list_ports

def list_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Found port: {port.device}")
        return port.device
    return None

class InputMethodArduino(InputMethod):
    NAME:str = "Arduino"

    def __init__(self):

        super().__init__()
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 11500
        self.serial_port.timeout = 0
        self.serial_port.write_timeout = 0

        self.serial_port.port = self.__detect_port()

        try:
            self.serial_port.open()
            print(f'Arduino: Connected! Port: {self.serial_port.port}')
        except Exception as e:
            print(f'Arduino: Not Connected...\n{e}')

    def click(self,button):
        self._send_command('c')

    def press(self):
        self._send_command('p')

    def release(self):
        self._send_command('r')

    def moveRelative(self, x, y):

        x_parts = self._split_value(x)
        y_parts = self._split_value(y)
        for x_part, y_part in zip(x_parts, y_parts):
            data = f'm{x_part},{y_part}\n'.encode()
            self.serial_port.write(data)

    def _split_value(self, value):
        values = []
        sign = -1 if value < 0 else 1

        while abs(value) > 127:
            values.append(sign * 127)
            value -= sign * 127

        values.append(value)

        return values

    def close(self):
        if self.serial_port.is_open:
            self.serial_port.close()

    def __del__(self):
        self.close()

    def __detect_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description:
                return port.device
        return None

    def _send_command(self, command):
        self.serial_port.write(f'{command}\n'.encode())
