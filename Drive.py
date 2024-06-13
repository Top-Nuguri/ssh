import sys
import msvcrt
from ev3dev.ev3 import *

motor_left = LargeMotor('outB')
motor_right = LargeMotor('outC')

def getch():
    return msvcrt.getch().decode('utf-8')

def forward():
    motor_left.run_forever(speed_sp=450)
    motor_right.run_forever(speed_sp=450)

def back():
    motor_left.run_forever(speed_sp=-450)
    motor_right.run_forever(speed_sp=-450)

def left():
    motor_left.run_forever(speed_sp=-450)
    motor_right.run_forever(speed_sp=450)

def right():
    motor_left.run_forever(speed_sp=450)
    motor_right.run_forever(speed_sp=-450)

def stop():
    motor_left.run_forever(speed_sp=0)
    motor_right.run_forever(speed_sp=0)

while True:
    k = getch()
    print(k)
    if k == 'w':
        forward()
    if k == 's':
        back()
    if k == 'a':
        left()
    if k == 'd':
        right()
    if k == ' ':
        stop()
    if k == 'q':
        break