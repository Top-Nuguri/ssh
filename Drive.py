import sys
import keyboard
from ev3dev.ev3 import *

motor_left = LargeMotor('outB')
motor_right = LargeMotor('outC')

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

def main():
    try:
        while True:
            if keyboard.is_pressed('w'):
                forward()
            elif keyboard.is_pressed('s'):
                back()
            elif keyboard.is_pressed('a'):
                left()
            elif keyboard.is_pressed('d'):
                right()
            elif keyboard.is_pressed('space'):
                stop()
            elif keyboard.is_pressed('q'):
                break
    except KeyboardInterrupt:
        stop()
        print("프로그램이 중단되었으며 모터가 정지되었습니다.")

if __name__ == "__main__":
    main()