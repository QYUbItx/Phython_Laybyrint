# Auf den 08.06.2024 als Hausaufgabe:

# Schreibe eine Funktion römische_zahl(string: str) -> str, die True zurückgibt, falls string eine gültige Darstellung einer römischen Zahl ist, ansonsten False.

# TODO

ziffern = ["I", "V", "X", "L", "C", "D", "M"]

def römische_zahl(string: str) -> bool:
    char = ""
    highest_index = 0
    repitition_count = 0
    subtraction_count = 0

    #geht alle möglichen bedingungen durch und gibt false zurück, falls eine bedingung nicht erfüllt wurde
    if not string.__len__():
        return False
    
    for item in list(reversed(string)):
        last_char = char
        char = item
        digit_index = ziffern.index(char)

        #testet ob char römische ziffer ist
        if not ziffern.count(char):
            return False
        
        #testet ob sich eine ziffer zu oft wiederholt
        if char == last_char:
            repitition_count += 1
            if (not (digit_index % 2) and repitition_count == 3) or ((digit_index % 2) and repitition_count == 1):
                return False
        else:
            repitition_count = 0

        #testet ob die nächste ziffer (rechts nach links) kleiner ist und entsprechende regeln
        if digit_index > highest_index:
            highest_index = digit_index
            subtraction_count = 0
        elif digit_index < highest_index:
            subtraction_count += 1
            if (not (digit_index % 2) and subtraction_count == 2) or ((digit_index % 2) and subtraction_count == 1):
                return False
            elif digit_index + 2 < highest_index:
                return False
                
    #gibt true zurück, wenn alle bedingungen erfüllt wurden
    return True

#print(römische_zahl("CMXCIX"))