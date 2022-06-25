#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import sys, os
sys.path.insert(0, os.path.abspath("../"))

from botconfig import *
from toolkit import *

PrgName = os.path.basename(__file__).removesuffix(".py")

def run():
    Base.settings(500,500,300,300)
    #
    Base.straight(600)
    Base.turn(60)
    Base.straight(380)
    Base.straight(-70)
    MotorTop.run_angle(-620,100)
    Base.straight(-800)

if __name__ == "__main__":
    run()