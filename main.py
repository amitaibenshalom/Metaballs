import pygame
import random
from pygame.constants import *
from consts import *
from Ball import *
from MSLoader import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    mballs = []
    for i in range(number_of_balls):
        mballs.append(Ball(random.randint(1, screen_width-1),random.randint(1, screen_height-1), random.randint(-10,10),random.randint(-10,10)))
    marchingSquaresManager = MarchingSquaresLoader(screen_width, screen_height, resolution, mballs, threshold)
    
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key >= pygame.K_0 and event.key <= pygame.K_6:
                    mballs.clear()
                    for i in range (event.key - pygame.K_0):
                        mballs.append(Ball(random.randint(1, screen_width-1),random.randint(1, screen_height-1), random.randint(-10,10),random.randint(-10,10)))
                elif event.key == pygame.K_LEFT:
                    marchingSquaresManager.inc_resolution(-10)
                elif event.key == pygame.K_RIGHT:
                    marchingSquaresManager.inc_resolution(10)
        marchingSquaresManager.move_balls()
        marchingSquaresManager.draw()
        clock.tick(fps)

main()
        