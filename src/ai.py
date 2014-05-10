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
        return -1000
    empty = len(np.where(grid != 0)[0])
    points = np.sum(mapper * grid)
    return empty * -20 + points

def wait():
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == KEYDOWN and event.key == K_f:
    #             return
    time.sleep(.01)

def transform(mapper):
    gaus = np.random.normal(0, 1, size = (4,4))
    mapper += gaus
    return mapper
# mapper = np.array([\
# [10,5,5,10],
# [5,1,1,5],
# [5,1,1,5],
# [10,5,5,10]
# ])


if __name__ == "__main__":
    pygame.init()
    num_blocks = (4,4)
    mapper = np.ones((4,4))

    results = (0, mapper)

    while True:
        model = Model(size = num_blocks)
        model.newBlock()
        # results.sort()
        mapper = transform(results[1])
        # view = View(model)
        # view.draw()
        count = 0
        while True:
            moves = []
            original = model.grid.copy()
            for move in [model.up, model.right, model.down, model.left]:
                model.grid = original.copy()
                move()
                moves.append((evaluateGrid(model.grid.copy(), original), move))

            moves.sort()
            moves[-1][1]()

            if (original == model.grid).all():
                count +=1
                if count > 10:
                    break
            else:
                count = 0
            # view.draw()
            # wait()
            model.update()
            # view.draw()
            # wait()
        score = np.max(model.grid) * 16 + np.sum(model.grid)
        if score > results[0]:
            print np.max(model.grid), score
            results = (score, mapper)

    pygame.quit()
