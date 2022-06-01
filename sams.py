import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_NAME = "Test Arcade"

# open window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME)

# background color
arcade.set_background_color(arcade.color.BARBIE_PINK)

# start drawing
arcade.start_render()
arcade.finish_render()

# display
arcade.run()
