#!/usr/bin/env python3
## Imports ##
from const import *
from util import *
from random import randint
## Fn && Classes ##
# lambda generate random num
genY = lambda limit: randint(limit*-1, limit)
# gen random number except 0
def genX(min=3, max=10) -> int:
    val = randint(0, 1)
    if val == 0:
        return randint(max *-1, min *-1)
    return randint(min, max)
# alternating iterator enum
def iterator():
    while True:
        yield PLAYER1COL
        yield PLAYER2COL

