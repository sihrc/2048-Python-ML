from model import *

import time


def evaluateGrid(grid, oldgrid):
    if (oldgrid == grid).all():
        return -1000
    empty = len(np.where(grid != 0)[0])
    if empty == 16:
        return -100000
    points = np.sum(mapper * grid)
    return empty * -20 + points

def wait():
    time.sleep(.01)

def transform(mapper):
    gaus = np.random.normal(0, 1, size = (4,4))
    mapper += gaus
    return mapper


if __name__ == "__main__":
    num_blocks = (4,4)
    mapper = np.ones((4,4))
    results = (0, mapper)

    while True:
        model = Model(size = num_blocks)
        model.newBlock()
        mapper = transform(results[1])
        count = 0
        while True:
            moves = model.grid.copy()
            best = -100000
            original = model.grid.copy()
            for move in xrange(4):
                model.grid = original.copy()
                model.move(move)
                curr = evaluateGrid(model.grid.copy(), original)
                if best < curr:
                    best = curr
                    moves = model.grid.copy()
            model.grid = moves.copy()
            if (original == model.grid).all():
                count +=1
                if count > 10:
                    break
            else:
                count = 0
            model.update()

        score = np.max(model.grid) * 16 + np.sum(model.grid)
        if score > results[0]:
            print np.max(model.grid), score
            print 
            results = (score, mapper)

