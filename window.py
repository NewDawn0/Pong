#!/usr/bin/env python3
## Imports ##
import pygame
import sys
from const import *
from util import *
## Window Class ##
class Window:
    def __init__(self):
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    def draw(self, paddles, ball, lScore, rScore):
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
    def drawWin(self, text, x, y):
        self.screen.blit(text, (x, y))
