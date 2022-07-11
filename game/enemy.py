from arcade import Sprite
from game.constants import RESOURCE_PATH
from math import radians
from random import randint

class Enemy(Sprite):
    
    def __init__(self, enemy_name, size, word, position):
        super().__init__(f"{RESOURCE_PATH}/enemy_sprites/{enemy_name}.png", size)

        self.shot = False
        self.word = word
        self.list_position = position
        self.random_color()

    def update(self):
        if self.shot == True:
            self.remove_from_sprite_lists()
        
    def random_color(self):
        r = randint(0,200)
        g = randint(0,200)
        b = randint(0,200)

        self.color = (r,g,b)