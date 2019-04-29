import serial
import time

ser_strong = 0

def run():
    ser_strong = serial.Serial('/dev/ttyACM2', 9600)
    ser_strong.write("M2DP200E".encode('utf-8'))
    ser_strong.close()
run()
