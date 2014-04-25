import pygame
from pygame.locals import *

from controller import *
from view import *
from model import *

import time

if __name__ == "__main__":
    pygame.init()
    num_blocks = (4,4)
    
    model = Model(size = num_blocks)
    view = View(model)
    controller = Controller(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)

        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()