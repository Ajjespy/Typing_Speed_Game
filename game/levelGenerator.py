import arcade
import game.controller
from game.constants import RESOURCE_PATH, MUSIC_HANDLER, MUSIC_DICT
from game.random_word import RandomWord
from time import time
from random import randint
from game.enemy import Enemy

class LevelGenerator(arcade.View):
    def __init__(self):
        super().__init__()
        self.background = None
        self.buttons = False
        self.enemy_list = arcade.SpriteList()
        self.enemy_names_list = ["Friendly Tim", "Knife Goose", "Knife Lady", "Rangoon", "Shady Jim", "Unfriendly Tim"]
        
    def setup(self, difficulty = "ALL"):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.background = arcade.load_texture(f"{RESOURCE_PATH}backgrounds/ShootZone.png")
            
        self.userType = ""
        self.last_time = 0
        self.num_words = 0
        self.start_type_time = None
        self.end_type_time = None

        self.enemy_pos = [-1, -1, -1]

        # add first enemy
        if self.num_words == 0:
            self.add_enemy(self.enemy_names_list[0], .5, RandomWord.get_word(randint(1, 8)), 0)

        MUSIC_HANDLER.play_song(MUSIC_DICT["wind"])  # add music here


    def on_draw(self):
        super().on_draw()
        arcade.start_render()
        # background gets drawn first
        arcade.draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)

        arcade.draw_text(self.userType, self.window.width / 2 - 44 * 5.5, 125, arcade.color.BLUE, 44, 400, "left", font_name="Ultra")
        arcade.draw_text(f"Sec: {int(self.last_time)}", self.window.width - 400, self.window.height - 48, arcade.color.GREEN, 44, 500, "center", "Ultra")  
        arcade.draw_text(f"Words: {self.num_words}", self.window.width - 450, self.window.height - 100, arcade.color.GREEN, 44, 500, "center", "Ultra")

        for enemy in self.enemy_list:
            enemy.draw()
            arcade.draw_text(enemy.word, enemy.center_x, enemy.center_y, arcade.color.BLUE, 44, 400, "left", font_name="Ultra")


    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        # checks if the user has typed in the correct word
        self.enemy_list.update()

        # stat checker stuff will be gone when stattracker is finished
        if not (self.start_type_time == None or self.end_type_time == None):
            self.end_type_time = None
            self.start_type_time = None
        
        # add more ememies based on number of words user has typed
        if not len(self.enemy_list) >= 3:
            pos = randint(0,2)
            while self.enemy_pos[pos] > 0:
                pos = randint(0,2)
            self.add_enemy(self.enemy_names_list[randint(0, len(self.enemy_names_list) - 1)], .75, RandomWord.get_word(randint(1, 8)), pos)

    def on_key_press(self, symbol: int, modifiers: int):
        game.controller.get_key_press(self, symbol)
        if symbol > 96 and symbol < 123:
            # basic stat checker will be finished in stat checker file
            if self.end_type_time == None and self.start_type_time == None:
                self.start_type_time = time()
            
            # checks for upper case chars
            if modifiers % 2 == 1:
                self.userType = self.userType + chr(symbol).upper()
            else:
                self.userType = self.userType + chr(symbol)
        if symbol == arcade.key.BACKSPACE:
            self.userType = self.userType[:-1]

        if symbol == arcade.key.ENTER:
            self.on_enter()
            
            
    def on_key_release(self, symbol: int, modifiers: int):
        # lets controller know that a key has become unpressed
        game.controller.get_key_press(self, symbol, True)

    def add_enemy(self, enemy_name, size, word, pos_index):
        self.width = self.window.width
        self.height = self.window.height
        position_list = [[self.width/7,self.height/2.5], [self.width/1.5,self.height/2], [self.width/1.1,self.height/3.5]]
        enemy = Enemy(enemy_name, size, word, pos_index)
        pos = position_list[pos_index]
        enemy.center_x = pos[0]
        enemy.center_y = pos[1]
        self.enemy_list.append(enemy)
        self.enemy_pos[pos_index] = 1

    def on_enter(self):
        for enemy in self.enemy_list:
            if len(self.userType) > len(enemy.word) - 1 and self.userType == enemy.word:
                # stat checker stuff
                self.end_type_time = time()
                self.last_time = self.end_type_time - self.start_type_time

                self.num_words += 1
                self.userType = ""
                enemy.shot = True
                self.enemy_pos[enemy.list_position] = -1
        self.userType = ""
