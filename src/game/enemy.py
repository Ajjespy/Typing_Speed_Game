from arcade import Sprite
from game.constants import RESOURCE_PATH
from math import radians

class Enemy(Sprite):
    
    def __init__(self, enemy_name, size, word, position):
        super().__init__(f"{RESOURCE_PATH}/enemy_sprites/{enemy_name}.png", size)

        self.shot = False
        self.word = word
        self.list_position = position

    def update(self):
        if self.shot == True:
            self.remove_from_sprite_lists()

