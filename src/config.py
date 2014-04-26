from pygame import Color

def getDistance(num):
    return (num * BOX_SIZE + (num + 1) * LINE_WIDTH)

def printer(message, tag):
    allow = [
    # "controller",
    # "model",
    ]
    if tag in allow:
        print "%s:\t\t%s" % (tag,message)

def getColor(h):
    def hsvToRGB(h, s, v):
        """Convert HSV color space to RGB color space
        
        @param h: Hue
        @param s: Saturation
        @param v: Value
        return (r, g, b)  
        """
        import math
        hi = math.floor(h*6)
        f =  (6*h) - hi
        p = v * (1.0 - s)
        q = v * (1.0 - (f*s))
        t = v * (1.0 - ((1.0 - f) * s))
        return {
            0: (v, t, p),
            1: (q, v, p),
            2: (p, v, t),
            3: (p, q, v),
            4: (t, p, v),
            5: (v, p, q),
        }[hi]

    h += 0.618033988749895
    h %= 1
    
    R,G,B = hsvToRGB(h, 0.5, 0.55)

    print R,G,B
    return h,Color(int(256*R),int(256*G),int(256*B))
    
BOX_SIZE = 190
BACKGROUND_COLOR = Color(80,80,80)
LINE_COLOR = Color(200,200,200)
LINE_WIDTH = 5

BOX_COLOR = {}
h = 100
for num in xrange(15):
    h,color = getColor(h)
    BOX_COLOR[2**num] = color



def test():
    pass

if __name__ == "__main__":
    test