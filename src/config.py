from pygame import Color

BOX_SIZE = 190
BOX_COLOR = Color(255,0,0)
BACKGROUND_COLOR = Color(80,80,80)
LINE_COLOR = Color(200,200,200)
LINE_WIDTH = 5

def getDistance(num):
    return (num * BOX_SIZE + (num + 1) * LINE_WIDTH)
