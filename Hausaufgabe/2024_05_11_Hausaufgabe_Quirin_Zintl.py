# Auf den 18.05.2024 als Hausaufgabe:

# Schreibe eine Funktion römisch_zu_dezimal(römische_zahl: str) -> int, die zu einer römischen Zahl die Darstellung als Dezimalzahl bestimmt und diese als Integer zurückgibt.

# TODO
römische_ziffern = ["I", "V", "X", "L", "C", "D", "M"]

def römisch_zu_dezimal(römiische_zahl: str) -> int:
    dezimal_zahl = 0
    last_index = 10000000000000000000000000

    for ziffer in list(römiische_zahl):
        index = römische_ziffern.index(ziffer)
        dezimal_wert = getdezimalValue(index)
        dezimal_zahl += dezimal_wert
        if index > last_index:
            dezimal_zahl -= getdezimalValue(last_index) * 2
        last_index = index
        
    return dezimal_zahl

def getdezimalValue(index:int) -> int:
    if not(index % 2):
        return_value = 10 ** (index / 2)
    else:
        return_value = 10 ** ((index - 1) / 2) * 5
    return return_value



#lösung
def römisch_zu_dezimal_lösung(römische_zahl):
    regeln = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ergebnis = 0

    for i in range(0, len(römische_zahl)):
        ziffer = römische_zahl[i]

        if(i < len(römische_zahl) - 1 and ziffer < regeln[römische_zahl[i + 1]]):
            ergebnis -= regeln[ziffer]
        else:
            ergebnis += regeln[ziffer]

    return ergebnis