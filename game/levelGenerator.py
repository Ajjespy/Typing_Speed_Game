from arcade import start_render, View, SpriteList, load_texture, draw_text, draw_rectangle_filled, draw_lrwh_rectangle_textured, key, color
import game.controller as controller
from game.constants import RESOURCE_PATH, MUSIC_HANDLER, MUSIC_DICT
from game.stattracker import StatTracker
from game.random_word import RandomWord
from time import time
from random import randint
from game.enemy import Enemy

class LevelGenerator(View):
    def __init__(self):
        super().__init__()
        self.background = None
        self.buttons = False
        self.enemy_list = SpriteList()
        self.enemy_names_list = ["Friendly Tim", "Knife Goose", "Knife Lady", "Rangoon", "Shady Jim", "Unfriendly Tim"]
        
    def setup(self):
        """
        Runs before the view is changed used for resetting the view without deleting the object
        """
        self.background = load_texture(f"{RESOURCE_PATH}backgrounds/ShootZone.png")
            
        self.userType = ""
        self.last_time = 0
        self.num_words = 0
        self.start_type_time = None
        self.end_type_time = None
        self.has_started = False
        self.stattracker = StatTracker()

        self.enemy_pos = [-1, -1, -1]

        # add first enemy
        if self.num_words == 0:
            self.add_enemy(self.enemy_names_list[0], .75, RandomWord.get_word(randint(1, 4)), 0)

        MUSIC_HANDLER.play_song(MUSIC_DICT["main_theme"], .5)  # add music here


    def on_draw(self):
        super().on_draw()
        start_render()
        # background gets drawn first
        draw_lrwh_rectangle_textured(0, 0, self.window.width, self.window.height, self.background)

        draw_text(self.userType, self.window.width / 2 - 44 * 5.5, 125, color.BLUE, 44, 400, "left", font_name="Ultra")
        draw_text(f"Sec: {int(self.last_time)}", self.window.width - 400, self.window.height - 48, color.GREEN, 44, 500, "center", "Ultra")  
        draw_text(f"Words: {self.num_words}", self.window.width - 450, self.window.height - 100, color.GREEN, 44, 500, "center", "Ultra")

        for enemy in self.enemy_list:
            enemy.draw()
            draw_text(enemy.word, enemy.center_x - 85, enemy.center_y + (enemy.height / 2), color.BLUE, 28, 400, "left", font_name="Ultra")
            if enemy.start != None:
                # Draws a timer so that the user knows which enemy is running out of time fastest
                draw_rectangle_filled(enemy.center_x, enemy.center_y - (enemy.height / 2), width = enemy.width / 2, height = 10, color = color.RED)
                draw_rectangle_filled(enemy.center_x, enemy.center_y - (enemy.height / 2), width = (enemy.width / 2) * (enemy.start/10), height = 10, color = color.GREEN)


    def on_update(self, delta_time: float):
        super().on_update(delta_time)
        # checks if the user has typed in the correct word
        self.enemy_list.update()

        for enemy in self.enemy_list:
            # if an enemy runs out of time then go to score screen
            if enemy.end <= time():
                self.stattracker.set_end()
                controller.on_change_view(self, 3, stat_tracker = self.stattracker)

        # stat checker stuff will be gone when stattracker is finished
        if not (self.start_type_time == None or self.end_type_time == None):
            self.end_type_time = None
            self.start_type_time = None
        
        # add more ememies based on number of words user has typed
        if not len(self.enemy_list) >= 3:
            pos = randint(0,2)
            while self.enemy_pos[pos] > 0:
                pos = randint(0,2)
            self.add_enemy(self.enemy_names_list[randint(0, len(self.enemy_names_list) - 1)], .75, RandomWord.get_word(randint(1, 4)), pos)

    def on_key_press(self, symbol: int, modifiers: int):
        controller.get_key_press(self, symbol)
        if symbol > 96 and symbol < 123:
            if not self.has_started:
                self.has_started = True
                self.stattracker.set_start()
            # basic stat checker will be finished in stat checker file
            if self.end_type_time == None and self.start_type_time == None:
                self.start_type_time = time()
            
            # checks for upper case chars
            if modifiers % 2 == 1:
                self.userType = self.userType + chr(symbol).upper()
            else:
                self.userType = self.userType + chr(symbol)
        if symbol == key.BACKSPACE:
            self.userType = self.userType[:-1]

        if symbol == key.ENTER:
            self.on_enter()
            
            
    def on_key_release(self, symbol: int, modifiers: int):
        # lets controller know that a key has become unpressed
        controller.get_key_press(self, symbol, True)

    def add_enemy(self, enemy_name, size, word, pos_index):
        """
        Adds enemies to the screen
        """
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
        """
        When the user enters a word something happens
        """
        for enemy in self.enemy_list:
            if len(self.userType) > len(enemy.word) - 1 and self.userType == enemy.word:
                # stat checker stuff
                self.end_type_time = time()
                self.last_time = self.end_type_time - self.start_type_time

                self.stattracker.add_word(enemy.word)
                self.stattracker.add_user_word(self.userType)

                self.num_words += 1
                self.userType = ""
                enemy.shot = True
                self.enemy_pos[enemy.list_position] = -1
        self.userType = ""
