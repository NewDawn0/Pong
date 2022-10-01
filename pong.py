#!/usr/bin/env python3
## Imports ##
import sys
from const import *
from init import Initializer
## Main Class ##
class Main(Initializer):
    def __init__(self):
        super().__init__()
    ## run ##
    def run(self):
        logger.log("info", "Starting mainlloop")
        while True:
            self.clock.tick(FPS)
            self.window.draw([self.lPaddle, self.rPaddle], self.ball, self.lScore, self.rScore)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.collision.movementHandler(keys, self.lPaddle, self.rPaddle)

            self.ball.move()
            self.collision.collisionHandler(self.ball, self.lPaddle, self.rPaddle)

            if self.ball.x < 0:
                self.rScore += 1
                self.ball.reset()
            elif self.ball.x > WIDTH:
                self.lScore += 1
                self.ball.reset()

            won = False
            if self.lScore >= WINNING_SCORE:
                won = True
                win_text = "Left Player Won!"
            elif self.rScore >= WINNING_SCORE:
                won = True
                win_text = "Right Player Won!"
    
            if won:
                text = FONT.render(win_text, 1, WHITE)
                logger.log("info", "calling wintext render function")
                self.window.drawWin(text, WIDTH//2 - text.get_width() //
                            2, HEIGHT//2 - text.get_height()//2)
                pygame.display.update()
                pygame.time.delay(10000)
                logger.log("info", "Resetting game")
                self.ball.reset()
                self.lPaddle.reset()
                self.rPaddle.reset()
                self.lScore = 0
                self.rScore = 0

if __name__ == '__main__':
    main = Main()
    main.run()
