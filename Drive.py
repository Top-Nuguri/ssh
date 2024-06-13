import curses
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


def main(stdscr):
    # curses 초기 설정
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        key = stdscr.getch()
        if key != -1:
            # 키 입력이 있을 때
            if key == ord('w'):
                forward()
            elif key == ord('s'):
                back()
            elif key == ord('a'):
                left()
            elif key == ord('d'):
                right()
            elif key == ord(' '):
                stop()
            elif key == ord('q'):
                break


curses.wrapper(main)
