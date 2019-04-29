import serial
import time

ser_strong = 0

def run():
    ser_strong = serial.Serial('/dev/strongarm', 9600)
    time.sleep(1)
    while(True):
        time.sleep(1)
        ser_strong.write("M2DP595E".encode('utf-8'))
        time.sleep(1)
        ser_strong.write("M2DP300E".encode('utf-8'))
    ser_strong.close()
run()
