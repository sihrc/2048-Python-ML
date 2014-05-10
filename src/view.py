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
        self.blocks = self.model.grid.tolist()            
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
        self.getBlocks()
        myfont = pygame.font.SysFont("monospace", 50)
        for list_blocks in self.blocks:
            for block in list_blocks:
                if block == 0:
                    continue
                # pygame.draw.
                pygame.draw.rect(self.screen, block.color, pygame.Rect(block.x,block.y,block.width,block.height))
                number = myfont.render("%d" % block.value, 1, (255,255,255))
                self.screen.blit(number, (block.x + block.width/2 - 20, block.y + block.height/2 - 20))

    def getBlocks(self):
        for x in xrange(self.model.size[0]):
            for y in xrange(self.model.size[1]):
                if self.model.grid[x,y] == 0:
                    self.blocks[x][y] = 0
                else:
                    self.blocks[x][y] = Block(x,y,self.model.grid[x,y])

    def draw(self):
        """ Draws the game state to the PyGame window """
        self.screen.fill(c.BACKGROUND_COLOR)
        self.draw_lines()
        self.draw_blocks()
        pygame.display.update()



class Block:
    """ Encodes the state of a brick """
    def __init__(self,posx,posy, value = 2):
        self.value = value
        self.posx = posx
        self.posy = posy
        self.width = c.BOX_SIZE
        self.height = c.BOX_SIZE
        self.color = c.BOX_COLOR[self.value]
        self.update()

    def update(self):
        """ Update Brick state """
        self.x = c.getDistance(self.posx)
        self.y = c.getDistance(self.posy)
