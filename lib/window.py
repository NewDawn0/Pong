#!/usr/bin/env python3
## Imports ##
import pygame
import sys
from lib.const import *
from lib.util import *
from lib.paddle import Paddle
from lib.ball import Ball
## Window Class ##
class Window:
    def __init__(self):
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    def draw(self, paddles: tuple[Paddle, Paddle], ball: Ball, lScore: int, rScore: int):
        self.screen.fill(BGCOL)
        lScoreTxt = FONT.render(f"{lScore}", 1, WHITE)
        rScoreTxt = FONT.render(f"{rScore}", 1, WHITE)
        self.screen.blit(lScoreTxt, (WIDTH//4 - lScoreTxt.get_width()//2, 20))
        self.screen.blit(rScoreTxt, (WIDTH*0.75 - rScoreTxt.get_width()//2, 20))

        iter = iterator()
        for paddle in paddles:
            paddle.drawRect(self.screen, next(iter))
        ball.drawCirc(self.screen, BALLCOL)
        pygame.display.update()
    def drawWin(self, text: str, x: int, y: int):
        self.screen.blit(text, (x, y))
