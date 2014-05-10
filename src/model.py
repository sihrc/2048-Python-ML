# import pygame
import numpy as np
import random

class Model():
    """ Encodes the game state for the Brick Breaker game """
   
    def __init__(self, size = (4,4)):
        """ Constructs a new Model object """
        self.gameover = False
        self.size = size
        self.grid = np.zeros(shape = size).astype('int')
        self.hasMoved = False
        self.newBlock()

    def reset(self):
        """
        Reset the game
        """
        self.gameover = True
        self.__init__(size = self.size) 

    def update(self):
        """
        Update the model and add a new random block
        """
        if self.hasMoved:
            self.newBlock() 
            self.hasMoved = False

    def move(self, direction):
        if direction == 0:   # UP
            a, b = (-1, 0)
        elif direction == 1: # RIGHT
            a, b = (1, 1)
        elif direction == 2: # DOWN
            a, b = (1, 0)
        elif direction == 3:                # LEFT
            a, b = (-1, 1)
        else:
            return

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




