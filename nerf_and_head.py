import serial
import time

ser_nerf = serial.Serial('/dev/ttyACM1', 9600)
#ser_head = serial.Serial('/dev/head', 9600)
commands = ["M1D10E", "M1D-10E", "M2D10E", "M2D-10E", "M7D0E"] 
init = ["M3D1E", "M3D2E", "M4D1E", "M4D2E"] #move nerf gun outward, inward, lens aperture open, close

def run_nerf_gun():
    #ser_head.write(init[0].encode('utf-8'))
    #ser_head.write(init[2].encode('utf-8'))
    print("Enter nerf gun wsad controls. Press f to fire. Press x to exit.")
    while(True):
        control = input()
        if control == "w":
            ser_nerf.write(commands[0].encode('utf-8'))
        if control == "s":
            ser_nerf.write(commands[1].encode('utf-8'))
        if control == "a":
            ser_nerf.write(commands[2].encode('utf-8'))
        if control == "d":
            ser_nerf.write(commands[3].encode('utf-8'))
        if control == "f":
            ser_nerf.write(commands[4].encode('utf-8')) 
        if control == "x":
            # ser_head.write(init[1].encode('utf-8'))
            #ser_head.write(init[3].encode('utf-8'))
            time.sleep(0.2)
            ser_nerf.close()
            break
    
          
    
        
