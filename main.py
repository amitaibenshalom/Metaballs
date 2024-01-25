import pygame
import random
from pygame.constants import *
from consts import *
from Ball import *
from MSLoader import *

pygame.font.init()
font = pygame.font.SysFont('Calibri', 30)

def show_configuration(msm):
    global font
    text_surface = font.render('Balls: ' + str(msm.get_num_of_balls()) + ", Resolution: " + str(msm.get_resolution()), False, (255,255,255))
    msm.screen.blit(text_surface, (0,0))

def main():
    global number_of_balls, resolution
    pygame.init()
    clock = pygame.time.Clock()
    freeze = False
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
                elif event.key == pygame.K_SPACE:
                    freeze = not freeze
                elif event.key >= pygame.K_0 and event.key <= pygame.K_6:
                    mballs.clear()
                    number_of_balls = event.key - pygame.K_0
                    for i in range (event.key - pygame.K_0):
                        mballs.append(Ball(random.randint(1, screen_width-1),random.randint(1, screen_height-1), random.randint(-10,10),random.randint(-10,10)))
                elif event.key == pygame.K_LEFT:
                    marchingSquaresManager.inc_resolution(-10)
                elif event.key == pygame.K_RIGHT:
                    marchingSquaresManager.inc_resolution(10)
        if not freeze: marchingSquaresManager.move_balls() 
        marchingSquaresManager.draw()
        show_configuration(marchingSquaresManager)
        pygame.display.flip()
        clock.tick(fps)

main()
        