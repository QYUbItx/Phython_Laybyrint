#ganzes arcade window zeug
import arcade
arcade.open_window(800, 600, "Labyrinth")
arcade.set_background_color(arcade.color.AERO_BLUE)
block_liste = arcade.SpriteList() #das wird gedrawd



#listen der block koordinaten
block_x_koordinaten = []
block_y_koordinaten = []

def popKor(x, y):
    block_x_koordinaten.pop(x)
    block_y_koordinaten.pop(y)

def blockLine(start, end, xOrY, secVal):
    pointer = 0
    if xOrY == "x":  
        pointer.x = start
        pointer.y = secVal
        popKor(pointer.x, pointer.y)
        while pointer.x != end:
            true = true






#macht Sachen einfacher
def readebleBlockKor(int):
    return int + 25

for i, elements in enumerate(block_x_koordinaten):
    block_x_koordinaten[i] = readebleBlockKor(block_x_koordinaten[i])
    block_y_koordinaten[i] = readebleBlockKor(block_y_koordinaten[i])



#macht objekte mit koordinaten in liste
for i, elements in enumerate(block_x_koordinaten):
    block = arcade.Sprite("texturen/block.png")
    block.center_x = block_x_koordinaten[i]
    block.center_y = block_y_koordinaten[i]
    block_liste.append(block)



#rendert und startet 
arcade.start_render()
block_liste.draw()
arcade.finish_render()
arcade.run()