from model import Model


def makeMove(grid, depth):
    for x in xrange(4):


def decide(grid, depth):
    if depth % 2 == 0:
        return makeMove(grid, depth)
    else:
        return placeRandomBlock(grid, depth)


if __name__ == "__main__":
    while True:
        model = Model()
        grid = model.grid.copy()
        decide(grid, depth = 3)

