import arcade

arcade.open_window(800, 600, "Labyrinth")

arcade.set_background_color(arcade.color.AERO_BLUE)

block_liste = arcade.SpriteList()

block_x_koordinaten = [25]
block_y_koordinaten = [25]

for i in block_x_koordinaten:
    block_liste[i].center_x = block_x_koordinaten[i]
    block_liste[i].center_y = block_y_koordinaten[i]


    
block = arcade.Sprite("texturen/block.png")
block.center_x = 25
block.center_y = 25
block_liste.append(block)

arcade.start_render()
block_liste.draw()
arcade.finish_render()

arcade.run()