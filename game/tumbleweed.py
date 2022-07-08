from arcade import Sprite, load_texture
from game.constants import RESOURCE_PATH
from math import radians

class Tumbleweed(Sprite):
    
    def __init__(self, starting_x, starting_y, size, tumble_path, speed, pause_next, spin):
        super().__init__()
        
        self.texture = load_texture(f"{RESOURCE_PATH}Tumbleweed.png")
        # Where the tumbleweed starts
        self.center_x = starting_x
        self.center_y = starting_y

        #  The size of the tumble weed. In mainmenu this is set as 0.5 making it half the size of the sprite.
        self.scale = size
        
        #  A list of y changes. One index is applied till the next_y is met.
        self.path = tumble_path

        #  The speed which the tumbleweed move left or right.
        self.speed = speed
        
        #  The speed which the tumbleweed spins.
        self.turn = spin

        #  Where it is in the tumble_path.
        self.path_point = 0

        #  Countdown till the tumbleweed will move on in the list.
        self.next_y = 0

        #  The number the next_y must meet to move onto the next index in the list.
        self.pause_next = pause_next

    def update(self):

        #  This is the delay between each movement section
        if self.next_y > self.pause_next:
            self.next_y = 0
            self.path_point += 1

            if self.path_point == len(self.path):
                self.path_point = 0
                #  sound maybe?
        else:
            self.next_y += 1

        #  Sets the y direction for the tumbleweed    
        y = self.path[self.path_point]

        #  Updates the tumbleweeds position
        self.center_x += self.speed
        self.center_y += y

        #  The amount the tumbleweed wil turn
        angle_rad = radians(self.turn)
        #  The tumbleweed turning
        self.angle += angle_rad

