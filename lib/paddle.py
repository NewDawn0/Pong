#!/usr/bin/env python3
## Imports ##
import pygame
from lib.const import *
from lib.baseObj import Obj
## Paddle Class ##
class Paddle(Obj):
    PADDLE_VELOCITY = PADDLE_VELOCITY
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.override(PADDLE_WIDTH, PADDLE_HEIGHT)
    def move(self, up: bool=True):
        if up: self.y -= self.PADDLE_VELOCITY
        else: self.y += self.PADDLE_VELOCITY

