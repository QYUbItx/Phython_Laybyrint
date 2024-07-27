import arcade
import arcade.color
import arcade.key
import random
import json
import arcade.key

colors = {
    "OLIVE": arcade.color.BLACK_OLIVE,
    "ICE": arcade.color.ICEBERG
}

class Labyrinth(arcade.Window):

    #läd die daten aus dem game_data file
    def load_game_data(self):
        file = open("game_data.json")
        data = json.load(file)
        file.close()
        return data
    
    def level_set_up(self):
        self.sprite_list = arcade.SpriteList()
        self.collision_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.hasKey = False

        self.key = 0
        self.lockblock = 0
        self.goal = {
            "x": 0,
            "y": 0
        }
        self.lock = {
            "x": 0,
            "y": 0
        }

        self.clear()
        self.level_data = self.game_data[self.level - 1]

        self.block_texture = self.level_data["block_texture"]
        arcade.set_background_color(colors[self.level_data["board_color"]])

        self.board = self.level_data["cells"]
        self.load_level()

    def load_level(self):
        spwans = []

        for i in range(self.board.__len__()):
            column = self.board[i]

            for j in range(column.__len__()):
                cell = column[j]

                if cell == 0:
                    continue

                x = j * 50
                y = (self.board.__len__() - 1 - i) * 50

                if cell == 1:
                    self.createSprite(x, y, self.block_texture, True)
                elif cell == 2:
                    self.createSprite(x, y, self.block_texture, False)
                elif cell == 3:
                    self.key = self.createSprite(x, y, "key", False)
                elif cell == 4:
                    self.lockblock = self.createSprite(x, y, "lockblock", True)
                elif cell == 5:
                    spwan = {
                        "x": x,
                        "y": y
                    }
                    spwans.append(spwan)
                elif cell == 6:
                    self.createEnemy(x, y, "enemy")
                elif cell == 7:
                    self.goal = {
                        "x": x,
                        "y": y
                    }
                elif cell == 8:
                    self.lock = {
                        "x": x,
                        "y": y
                    }
        
        
        spawn_pos = spwans[random.randint(0, len(spwans) - 1)]
        self.player = self.createSprite(spawn_pos["x"], spawn_pos["y"], "player", False, 0.75)

        self.physics = arcade.PhysicsEngineSimple(self.player, self.collision_list)


    #funktionen um effectiver sprites zu erstellen
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

        self.game_data = self.load_game_data()

        self.level = 1
        self.level_set_up()
        
        self.keys = {
            "w": False,
            "a": False,
            "s": False,
            "d": False
        }
        self.play_time = 0


    #hier vielleicht noch checken, ob komplimentärer key getrückt ist und dann entsprechede geschwidikeit auf 0 setzen 
    def on_key_press(self, char: int, modifiers: int):
        if char == arcade.key.W:
            self.keys["w"] = True
            self.player.change_y = 2.4
        if char == arcade.key.A:
            self.keys["a"] = True
            self.player.change_x = -2.4 
        if char == arcade.key.S:
            self.keys["s"] = True
            self.player.change_y = -2.4
        if char == arcade.key.D:
            self.keys["d"] = True
            self.player.change_x = 2.4

        if modifiers == arcade.key.MOD_ACCEL and char == arcade.key.R:
            self.keys = {
                "w": False,
                "a": False,
                "s": False,
                "d": False
            }
            self.play_time = 0

            self.level = 1
            self.level_set_up()
            
    def on_key_release(self, char: int, modifiers: int):
        if char == arcade.key.W:
            if self.keys["s"]:
                self.player.change_y = -2.4
            else:
                self.player.change_y = 0
            self.keys["w"] = False
        elif char == arcade.key.A:
            if self.keys["d"]:
                self.player.change_x = 2.4
            else:
                self.player.change_x = 0
            self.keys["a"] = False
        elif char == arcade.key.S:
            if self.keys["w"]:
                self.player.change_y = 2.4
            else:
                self.player.change_y = 0
            self.keys["s"] = False
        elif char == arcade.key.D:
            if self.keys["a"]:
                self.player.change_x = -2.4
            else:
                self.player.change_x = 0
            self.keys["d"] = False
            
        
    def on_update(self, delta_time):
        if self.level == 0:
            return

        #update physics & entities
        self.physics.update()
        self.player.update()
        for enemy in self.enemy_list:
            enemy.update()

        #check for events
        if self.key and not self.hasKey and arcade.check_for_collision(self.player, self.key):
            self.hasKey = True
            if self.key in self.sprite_list:
                self.sprite_list.remove(self.key)

        if self.lockblock and self.player.center_x >= self.lock["x"] and self.player.center_x >= self.lock["y"] and self.player.center_y <= self.lock["x"] + 50 and self.player.center_y <= self.lock["y"] + 50 and self.hasKey:
            self.sprite_list.remove(self.lockblock)
            self.collision_list.remove(self.lockblock)
            self.hasKey = False

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.player, enemy):
                self.level = 0

        if self.player.center_x >= self.goal["x"] and self.player.center_x >= self.goal["y"] and self.player.center_y <= self.goal["x"] + 50 and self.player.center_y <= self.goal["y"] + 50:
            self.level += 1
            self.level_set_up()

        #update time
        self.play_time += round(delta_time, 2)
        

    def on_draw(self):
        if self.level == 0:
            arcade.draw_text("GAME OVER", 400, 300, font_size= 10)
            return

        self.clear()
        self.sprite_list.draw()

        if self.play_time > 1:
            splited_time = str(self.play_time).split(".")
            arcade.draw_text(splited_time[0] + "." + splited_time[1][0:2], 400, 10)
        else:
            arcade.draw_text("0", 400, 10)



labyrinth = Labyrinth()
arcade.run()