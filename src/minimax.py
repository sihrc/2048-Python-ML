from model import Model
from view import View

import pygame
import numpy as np
import time

_LOSE_ = -9999999
mapper = np.array([\
    [64 ,16 ,2  ,1],
    [16 ,2  ,1  ,-2],
    [2  ,1  ,-2  ,-16],
    [1  ,-2  ,-16  ,-64]
    ])

class Node:
    def __init__(self, move, grid):
        self.score = 0
        self.move = move
        self.grid = grid.copy()
        self.invalid = False
        self.makemove()
        self.children = []

    def bestMove(self):
        # return max(self.children, key = lambda x: x.score).move
        best = None
        score = _LOSE_
        for node in self.children:
            # print node.move, node.score, node.invalid
            if score < node.score and not node.invalid:
                best = node.move
                score = node.score
        return best

    def makemove(self):
        if self.move >= 4:
            return
        model = Model()
        model.grid = self.grid.copy()
        model.move(self.move)
        if (self.grid == model.grid).all():
            self.invalid = True
        self.grid = model.grid.copy()

    def getScore(self):
        for node in self.children:
            self.score += node.score



def evaluate(grid):
    """
    Board evaluation function
    """
    return np.sum(mapper * grid)


def decide(node, depth):
    if depth == 0:
        node.score = evaluate(node.grid)
        return node

    if depth % 2 == 1:
        for x in xrange(4):
            node.children.append(decide(Node(x, node.grid), depth - 1))
        node.getScore()
        return node
    else:
        for row, col in zip(*np.where(node.grid == 0)):
            newnode = Node(move = 4, grid = node.grid)
            newnode.grid[row, col] = 2
            node.children.append(decide(newnode, depth - 1))
        node.getScore()
        return node



if __name__ == "__main__":
    # pygame.init()
    while True:
        current_model = Model()
        # view = View(current_model)
        while True:
            grid = current_model.grid.copy()
            if len(np.where(grid != 0)[0]) > 8:
                depth = 5
            else:
                depth = 3
            node = decide(Node(5, grid), depth = depth)
            move = node.bestMove()
            if move == None:
                print "GAMEOVER"
                break
            current_model.move(move)
            # view.draw()
            current_model.update()
            # view.draw()
        print np.max(node.grid)
