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
#kommentar
#kommentar2
def run():
    Base.settings(225,225,100,100)
    Base.straight(340)
    Base.turn(-60)
    Base.turn(153) # fertig erste drehung
    Base.straight(470)#nach vorne
    MotorTop.run_angle(-720,360,Stop.HOLD,False)
    Base.straight(-80)
    MotorTop.run_angle(-720,270,Stop.HOLD,False)
    Base.straight(-100)#fertig absetzen
    Base.turn(45)
    MotorTop.run_angle(360,630,Stop.HOLD, False)
    Base.straight(260)
    Base.turn(-45)
    Base.straight(330)
    MotorTop.run_angle(-360,530,Stop.HOLD,True)
    Base.straight(370)
    MotorTop.run_angle(-360,55)
    Base.stop()
    Base.settings(400,400,150,150)
    Base.straight(-1620)
    MotorTop.run_angle(-360,118)

if __name__ == "__main__":
    run()
