#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from botconfig import *

"""
  for pixel placement       for text placement        for image placement
+---------------------+   +---------------------+   +---------------------+
|0,0             177,0|   |0,0              21,0|   |-177,-127    -177,127|
|                     |   |                     |   |                     |
|    Drawing Grid     |   |      Grid Array     |   |     Pixel Array     |
|                     |   |                     |   |                     |
|0,127         177,127|   |0,11            21,11|   |-177,127      177,127|
+---------------------+   +---------------------+   +---------------------+
"""
def DisplayText(text:str, coord:tuple[int,int]=(0,0), clear:bool=False, **kwargs) -> None:
    if clear: Brick.screen.clear()
    Brick.screen.draw_text(coord[0], coord[1], text, **kwargs)

#gyro geradeaus
def GyroDrive(origin:int=0) -> None:
    pass
