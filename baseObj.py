#!/usr/bin/env python3
## Imports ##
import pygame
## Rectangle Class ##
class Obj:
    def __init__(self, x, y):
        self.origX = x
        self.origY = y
        self.x = self.origX
        self.y = self.origY
        self.height = 10 # default
        self.width = 10 # default
    def override(self, width, height):
        self.height = height
        self.width = width
    def reset(self):
        self.x = self.origX
        self.y = self.origY
    def drawRect(self, win, col):
        pygame.draw.rect(win, col, (self.x, self.y, self.width, self.height))
    def drawCirc(self, win, col):
        pygame.draw.circle(win, col, (self.x, self.y), self.height)

