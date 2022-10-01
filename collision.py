#!/usr/bin/env python3
from const import *
from ball import Ball
from paddle import Paddle
## Collision Class ##
class Collision:
    @staticmethod
    def collisionHandler(ball: Ball, lPaddle: Paddle, rPaddle: Paddle):
        if ball.y + ball.height >= HEIGHT:
            ball.yVel *= -1
        elif ball.y - ball.height <= 0:
            ball.yVel *= -1
        if ball.xVel < 0 and (ball.y >= lPaddle.y and ball.y <= lPaddle.y + lPaddle.height) and (ball.x - ball.height <= lPaddle.x + lPaddle.width):
            ball.xVel *= -1
            middle_y = lPaddle.y + lPaddle.height / 2
            difference_in_y = middle_y - ball.y
            reduction_factor = (lPaddle.height / 2) / ball.BALL_VELOCITY
            y_vel = difference_in_y / reduction_factor
            ball.yVel = -1 * y_vel
        elif ball.y >= rPaddle.y and ball.y <= rPaddle.y + rPaddle.height and ball.x + ball.height >= rPaddle.x:
            ball.xVel *= -1
            middle_y = rPaddle.y + rPaddle.height / 2
            difference_in_y = middle_y - ball.y
            reduction_factor = (rPaddle.height / 2) / ball.BALL_VELOCITY
            y_vel = difference_in_y / reduction_factor
            ball.yVel = -1 * y_vel
    @staticmethod
    def movementHandler(keys: pygame.key.ScancodeWrapper, lPaddle: Paddle, rPaddle: Paddle):
        if keys[pygame.K_w] and lPaddle.y - lPaddle.PADDLE_VELOCITY >= 0:
            lPaddle.move(up=True)
        if keys[pygame.K_s] and lPaddle.y + lPaddle.PADDLE_VELOCITY + lPaddle.height <= HEIGHT:
            lPaddle.move(up=False)
        if keys[pygame.K_UP] and rPaddle.y - rPaddle.PADDLE_VELOCITY >= 0:
            rPaddle.move(up=True)
        if keys[pygame.K_DOWN] and rPaddle.y + rPaddle.PADDLE_VELOCITY + rPaddle.height <= HEIGHT:
            rPaddle.move(up=False)
