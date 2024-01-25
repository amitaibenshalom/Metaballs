import pygame
from consts import *

class MarchingSquaresLoader():

    def __init__(self, width, height, resolution, metaballs, threshold):
        self.width = width
        self.height = height
        self.resolution = resolution
        self.metaballs = metaballs
        self.threshold = threshold
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Metaballs by Amitai Ben Shalom')
        self.screen.fill(bg_color)
        self.squaresWidth = resolution  # number of squares in x axis
        self.squaresHeight =int(height / width * resolution) # number of squares in y axis
        self.squareSide = width / resolution  # size of the side of the square

    def inc_resolution(self, r):
        if self.resolution == MIN_RESOLUTION and r < 0 or self.resolution == MAX_RESOLUTION and r > 0:
            return
        self.resolution += r
        self.squaresWidth = self.resolution
        self.squaresHeight =int(screen_height / screen_width * self.resolution) # number of squares in y axis
        self.squareSide = screen_width / self.resolution  # size of the side of the square

    def inc_threshold(self, t):
        if self.threshold <= MIN_THRESHOLD / self.width and t < 0 or self.threshold >= MAX_THRESHOLD / self.width and t > 0:
            return
        self.threshold += t

    def get_resolution(self):
        return self.resolution
    
    def get_num_of_balls(self):
        return len(self.metaballs)
    
    def get_threshold(self):
        return self.threshold

    def get_total_potential(self, x, y):
        p = 0
        for ball in self.metaballs:
            p += ball.get_potential(x,y)
        return p
    
    def above_threshold(self, x, y):
        if self.get_total_potential(x, y) > self.threshold:
            return 1
        return 0

    def get_square_case(self, r, c):
        index = self.above_threshold(c * self.squareSide, (r + 1) * self.squareSide) 
        index += 2 * self.above_threshold((c + 1) * self.squareSide, (r + 1) * self.squareSide)
        index += 4 * self.above_threshold((c + 1) * self.squareSide, r * self.squareSide)
        index += 8 * self.above_threshold(c * self.squareSide, r * self.squareSide)
        return index

    # draw square from lookup table
    def draw_by_index(self, index, r, c):
        if index == 0 or index == 15:  # no lines
            return
        if index == 6 or index == 9:  # vertical line
            pygame.draw.line(self.screen, line_color, (int((c + 0.5) * self.squareSide), r * self.squareSide),
                              (int((c + 0.5) * self.squareSide), (r + 1) * self.squareSide), line_width)
        elif index == 3 or index == 12:  # horizontal line
            pygame.draw.line(self.screen, line_color, (c * self.squareSide, int((r + 0.5) * self.squareSide)),
                              ((c + 1) * self.squareSide, int((r + 0.5) * self.squareSide)), line_width)
        elif index == 4 or index == 11:  # top-right corner or all other three corners
            pygame.draw.line(self.screen, line_color, (int((c + 0.5) * self.squareSide), r * self.squareSide),
                             ((c + 1) * self.squareSide, int((r + 0.5) * self.squareSide)), line_width)
        elif index == 7 or index == 8:  # top-left corner or all other three corners
            pygame.draw.line(self.screen, line_color, (c * self.squareSide, int((r + 0.5) * self.squareSide)),
                             (int((c + 0.5) * self.squareSide), r * self.squareSide), line_width)
        elif index == 1 or index == 14:  # bottom-left corner or ...
            pygame.draw.line(self.screen, line_color, (c * self.squareSide, int((r + 0.5) * self.squareSide)),
                             (int((c + 0.5) * self.squareSide), (r + 1) * self.squareSide), line_width)
        elif index == 2 or index == 13:  # bottom-right corner or ...
            pygame.draw.line(self.screen, line_color, (int((c + 0.5) * self.squareSide), (r + 1) * self.squareSide),
                             ((c + 1) * self.squareSide, int((r + 0.5) * self.squareSide)), line_width)
        elif index == 5:  # parallel lines up
             pygame.draw.line(self.screen, line_color, (c * self.squareSide, int((r + 0.5) * self.squareSide)),
                             (int((c + 0.5) * self.squareSide), r * self.squareSide), line_width)
             pygame.draw.line(self.screen, line_color, (int((c + 0.5) * self.squareSide), (r + 1) * self.squareSide),
                             ((c + 1) * self.squareSide, int((r + 0.5) * self.squareSide)), line_width)
        elif index == 10:  # parrallel lines down
            pygame.draw.line(self.screen, line_color, (c * self.squareSide, int((r + 0.5) * self.squareSide)),
                             (int((c + 0.5) * self.squareSide), (r + 1) * self.squareSide), line_width)
            pygame.draw.line(self.screen, line_color, (int((c + 0.5) * self.squareSide), r * self.squareSide),
                             ((c + 1) * self.squareSide, int((r + 0.5) * self.squareSide)), line_width)
            
    def draw(self):
        self.screen.fill(bg_color)
        for r in range (self.squaresHeight):
            for c in range (self.squaresWidth):
                self.draw_by_index(self.get_square_case(r, c), r, c)

    def move_balls(self):
        for ball in self.metaballs:
            ball.move()


            
        