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
        return -10
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
        xmodel = Model()

        xmodel.grid = model.grid.copy()
        xmodel.up()
        moves.append((evaluateGrid(xmodel.grid, grid), model.up))

        xmodel.grid = model.grid.copy()
        xmodel.right()
        moves.append((evaluateGrid(xmodel.grid, grid), model.right))

        xmodel.grid = model.grid.copy()
        xmodel.down()
        moves.append((evaluateGrid(xmodel.grid, grid), model.down))

        xmodel.grid = model.grid.copy()
        xmodel.left()
        moves.append((evaluateGrid(xmodel.grid, grid), model.left))
        moves.sort()
        moves[-1][1]()

        view.draw()
        wait()
        model.update()
        view.draw()
        wait()

    pygame.quit()
