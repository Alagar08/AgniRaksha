import serial
import time

gsm = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

def send_sms(number, message):
    gsm.write(b'AT+CMGF=1\r')
    time.sleep(1)
    gsm.write(f'AT+CMGS="{number}"\r'.encode())
    time.sleep(1)
    gsm.write(message.encode() + b"\x1A")

send_sms("+91XXXXXXXXXX", "🔥 HIGH FIRE RISK DETECTED! Evacuate immediately.")
