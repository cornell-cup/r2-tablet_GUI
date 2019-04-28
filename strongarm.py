import serial
import time

ser_strong = 0

def run():
    ser_strong = serial.Serial('/dev/strongarm', 9600)
    ser_precise.write("M2DN595E".encode('utf-8'))
    
run()
