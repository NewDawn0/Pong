#!/usr/bin/env python3
## Imports ##
import pygame
from const import *
from util import genX, genY
from baseObj import Obj
from logger import Logger
logger.addType(('debug', ['\033[33m', 'DEBUG     ', 2]))
## Ball Class ##
class Ball(Obj):
    BALL_VELOCITY = BALL_VELOCITY
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.xVel = genX()
        self.yVel = genY(1)
        logger.log("debug", f"BAll X and Y\nX => {self.xVel}\nY => {self.yVel}\n")
    def move(self):
        self.xVel *= 1.001
        self.yVel *= 1.001
        self.x += self.xVel
        self.y += self.yVel
    def resetBall(self):
        self.reset()
        self.xVel = genX()
        self.yVel = genY(2)
        logger.log("debug", f"BAll X and Y\nX => {self.xVel}\nY => {self.yVel}\n")

