import arcade
import game.constants as const
from math import radians

class Enemy(arcade.Sprite):
    
    def __init__(self, enemy_name, size, word):
        super().__init__(f"{const.RESOURCE_PATH}/enemy_sprites/{enemy_name}.png", size)

        self.shot = False
        self.word = word

    def update(self):
        if self.shot == True:
            self.remove_from_sprite_lists

