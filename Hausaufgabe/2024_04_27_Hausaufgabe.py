# TODO
#
# Schreibe eine Funktion abstand(sprite1: arcade.Sprite, sprite2: arcade.Sprite) -> float, die den euklidischen Abstand zwischen den beiden Sprites sprite1 und sprite2 berechnet und zurückgibt.
# Lies im Internet (zum Beispiel auf Wikipedia) nach, was der euklidische Abstand ist.
#
# Hinweis: sprite1 und sprite2 besitzen Attribute center_x und center_y, die ihre x- und y-Positionen angeben.
# Auf diese kann über sprite1.center_x/sprite1.center_y/sprite2.center_x/sprite2.center_y zugegriffen werden.

import math

def abstand(sprite1, sprite2):
    d = math.sqrt((sprite1.center_x - sprite2.center_x) ** 2 + (sprite1.center_y - sprite2.center_y) ** 2)
    return d