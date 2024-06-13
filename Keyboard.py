# -*- coding: utf-8 -*-
import curses
from ev3dev.auto import LargeMotor

# 포트를 지정하지 않고 모터 객체 생성
motor_left = LargeMotor()
motor_right = LargeMotor()


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
    motor_left.stop(stop_action="brake")
    motor_right.stop(stop_action="brake")


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
