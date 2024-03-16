## Beispiel 1: Schreibe eine Funktion namens eins, die die Zahl 1 zurückgibt.
## Rufe die Funktion anschließend auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def eins():
    return 1
ergebnis = eins()
print(ergebnis)

## Aufgabe 1: Schreibe eine Funktion namens würfel, die eine zufällige Zahl zwischen 1 und 6 zurückgibt.
## Rufe die Funktion anschließend auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
import random

def würfel():
    return random.randint(1, 6)
ergebnis = würfel()
print(ergebnis)

## Aufgabe 2: Schreibe eine Funktion namens doppeltes, die einen Parameter namens zahl besitzt und das Doppelte von zahl zurückgibt.
## Rufe die Funktion anschließend mit dem Argument 5 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def doppeltes(zahl):
    return zahl * 2
ergebnis = doppeltes(5)
print(ergebnis)

## Aufgabe 3: Schreibe eine Funktion namens summe, die zwei Parameter namens zahl1 und zahl2 besitzt und die Summe dieser Zahlen zurückgibt.
## Rufe die Funktion anschließend mit den Argumenten 12 und 8 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def summe(zahl1, zahl2):
    return zahl1 + zahl2
ergebnis = summe(12, 8)
print(ergebnis)

## Aufgabe 4: Schreibe eine Funktion namens positiv, die einen einzigen Parameter namens zahl besitzt und True zurückgibt, falls zahl positiv ist, ansonsten False.
## Rufe die Funktion anschließend mit dem Argument 100 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def positiv(zahl):
    if zahl > 0:
        return True
    else:
        return False
ergebnis = positiv(100)
print(ergebnis)

## Aufgabe 5: Schreibe eine Funktion namens größere, die zwei Parameter zahl1 und zahl2 besitzt und den maximalen Wert unter beiden Zahlen zurückgibt.
## Rufe die Funktion anschließend mit den Argumenten 3 und -3 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def positiv(zahl1, zahl2):
    if zahl1 > zahl2:
        return zahl1
    elif zahl2 > zahl1:
        return zahl2
ergebnis = positiv(3, -3)
print(ergebnis)

## Aufgabe 6: Schreibe eine Funktion namens quadrat, die einen einzigen Parameter zahl besitzt und dessen Quadrat zurückgibt.
## Rufe die Funktion anschließend mit dem Argument 5 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def doppeltes(zahl):
    return zahl ** 2
ergebnis = doppeltes(5)
print(ergebnis)

## Aufgabe 7: Schreibe eine Funktion namens hoch, die zwei Parameter zahl und exponent besitzt und den Wert von zahl hoch exponent zurückgibt (** steht für hoch).
## Rufe die Funktion anschließend mit den Argumenten 2 und 4 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def summe(zahl1, exponent):
    return zahl1 ** exponent
ergebnis = summe(2, 4)
print(ergebnis)

## Beispiel 2: Schreibe eine Funktion namens listenelement, die zwei Parameter liste und index besitzt und das Element an der Stelle index der Liste zurückgibt.
## Rufe die Funktion anschließend mit den Argumenten [3, 1, 5] und 0 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listenelement(liste, index):
    return liste[index]
ergebnis = listenelement([3, 1, 5], 0)
print(ergebnis)

## Aufgabe 8: Schreibe eine Funktion namens listenelement_positiv, die zwei Parameter liste und index besitzt und True zurückgibt, falls das Element an der Stelle index
## der Liste positiv ist, ansonsten False.
## Rufe die Funktion anschließend mit den Argumenten [3, 1, 5] und 1 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listenelement_positiv(liste, index):
    if liste[index] > 0:
        return True
    else:
        return False
ergebnis = listenelement_positiv([3, 1, 5], 1)
print(ergebnis)

## Aufgabe 9: Schreibe eine Funktion namens listenelemente_vergleich, die drei Parameter liste, index1 und index2 besitzt und True zurückgibt, falls das Element an der Stelle index1
## der Liste größer als das der Stelle index2 der Liste ist, ansonsten False.
## Rufe die Funktion anschließend mit den Argumenten [3, 1, 5], 1 und 0 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listenelemente_vergleich(liste, index1, index2):
    li1 = liste[index1]
    li2 = liste[index2]
    if li1 > li2:
        return li1
    else:
        return li2
ergebnis = listenelemente_vergleich([3, 1, 5], 1, 0)
print(ergebnis)

## Aufgabe 10: Schreibe eine Funktion namens listen_vergleich, die zwei Parameter liste1 und liste2 besitzt und True zurückgibt, falls das erste Element in liste1 größer ist als das erste Element
## in liste2, ansonsten False.
## Rufe die Funktion anschließend mit den Argumenten [4, 5, 6] und [7, -3, 0] auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listen_vergleich(liste1, liste2):
    li1 = liste1[0]
    li2 = liste2[0]
    if li1 > li2:
        return True
    else:
        return False
ergebnis = listen_vergleich([4, 5, 6], [7, -3, 0])
print(ergebnis)

## Aufgabe 11: Schreibe eine Funktion namens listen_vergleich_index, die drei Parameter liste1, liste2 und index besitzt und True zurückgibt, falls das Element in liste1 an der Stelle index größer ist
## als das Element an der Stelle index in liste2, ansonsten False.
## Rufe die Funktion anschließend mit den Argumenten [4, 5, 6], [7, -3, 0] und 1 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listen_vergleich_index(liste1, liste2, index):
    li1 = liste1[index]
    li2 = liste2[index]
    if li1 > li2:
        return True
    else:
        return False
ergebnis = listen_vergleich_index([4, 5, 6], [7, -3, 0])
print(ergebnis)

## Aufgabe 12: Schreibe eine Funktion namens listen_elemente_summe, die einen einzigen Parameter liste besitzt und die Summe der ersten drei Elemente dieser Liste zurückgibt.
## Rufe die Funktion anschließend mit dem Argument [10, 11, 12, 13, 14, 15] auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listen_elemente_summe(liste):
    return liste[0] + liste[1] + liste[2]
ergebnis = listen_elemente_summe([10, 11, 12, 13, 14, 15])
print(ergebnis)

## Aufgabe 13: Schreibe eine Funktion namens listen_elemente_summe_index, die drei Parameter liste, index1 und index2 besitzt und die Summe der Elemente an den Stellen index1 und index2 dieser Liste zurückgibt.
## Rufe die Funktion anschließend mit den Argumenten [10, 11, 12, 13, 14, 15], 1 und 4 auf, speichere das Ergebnis in einer Variable namens ergebnis und gib es aus.
def listen_elemente_summe_index(liste, index1, index2):
    return liste[index1] + liste[index2]
ergebnis = listen_elemente_summe_index([10, 11, 12, 13, 14, 15])
print(ergebnis)
