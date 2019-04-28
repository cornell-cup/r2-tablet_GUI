#!/usr/bin/env python
from __future__ import print_function
import select
import serial
import signal
import socket
import struct
import sys
import time
import traceback
import readchar
import sys
import json
import terabee
import lidar
from threading import Thread


import xbox

# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

# Print one or more values without a line feed
def show(*args):
    for arg in args:
        print(arg, end="")

# Print true or false value based on a boolean, without linefeed
def showIf(boolean, ifTrue, ifFalse=" "):
    if boolean:
        show(ifTrue)
    else:
        show(ifFalse)



sys.path.insert(0, "../../../protocol/reference")
import R2Protocol2 as R2Protocol

#TCP_IP = '0.0.0.0'
#TCP_PORT = 9000
#BUFFER_SIZE = 64

MOVE_DATA = R2Protocol.encode(b"BM", b"\x00a\x00a")
STOP_DATA = R2Protocol.encode(b"BM", b"\x00\x19\x00\x19")

def dir(x):
  return 1 if x < 0 else 0

def clamp(x, l, u):
  if x < l:
    return l
  if x > u:
    return u
  return x

motors = serial.Serial('/dev/locomotion', baudrate=115200, timeout=1)


def signal_handler(signal, frame):
  print("Exiting")
  motors.write(STOP_DATA)
  motors.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

time.sleep(2)

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setblocking(0)
#s.bind((TCP_IP, TCP_PORT))
#s.listen(1)

print("Listening")


ls = int(255 * clamp(float(-50), -1.0, 1.0))
rs = int(255 * clamp(float(50), -1.0, 1.0))
send_data = R2Protocol.encode(b"BM", struct.pack("4B",
    dir(ls), clamp(abs(ls), 25, 230),
    dir(rs), clamp(abs(rs), 25, 230)))
last = time.time()
last_executed = time.time()
interval = 5.0
last_moved = -2

'''
HOST = '0.0.0.0'
PORT = 11000
lidar_data = -1
class ListenThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        self.recvSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recvSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.recvSocket.bind((HOST, PORT))
        self.recvSocket.listen(0)
        conn, addr = self.recvSocket.accept()
        print(conn,addr)
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # data = json.loads(data1.decode('utf-8'))
            if not data:
                break
                print("Here")
            try:
                global lidar_data
                lidar_data = (data.decode())
                print("lidar_data ")
                print(lidar_data)
            except Exception as e:
                print (e)
thread = ListenThread()
thread.start()
'''

def run(distance):
    # Instantiate the controller
    joy = xbox.Joystick()
    while not joy.Back():
            time.sleep(0.1)
            degree = 0
            x = 0
            y = 0
            
            if joy.rightTrigger() > 0:
                degree = 1
            if joy.leftTrigger() > 0:
                degree = -1
            x = joy.leftX()
            y = joy.leftY()

            motor_command(x, y)
            head_command(degree)
            if lidar.run_lidar() == False: #stop motors if lidar reads something within 12 inches
                motor_command(0,0)
                break

def head_command(degree):
    print(degree)
    global motors
    hs = int(45 * clamp(float(degree), -1.0, 1.0)) + 90
    send_data = R2Protocol.encode(b"HM", struct.pack("3B",
        hs,0,100))
    print(send_data)
    motors.write(send_data)

def shake_head():
    head_command(1)
    time.sleep(0.5)
    head_command(-1)
    time.sleep(0.5)
    head_command(0)

def motor_command(x, y):
    print(x)
    print(y)
    global motors
    xs = int(255 * clamp(float(x*50), -1.0, 1.0))
    nx = int(255 * clamp(float((x+1)*50), -1.0, 1.0))
    px = int(255 * clamp(float((1-x)*50), -1.0, 1.0))
    ys = int(255 * clamp(float(y*50), -1.0, 1.0))
    send_data = 0
    
    if x > 0:
        send_data = R2Protocol.encode(b"BM", struct.pack("4B",
        dir(nx), clamp(abs(nx), 25, 230),
        dir(xs), clamp(abs(xs), 25, 230)))
    elif x < 0:
        send_data = R2Protocol.encode(b"BM", struct.pack("4B",
        dir(xs), clamp(abs(xs), 25, 230),
        dir(px), clamp(abs(px), 25, 230)))
    else:
        send_data = R2Protocol.encode(b"BM", struct.pack("4B", dir(ys), clamp(abs(ys), 25, 230), dir(ys), clamp(abs(ys), 25, 230)))
    
    print (send_data)
    motors.write(send_data)


