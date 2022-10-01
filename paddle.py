#!/usr/bin/env python3
## Imports ##
import pygame
from const import *
from baseObj import Obj
## Paddle Class ##
class Paddle(Obj):
    PADDLE_VELOCITY = PADDLE_VELOCITY
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.override(PADDLE_WIDTH, PADDLE_HEIGHT)
    def move(self, up=True):
        if up: self.y -= self.PADDLE_VELOCITY
        else: self.y += self.PADDLE_VELOCITY
    def reset(self):
        self.x = self.origX
        self.y = self.origY

