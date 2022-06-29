import arcade
import game.constants as const
from math import radians

class Tumbleweed(arcade.Sprite):
    
    def __init__(self, starting_x, starting_y, size, tumble_path, speed, pause_next, spin):
        super().__init__()
        self.texture = arcade.load_texture(f"{const.RESOURCE_PATH}Tumbleweed.png")
        # Where the tumbleweed starts
        self.center_x = starting_x
        self.center_y = starting_y

        # The size of the tumble weed. In mainmenu this is set as 0.5 making it half the size of the sprite.
        self.scale = size
        
        # A list of y changes. One index is applied till the next_y is met.
        self.path = tumble_path

        # The speed which the tumbleweed move left or right.
        self.speed = speed
        
        # The speed which the tumbleweed spins.
        self.turn = spin

        # Where it is in the tumble_path.
        self.path_point = 0

        # Countdown till the tumbleweed will move on in the list.
        self.next_y = 0

        # The number the next_y must meet to move onto the next index in the list.
        self.pause_next = pause_next

    def update(self):

        if self.next_y > self.pause_next:
            self.next_y = 0
            self.path_point += 1

            if self.path_point == len(self.path):
                self.path_point = 0
                # sound maybe?
        else:
            self.next_y += 1

        y = self.path[self.path_point]

        self.center_x += self.speed
        self.center_y += y

        angle_rad = radians(self.turn)

        self.angle += angle_rad

