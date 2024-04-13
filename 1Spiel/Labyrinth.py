#ganzes arcade window zeug
import arcade




class Labyrinth(arcade.Window):

    #ist dafür da, um Linien aus Blöcken zu machen
    class Pointer:
        x = 0
        y = 0

        def __init__(self, x, y):
            self.x = x
            self.y = y

    def blockLine(self, x, y, length, horizontal):
        pointer = self.Pointer(x, y)
        self.createBlock(pointer.x, pointer.y, "block")
        length -= 1
        i = 0
        if horizontal:  
            while i < length:
                pointer.x += 50
                self.createBlock(pointer.x, pointer.y, "block")
                i += 1
        else:
            while i < length:
                pointer.y += 50
                self.createBlock(pointer.x, pointer.y, "block") 
                i += 1


    #macht Sachen einfacher
    def readebleBlockKor(self, int):
        return int + 25

    #erstellt einen block und appendet ihn zur block liste
    def createBlock(self, x, y, type):
        block = arcade.Sprite("texturen/" + type + ".png")
        block.center_x = self.readebleBlockKor(x)
        block.center_y = self.readebleBlockKor(y)
        self.block_liste.append(block)

    

    def __init__(self):
        super().__init__(800, 600, "Labyrinth")
        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.block_liste = arcade.SpriteList() #das wird gedrawd
        self.entity_liste = arcade.SpriteList()


        #Linien der Ränder
        self.blockLine(0, 0, 16, True)
        self.blockLine(0, 550, 16, True)
        self.blockLine(0, 0, 12, False)
        self.blockLine(750, 0, 12, False)

        #andere Linien
        self.blockLine(100, 450, 4, True)
        self.blockLine(100, 300, 3, False)
        self.blockLine(350, 350, 3, False)
        self.blockLine(200, 300, 5, True)
        self.blockLine(400, 450, 2, True)
        self.blockLine(550, 450, 2, False)
        self.blockLine(500, 350, 3, True)
        self.blockLine(650, 200, 6, False)
        self.blockLine(500, 150, 6, True)
        self.blockLine(400, 50, 5, False)
        self.blockLine(150, 150, 5, True)
        self.blockLine(100, 150, 2, False)

        #einzelne Blöcke
        self.createBlock(250, 400, "block")
        self.createBlock(300, 250, "block")
        self.createBlock(200, 200, "block")
        self.createBlock(200, 100, "block")
        self.createBlock(300, 50, "block")
        self.createBlock(550, 250, "block")
        self.createBlock(450, 250, "block")
        self.createBlock(500, 100, "block")
        self.createBlock(600, 50, "block")
        self.createBlock(100, 50, "block")


        player = arcade.Sprite("texturen/player.png")
        player.center_x = 325
        player.center_y = 225
        player.height = 50
        player.width = 50
        self.entity_liste.append(player)

    def on_key_press(self, char, modifiers):
        if char.w:
            print("w")
        


    def on_draw(self):
        self.clear()
        self.block_liste.draw()
        self.entity_liste.draw()




labyrinth = Labyrinth()
arcade.run()