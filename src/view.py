import config as c
import pygame

class View:
    """ Encodes a view of the BrickBreaker game in a PyGame window """
    def __init__(self, model):
        """ Constructs a PyGameWindowView object
            screen: the window to draw the game to
            model: the Brick Breaker game state """
        self.model = model
        self.screen = self.create_screen()
            
    def create_screen(self):
        rows, cols = self.model.size
        self.screen_size = c.getDistance(rows), c.getDistance(cols)
        return pygame.display.set_mode(self.screen_size)

    def draw_lines(self):
        rows, cols = self.model.size
        for x in xrange(rows + 1):
            pygame.draw.rect(self.screen, c.LINE_COLOR, pygame.Rect(c.getDistance(x) - c.LINE_WIDTH,0,c.LINE_WIDTH,self.screen_size[1]))
        for y in xrange(cols + 1):
            pygame.draw.rect(self.screen, c.LINE_COLOR, pygame.Rect(0, c.getDistance(y) - c.LINE_WIDTH, self.screen_size[0], c.LINE_WIDTH))

    def draw_blocks(self):
        for block in self.model.blocks:
            pygame.draw.rect(self.screen, block.color, pygame.Rect(block.x,block.y,block.width,block.height))

    def draw(self):
        """ Draws the game state to the PyGame window """
        self.screen.fill(c.BACKGROUND_COLOR)
        self.draw_lines()
        self.draw_blocks()
        pygame.display.update()