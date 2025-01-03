import serial
from escpos.printer import Serial
import platform
import glob 

class TicketPrinter:
    def __init__(self, port=None, baudrate=9600, timeout=1):
        if port is None:
            if platform.system() == 'Windows':
                port = 'COM1'
            elif platform.system() == 'Linux':
                port = self.find_serial_port()
            elif platform.system() == 'Darwin':  # macOS
                port = self.find_serial_port()
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        
    def find_serial_port(self):
        ports = glob.glob('/dev/tty.*')
        if not ports:
            raise serial.SerialException("No serial ports found")
        return ports[0]  # or implement logic to choose the correct one

        
    def print_ticket(self, message):
        self.ser.write(message.encode())
        p = Serial(devfile='/dev/serial0', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=1.00)
        p.text(message)
        p.cut()

    def format_ticket(self, phrase):
        nouvelle_phrase = ""
        for i, char in enumerate(phrase):
            if i % 8 == 0 and i != 0:
                nouvelle_phrase += "\n" + char
            else:
                nouvelle_phrase += char
        return nouvelle_phrase
    
    def __del__(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            self.ser.close()

    def print_center(self, text):
        esc_command = bytes([27, 97, 1])
        text_bytes = text.encode('utf-8')
        self.ser.write(esc_command + text_bytes)

    def PrintRun():
        ticket = self.TicketPrinter()
        printer.print_ticket("Hello, world!")

if __name__ == "__main__":
    printer = TicketPrinter()
    printer.print_ticket("Hello, world!")