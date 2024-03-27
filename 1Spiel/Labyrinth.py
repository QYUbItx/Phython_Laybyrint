#ganzes arcade window zeug
import arcade
arcade.open_window(800, 600, "Labyrinth")
arcade.set_background_color(arcade.color.AERO_BLUE)
block_liste = arcade.SpriteList() #das wird gedrawd



#listen der block koordinaten #TODO das ist quatsch, mit objekt ist besser
block_x_kor = []
block_y_kor = []



#ist dafür da, um Linien aus Blöcken zu machen
class Pointer:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def appendKor(x, y):
    block_x_kor.append(x)
    block_y_kor.append(y)

def blockLine(x, y, length, horizontal):
    pointer = Pointer(x, y)
    appendKor(pointer.x, pointer.y)
    length -= 1
    i = 0
    if horizontal:  
        while i < length:
            pointer.x += 50
            appendKor(pointer.x, pointer.y)
            i += 1
    else:
        while i < length:
            pointer.y += 50
            appendKor(pointer.x, pointer.y) 
            i += 1

#Linien der Ränder
blockLine(0, 0, 16, True)
blockLine(0, 550, 16, True)
blockLine(0, 0, 12, False)
blockLine(750, 0, 12, False)

#andere Linien
blockLine(100, 450, 4, True)
blockLine(100, 300, 3, False)
blockLine(350, 350, 3, False)
blockLine(200, 300, 5, True)
blockLine(400, 450, 2, True)
blockLine(550, 450, 2, False)
blockLine(500, 350, 3, True)
blockLine(650, 200, 6, False)
blockLine(500, 150, 6, True)
blockLine(400, 50, 5, False)
blockLine(150, 150, 5, True)
blockLine(100, 150, 2, False)

#einzelne Blöcke
appendKor(250, 400)
appendKor(300, 250)
appendKor(200, 200)
appendKor(200, 100)
appendKor(300, 50)
appendKor(550, 250)
appendKor(450, 250)
appendKor(500, 100)
appendKor(600, 50)
appendKor(100, 50)



#macht Sachen einfacher
def readebleBlockKor(int):
    return int + 25

for i, elements in enumerate(block_x_kor):
    block_x_kor[i] = readebleBlockKor(block_x_kor[i])
    block_y_kor[i] = readebleBlockKor(block_y_kor[i])



#macht objekte mit koordinaten in die blockliste
for i, elements in enumerate(block_x_kor):
    block = arcade.Sprite("texturen/block.png")
    block.center_x = block_x_kor[i]
    block.center_y = block_y_kor[i]
    block_liste.append(block)



#rendert und startet das Spiel
arcade.start_render()
block_liste.draw()
arcade.finish_render()
arcade.run()