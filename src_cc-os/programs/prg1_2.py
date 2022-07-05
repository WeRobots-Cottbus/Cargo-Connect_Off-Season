#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, "/home/robot/src_cc-os")

from botconfig import *
from toolkit import *

PrgName = __file__.split("/")[-1][:-3]

def run():
    Base.settings(150,150,300,300)
    while Base.distance() <= 816:
        Base.drive(200,-1)
    Base.stop()
    MotorLeft.brake()
    MotorRight.brake()

    MotorTop.run_angle(300,150,Stop.HOLD,True)

    Base.reset()
    while Base.distance() >= -816:
        Base.drive(-400,0)
    Base.stop()
    Base.turn(-90)

if __name__ == "__main__":
    run()
