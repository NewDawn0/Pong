#!/usr/bin/env python3
## Imports ##
import pygame; pygame.init()
from logger import Logger
## Constants ##
# Window
FPS = 60
WIDTH = 1000
HEIGHT = int(WIDTH * 0.5625)
FONT = pygame.font.SysFont("arial", 20)

# Objects
PADDLE_WIDTH = 20
PADDLE_HEIGHT = int(PADDLE_WIDTH * 5)
PADDLE_VELOCITY = 5
BALL_VELOCITY = 5
WINNING_SCORE = 10

# Colours
BGCOL = (31, 31, 31)
WHITE = (230, 230, 230)
BALLCOL = (134, 133, 239)
PLAYER1COL = (0, 198, 207)
PLAYER2COL = (213, 127, 109)

# Logger
logger = Logger()
