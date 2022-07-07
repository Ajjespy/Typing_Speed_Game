from arcade import Sprite
from game.constants import RESOURCE_PATH
from math import radians

class Enemy(Sprite):
    
    def __init__(self, enemy_name, size, word):
        super().__init__(f"{RESOURCE_PATH}/enemy_sprites/{enemy_name}.png", size)

        self.shot = False
        self.word = word

    def update(self):
        if self.shot == True:
            self.remove_from_sprite_lists

