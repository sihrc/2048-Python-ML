import pygame
import numpy as np
import config as c

class Model:
    """ Encodes the game state for the Brick Breaker game """
   
    def __init__(self, size = (4,4)):
        """ Constructs a new Model object """
        self.size = size
        self.blocks = [Block(c.getDistance(x), c.getDistance(y),c.BOX_SIZE,c.BOX_SIZE,c.BOX_COLOR) for x in xrange(size[0]) for y in xrange(size[1])]

    def update(self):
        pass

    def change_paddle_velocity(self,acceleration):
        self.paddle.velocity_x += acceleration


class Block:
    """ Encodes the state of a brick """
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def update(self):
        """ Update Brick state """
        pass
