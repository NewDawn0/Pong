#!/usr/bin/env python3
## Logger class ##
class Logger:
    debugLvl = 0
    def __init__(self):
        self.noCol = '\033[m'
        self.type = {
            'err': ['\033[31m', 'ERROR     ', 1],
            'warning': ['\033[33m', 'WARNING   ', 2],
            'info': ['\033[32m', 'INFO      ', 3]
        }
    def log(self, type, msg):
        if self.debugLvl >= self.type[type][2]: 
            print(f"{self.type[type][0]}{self.type[type][1]}{self.noCol}{msg}")
    def addType(self, type):
        self.type[type[0]] = type[1]
    def delType(self, type):
        del self.type[type]
    def overwriteType(self, type, target):
        self.addType(type)
        self.delType(target)
    @classmethod
    def setDebugLvl(cls, debugLvl):
        cls.debugLvl = debugLvl
    def test(self):
        for key in self.type:
            print(f"{key} => {self.type[key]}")
