import serial
import time

ser_strong = 0

def run():
    ser_strong = serial.Serial('/dev/strongarm', 9600)
    ser_strong.write("M2DP595E".encode('utf-8'))
    
run()
