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

def test():
    pass

if __name__ == "__main__":
    # test(1,0) # right
    # test(-1,0) # left
    # test(1,1) # down
    test(-1,1) # up