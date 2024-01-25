# class of metaball
from consts import *
import math

class Ball:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x >= screen_width or self.x <= 0:
            self.vx = -self.vx
        if self.y >= screen_height or self.y <= 0:
            self.vy = -self.vy

    def get_potential(self, x, y):
        if self.x == x and self.y == y:
            return float('inf')
        return (1 / math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2))
