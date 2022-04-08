import pygame
from ca import *


class ui:
    # white color
    WHITE = (255,255,255)
    # light shade of the button
    color_light = (170,170,170)
    # dark shade of the button
    color_dark = (100,100,100)
    
    def __init__(self, x, y, width, heigth):
        self.x = x
        self.y = y
        self.width = width
        self.height = heigth
    
    def button_clicked(self, mouse, screen):
        mouse = pygame.mouse.get_pos()
        # if the mouse is in the button
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            return True
    
    def get_coordinates(self):
        return self.x, self.y, self.width, self.height
    

