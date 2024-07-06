import arcade
import arcade.key
import random
import json


class Labyrinth(arcade.Window):

    #läd die daten aus einem level json file
    def load_level_data(self, level: int):
        file = open(f"level{level}.json")
        data = json.load(file)
        file.close()
        return data
    
    def level_up(self):
        self.level += 1
        self.clear()
        self.level_data = self.load_level_data(self.level)

    def load_level(self):
        #create board? how do you call it in english? #TODO
        self.blockLine(0, 0, 16, True)
        self.blockLine(0, 550, 16, True)
        self.blockLine(0, 0, 12, False)
        self.blockLine(750, 0, 12, False)

        spwans = []

        for i in range(self.board.__len__()):
            column = self.board[i]

            for j in range(column.__len__()):
                cell = column[j]

                if cell == 0:
                    continue
                elif cell == 1:
                    self.createSprite(j * 50, i * 50, "block", True)
                elif cell == 2:
                    self.createSprite(j * 50, i * 50, "fakeblock", False)
                elif cell == 3:
                    self.key = self.createSprite(j * 50, i * 50, "key", False)
                elif cell == 4:
                    self.lockblock = self.createSprite(j * 50, i * 50, "lockblock", True)
                elif cell == 5:
                    spwan = {
                        "x": j * 50,
                        "y": i * 50
                    }

                    spwans.append(spwan)
                elif cell == 6:
                    self.createEnemy(j * 50, i * 50, "enemy")


        #for item in self.level_data["blocks"]:
        #    self.createSprite(item["x"], item["y"], "block", True)
        #
        #for item in self.level_data["lines"]:
        #    self.blockLine(item["x"], item["y"], item["length"], item["horizontal"])
        #
        #for item in self.level_data["fakeblocks"]:
        #    self.createSprite(item["x"], item["y"], "fakeblock", False)
        #
        #for item in self.level_data["locks"]:
        #    self.lockblock = self.createSprite(item["x"], item["y"], "lockblock", True)
        #
        #for item in self.level_data["keys"]:
        #    self.key = self.createSprite(item["x"], item["y"], "key", False)

        #create entities
        
        spawn_pos = spwans[random.randint(0, spwans.__len__() - 1)]
        self.player = self.createSprite(spawn_pos["x"], spawn_pos["y"], "player", False, 0.75)

        #for item in self.level_data["enemys"]:
        #    self.enemy = self.createEnemy(item["x"], item["y"], "enemy")


    #funktionen um effectiver sprites zu erstellen
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
        sprite = arcade.Sprite(f"texturen/{texture}.png", size)
        sprite.center_x = x + 25
        sprite.center_y = y + 25
        if collisions:
            self.collision_list.append(sprite)
        self.sprite_list.append(sprite)
        return sprite

    
    def createEnemy(self, x, y, texture):
        enemy = self.createSprite(x, y, texture, False)
        self.enemy_list.append(enemy)
        return enemy
    

    def goTo(self, enemy:arcade.Sprite, x, y):
        dx = enemy.center_x - x
        dy = enemy.center_y - y
        enemy.change_x = dx
        enemy.change_y = dy


    def __init__(self):
        super().__init__(800, 600, "Labyrinth")
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        self.level = 1
        self.level_data = self.load_level_data(self.level)
    
        self.sprite_list = arcade.SpriteList() #das wird gedrawd
        self.collision_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.hasKey = False
        self.play_time = 0
        
        self.board = self.level_data["cells"]
        self.load_level()

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
        #update physics & entities
        self.physics.update()
        self.player.update()
        #self.enemy.update()

        #check for events
        if arcade.check_for_collision(self.player, self.key) and not self.hasKey:
            self.hasKey = True
            if self.key in self.sprite_list:
                self.sprite_list.remove(self.key)

        if self.player.center_x >= 550 and self.player.center_x <= 600 and self.player.center_y <= 150 and self.player.center_y >= 100 and self.hasKey:
            self.sprite_list.remove(self.lockblock)
            self.collision_list.remove(self.lockblock)
            self.hasKey = False

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.player, enemy):
                print("stop") #TODO end game

        #update time
        self.play_time += round(delta_time, 2)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
        splited_time = str(self.play_time).split(".")
        arcade.draw_text(splited_time[0] + "." + splited_time[1][0:2], 400, 10)



labyrinth = Labyrinth()
arcade.run()