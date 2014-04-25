from pygame.locals import *
import pygame

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
        if event.key == pygame.K_LEFT:
            print "LEFT"
        elif event.key == pygame.K_RIGHT:
            print "RIGHT"
        elif event.key == pygame.K_UP:
            print "UP"
        elif event.key == pygame.K_DOWN:
            print "DOWN"