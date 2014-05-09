import pygame
from pygame.locals import *

from controller import *
from view import *
from model import *
from config import printer

import time
import copy

def evaluateGrid(grid, oldgrid):
    if (oldgrid == grid).all():
        return -100000
    empty = len(np.where(grid == 0)[0])
    points = np.sum(grid)
    return empty * 15 + points

def wait():
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == KEYDOWN and event.key == K_f:
    #             return
    time.sleep(.1)


if __name__ == "__main__":
    pygame.init()
    num_blocks = (4,4)
    
    model = Model(size = num_blocks)
    model.newBlock()

    view = View(model)
    view.draw()

    while True:
        moves = []
        original = model.grid.copy()
        for move in [model.up, model.right, model.down, model.left]:
            model.grid = original.copy()
            move()
            moves.append((evaluateGrid(model.grid, original), move))

        moves.sort()
        moves[-1][1]()

        view.draw()
        wait()
        model.update()
        view.draw()
        wait()

    pygame.quit()
