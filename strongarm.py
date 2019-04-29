import serial
import time

ser_strong = serial.Serial('/dev/strongarm', 9600)

'''
time.sleep(1)
while(True):
    ser_strong.write("M1DN000E".encode('utf-8'))
    time.sleep(1)
    ser_strong.write("M2DP100E".encode('utf-8'))
    time.sleep(1)
    #if ser_strong.inWaiting():
    #print(ser_strong.readline())
# ser_strong.close()
'''
def lift():
    for i in range(0,2):
        ser_strong.write("M2DN999E".encode('utf-8'))
        time.sleep(1)
        ser_strong.write("M2DN800E".encode('utf-8'))
        time.sleep(1)
    ser_strong.close()
