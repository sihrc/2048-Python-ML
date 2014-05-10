# import pygame
import numpy as np
import random
import config as c

class Model:
    """ Encodes the game state for the Brick Breaker game """
   
    def __init__(self, size = (4,4)):
        """ Constructs a new Model object """
        self.gameover = False
        self.size = size
        self.grid = np.zeros(shape = size).astype('int')
        self.blocks = self.grid.tolist()
        self.hasMoved = False



    def reset(self):
        self.gameover = True
        self.__init__(size = self.size) 

    def update(self):
        if self.hasMoved:
            self.newBlock() 
            self.hasMoved = False

    def left(self):
        self.arrow_press(-1,1)

    def right(self):
        self.arrow_press(1,1)

    def down(self):
        self.arrow_press(1,0)

    def up(self):
        self.arrow_press(-1,0)

    def arrow_press(self, a, b):
        prev = self.grid.copy()
        grid = self.shift(a,b)
        if not self.has_moves() and len(np.where(self.grid == 0)[0]) == 0:
            self.gameover = True
        self.hasMoved = not (prev == self.grid).all()

    def has_moves(self):
        if (self.grid[1:,:] == self.grid[:-1,:]).any():
            return True
        if (self.grid[:,1:] == self.grid[:,:-1]).any():
            return True
        return

    def shift(self, way, axis):
        for y in xrange(self.size[axis]):
            curr = self.grid[y,:] if axis == 0 else self.grid[:,y]
            curr = sorted(curr,key = lambda x: way * (x != 0))
            range_ = range(len(curr))
            x = 0 if way == -1 else len(curr) - 1
            while True:
                c.printer(curr,"model")
                next_ = x - way
                if next_ in range_:
                    if curr[x] == 0 and curr[next_] == 0:
                        x -= way
                    elif curr[x] == 0:
                        curr[x] = curr[next_]
                        curr[next_] = 0
                        x += way
                    elif curr[next_] == curr[x]:
                        curr[x] *= 2
                        curr[next_] = 0
                    else:
                        x -= way
                else:
                    break
                c.printer(curr,"model")
            if axis == 0:
                self.grid[y,:] = curr
            else:
                self.grid[:,y] = curr
    

    def newBlock(self):
        rows, cols = np.where(self.grid == 0)
        if len(rows) == 0:
            return
        row,col = random.choice(zip(rows,cols))
        self.grid[row,col] = 2       

    def getBlocks(self):
        for x in xrange(self.size[0]):
            for y in xrange(self.size[1]):
                if self.grid[x,y] == 0:
                    self.blocks[x][y] = 0
                else:
                    self.blocks[x][y] = Block(x,y,self.grid[x,y])



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
