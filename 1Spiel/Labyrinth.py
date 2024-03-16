import arcade

arcade.open_window(800, 600, "Labyrinth")

arcade.set_background_color(arcade.color.AERO_BLUE)

block_liste = arcade.SpriteList()

block_x_koordinaten = [25, 75]
block_y_koordinaten = [25, 75]

for i in block_x_koordinaten:
    block = arcade.Sprite("texturen/block.png")
    print(i)
    block.center_x = block_x_koordinaten[0]
    block.center_y = block_y_koordinaten[0]
    block_liste.append(block)

arcade.start_render()
block_liste.draw()
arcade.finish_render()

arcade.run()