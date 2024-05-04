#ganzes arcade window zeug
import arcade
import arcade.key




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
        self.createSprite(pointer.x, pointer.y, "block", True)
        length -= 1
        i = 0
        if horizontal:  
            while i < length:
                pointer.x += 50
                self.createSprite(pointer.x, pointer.y, "block", True)
                i += 1
        else:
            while i < length:
                pointer.y += 50
                self.createSprite(pointer.x, pointer.y, "block", True)
                i += 1


    def createSprite(self, x, y, texture, collisions, size = 1):
        sprite = arcade.Sprite("texturen/" + texture + ".png", size)
        sprite.center_x = x
        sprite.center_y = y
        if collisions:
            self.collision_list.append(sprite)
        self.sprite_list.append(sprite)



    #macht Sachen einfacher
    def readebleBlockKor(self, int):
        return int + 25
    


    def __init__(self):
        super().__init__(800, 600, "Labyrinth")
        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.sprite_list = arcade.SpriteList() #das wird gedrawd
        self.collision_list = arcade.SpriteList()
        self.hasThePlayerTheKeyQuestionMark = False
        

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
        self.blockLine(500, 150, 4, True)
        self.blockLine(400, 100, 5, False)
        self.blockLine(150, 150, 5, True)
        self.blockLine(100, 150, 2, False)

        #einzelne Blöcke
        self.createSprite(250, 400, "block", True)
        self.createSprite(300, 250, "block", True)
        self.createSprite(200, 200, "block", True)
        self.createSprite(200, 100, "block", True)
        self.createSprite(300, 50, "block", True)
        self.createSprite(550, 250, "block", True)
        self.createSprite(450, 250, "block", True)
        self.createSprite(500, 100, "block", True)
        self.createSprite(600, 50, "block", True)
        self.createSprite(100, 50, "block", True)

        #andere Blöcke
        self.createSprite(400, 50, "fakeblock", False)
        self.createSprite(700, 150, "fakeblock", False)
        self.createSprite(600, 100, "lockblock", True)

        #enemys

        #andere Sprites
        self.key = self.createSprite(350, 50, "key", False)

        #player init
        self.player = self.createSprite(325, 225, "player", False, 0.75)

        print(isinstance(self.player, arcade.Sprite))

        #pysics engine
        self.physics = arcade.PhysicsEngineSimple(self.player, self.collision_list)


    
    def on_key_press(self, char: int, modifiers: int):
        if char == arcade.key.W:
            self.player.change_y = 2.4
        elif char == arcade.key.A:
            self.player.change_x = -2.4
        elif char == arcade.key.S:
            self.player.change_y = -2.4
        elif char == arcade.key.D:
            self.player.change_x = 2.4
            
    #20.4. hier das release-check-ding machen. #27.4. was meinst du?!
    def on_key_release(self, char: int, modifiers: int):
        if char == arcade.key.W:
            self.player.change_y = 0
            #self.on_key_press()
        elif char == arcade.key.A:
            self.player.change_x = 0
            #self.on_key_press()
        elif char == arcade.key.S:
            self.player.change_y = 0
            #self.on_key_press()
        elif char == arcade.key.D:
            self.player.change_x = 0
            #self.on_key_press()
            
        
    def on_update(self, delta_time):
        self.physics.update()
        self.player.update()
        if arcade.check_for_collision(self.player, self.key):
            self.hasThePlayerTheKeyQuestionMark = True
            self.sprite_list.pop(-2)
            print("a")
        if self.player.center_x >= 550 and self.player.center_x <= 600 and self.player.center_y <= 150 and self.player.center_y >= 100 and self.hasThePlayerTheKeyQuestionMark:
            self.block_liste.pop(-1)
            self.hasThePlayerTheKeyQuestionMark = False
            print("b")

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()




labyrinth = Labyrinth()
arcade.run()