from pygame import Color


BOX_SIZE = 190
BOX_COLOR = Color(255,0,0)
BACKGROUND_COLOR = Color(80,80,80)
LINE_COLOR = Color(200,200,200)
LINE_WIDTH = 5

def getDistance(num):
    return (num * BOX_SIZE + (num + 1) * LINE_WIDTH)

def printer(message, tag):
    allow = [
    "controller",
    ]
    if tag in allow:
        print "%s:\t\t%s" % (tag,message)

def test(way, axis):
    import numpy as np
    size = (4,4)
    a = np.array([[0,0,2,2],[4,2,0,4],[4,2,0,0],[0,0,4,4]])
    for y in xrange(size[axis]):
        curr = a[y,:] if axis == 0 else a[:,y]
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
            a[y,:] = curr
        else:
            a[:,y] = curr

if __name__ == "__main__":
    # test(1,0) # right
    # test(-1,0) # left
    # test(1,1) # down
    test(-1,1) # up