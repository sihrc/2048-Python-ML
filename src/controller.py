from pygame.locals import *
import pygame

import config as c

class Controller:
    """ Controls Brick Breaker using the keyboard """
    
    def __init__(self, model):
        """ Constructs a PyGameKeyboardController object
            model: the Brick Breaker game state """
        self.model = model
    
    def handle_pygame_event(self, event):
        """ handles a PyGame key down event
            event: a PyGame event of type KEYDOWN """
        if event.type != KEYDOWN:
            # nothing to do
            return
        if event.key == pygame.K_UP:
            c.printer("UP", "controller")
            self.model.move(0)
            self.model.update()
        elif event.key == pygame.K_RIGHT:
            c.printer("RIGHT", "controller")
            self.model.move(1)
            self.model.update()
        elif event.key == pygame.K_DOWN:
            c.printer("DOWN", "controller")
            self.model.move(2)
            self.model.update()
        elif event.key == pygame.K_LEFT:
            c.printer("LEFT", "controller")
            self.model.move(3)
            self.model.update() 

        