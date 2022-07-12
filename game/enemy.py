from arcade import Sprite
from game.constants import RESOURCE_PATH
from time import time
from random import randint
import game.controller as controller

class Enemy(Sprite):
    
    def __init__(self, enemy_name, size, word, position):
        super().__init__(f"{RESOURCE_PATH}/enemy_sprites/{enemy_name}.png", size)

        self.shot = False
        self.word = word
        self.start = None
        self.list_position = position
        self.random_color()

    def update(self):
        if self.start == None:
            self.start = time()
            self.end = self.start + 10
        if self.shot == True:
            self.remove_from_sprite_lists()
        self.start = int(self.end - time())
        
    def random_color(self):
        r = randint(0,200)
        g = randint(0,200)
        b = randint(0,200)

        self.color = (r,g,b)