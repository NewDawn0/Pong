#!/usr/bin/env python3
## Imports ##
from lib.const import *
from sys import argv
from lib.paddle import Paddle
from lib.ball import Ball
from lib.window import Window
from lib.collision import Collision
## Initializer Class ##
class Initializer:
    def __init__(self):
        logger.log("info", "Initialising main")
        pygame.init()
        self.window = Window()
        self.clock = pygame.time.Clock()
        self.lPaddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT //
                         2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.rPaddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT //
                          2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = Ball(WIDTH // 2, HEIGHT // 2)

        self.lScore = 0
        self.rScore = 0
        self.collision = Collision()
        self.parseArgs()
    @staticmethod
    def parseArgs():
        for arg in argv:
            if arg in ("-h", "--help"):
                logger.log("info", "help")
            elif arg in ("-d", "--debug"):
                logger.log("info", "showing debug log")
                logger.setDebugLvl(4)
