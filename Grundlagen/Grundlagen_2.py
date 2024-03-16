## Beispiel 1: So erstellt man eine Variable zufallszahl1, die eine zufällige Zahl zwischen 1 und 10 enthält.
import random # Muss nur einmal pro Datei geschrieben werden
zufallszahl1 = random.randint(1, 10)

## Aufgabe 1: Gib die Variable zufallszahl1 aus.
print(zufallszahl1)

## Aufgabe 2: Erstelle eine Variable zufallszahl2, die eine zufällige Zahl zwischen 1 und 100 enthält.
zufallszahl2 = random.randint(1, 100)

## Aufgabe 3: Gib die Variable zufallszahl2 aus.
print(zufallszahl2)

## Aufgabe 4: Erstelle eine Variable zufallszahl3, die eine zufällige Zahl zwischen -25 und 25 enthält.
zufallszahl3 = random.randint(-25, 25)


## Aufgabe 5: Gib die Variable zufallszahl3 aus.
print(zufallszahl3)

## Aufgabe 6: Addiere die Variable zufallszahl1 mit der Variable zufallszahl2 und speichere das Ergebnis in einer Variable ergebnis1.
ergebnis1 = zufallszahl2 + zufallszahl1

## Aufgabe 7: Addiere die Variable ergebnis1 mit der Zahl 20 und speichere da Ergebnis in einer Variable ergebnis2.
ergebnis2 = ergebnis1 + 20

## Aufgabe 8: Erstelle eine Variable zufallszahl4, die eine zufällige Zahl zwischen 1 und zufallszahl2 enthält.
zufallszahl4 = random.randint(1, zufallszahl2)

## Aufgabe 9: Erstelle eine Variable zufallszahl5, die eine zufällige Zahl zwischen zufallszahl4 und 250 enthält.
zufallszahl5 = random.randint(zufallszahl4, 250)

## Aufgabe 10: Gib die Variable zufallszahl5 aus.
print(zufallszahl5)

## Aufgabe 11: Erstelle eine Variable zufallszahl6, die eine zufällige Zahl zwischen ergebnis1 und ergebnis2 enthält.
zufallszahl6 = random.randint(ergebnis1, ergebnis2)

## Aufgabe 12: Gib die Variable zufallszahl6 aus.
print(zufallszahl6)

## Beispiel 2: So prüft man, ob die Variable zufallszahl1 den Wert 10 besitzt. Falls ja, wird "10" ausgegeben.
if zufallszahl1 == 10:
    print("10")

## Aufgabe 13: Falls die Variable zufallszahl2 den Wert 50 enthält, gib "50" aus.
if zufallszahl2 == 50:
    print(50)

## Aufgabe 14: Falls die Variable zufallszahl3 den Wert 0 enthält, gib "0" aus.
if zufallszahl3 == 0:
    print(zufallszahl3)

## Aufgabe 15: Falls die Variable zufallszahl6 den Wert 100 enthält, gib "100" aus.
if zufallszahl6 == 100:
    print(zufallszahl6)

## Aufgabe 16: Falls die Summe aus zufallszahl2 und zufallszahl3 den Wert 75 enthält, gib "75" aus.
if zufallszahl2 + zufallszahl3 == 75:
    print(75)

## Beispiel 3: So prüft man, ob die Variable zufallszahl1 einen Wert ungleich 5 besitzt. Falls ja, wird "Ungleich 5" ausgegeben.
if zufallszahl1 != 5:
    print("Ungleich 5")

## Aufgabe 17: Falls die Variable zufallszahl4 einen Wert ungleich 50 besitzt, gib "Ungleich 50" aus.
if zufallszahl3 != 50:
    print("Ungleich 50")

## Aufgabe 18: Falls die Variable zufallszahl5 einen Wert ungleich 200 besitzt, gib "Ungleich 200" aus.
if zufallszahl5 != 200:
    print("Ungleich 200")

## Aufgabe 19: Falls die Variable zufallszahl3 einen Wert ungleich 0 besitzt, gib "Ungleich 0" aus.
if zufallszahl3 != 0:
    print("Ungleich 0")

## Aufgabe 20: Falls die Differenz aus zufallszahl5 und zufallszahl4 einen Wert ungleich 100 besitzt, gib "Ungleich 100" aus.
if zufallszahl5 / zufallszahl6 != 100:
    print("Ungleich100")

## Beispiel 4: So prüft man, ob die Variable zufallszahl1 einen Wert kleiner 8 besitzt. Falls ja, wird "Kleiner 8" ausgegeben.
if zufallszahl1 < 8:
    print("Kleiner 8")

## Aufgabe 21: Falls die Variable zufallszahl2 einen Wert kleiner 33 besitzt, gib "Kleiner 33" aus.
if zufallszahl2 < 33:
    print("Kleiner 33")

## Aufgabe 22: Falls die Variable zufallszahl3 einen Wert kleiner 0 besitzt, gib "Kleiner 0" aus.
if zufallszahl3 < 0:
    print("Kleiner 0")

## Aufgabe 23: Falls die Variable zufallszahl4 einen Wert kleiner 77 besitzt, gib "Kleiner 77" aus.
if zufallszahl4 < 77:
    print("Kleiner 77")

## Aufgabe 24: Falls das Produkt von zufallszahl1 und zufallszahl2 kleiner dem Produkt von zufallszahl3 und zufallszahl4 ist, gib "Kleiner Produkt" aus.
if zufallszahl1 * zufallszahl2 < zufallszahl3 * zufallszahl4:
    print("Kleiner Produkt")

## Beispiel 5: So prüft man, ob die Variable zufallszahl1 einen Wert kleiner oder gleich 5 besitzt. Falls ja, wird "Kleiner-gleich 5" ausgegeben.
if zufallszahl1 <= 5:
    print("Kleiner-gleich 5")

## Aufgabe 25: Falls die Variable zufallszahl3 kleiner oder gleich -10 ist, gib "Kleiner-gleich -10" aus.
if zufallszahl3 <= -10:
    print("Kleiner-gleich -10")

## Aufgabe 26: Falls die Variable zufallszahl2 kleiner oder gleich 50 ist, gib "Kleiner-gleich 50" aus.
if zufallszahl2 <= -50:
    print("Kleiner-gleich 50")

## Aufgabe 27: Falls die Summe aus zufallszahl1 und zufallszahl3 kleiner oder gleich 0 ist, gib "Kleiner-gleich 0" aus.
if zufallszahl1 + zufallszahl3 <= 0:
    print("Kleiner-gleich 0")

## Beispiel 6: So prüft man, ob die Variable zufallszahl1 einen Wert größer 8 besitzt. Falls ja, wird "Größer 8" ausgegeben.
if zufallszahl1 > 8:
    print("Größer 8")

## Aufgabe 28: Falls die Variable zufallszahl4 größer 80 ist, gib "Größer 80" aus.
if zufallszahl4 > 80:
    print("Größer 80")

## Aufgabe 29: Falls die Variable zufallszahl2 größer 15 ist, gib "Größer 15" aus.
if zufallszahl2 > 15:
    print("Größer 15")

## Aufgabe 30: Falls die Variable zufallszahl3 größer 1 ist, gib "Größer 1" aus.
if zufallszahl3 > 1:
    print("Größer 1")

## Aufgabe 31: Falls das Produkt von zufallszahl1 und zufallszahl2 größer 500 ist, gib "Größer 500" aus.
if zufallszahl1 * zufallszahl2 > 500:
    print("Größer 500")

## Beispiel 7: So prüft man, ob die Variable zufallszahl1 größer oder gleich 3 ist. Falls ja, wird "Größer-gleich 3" ausgegeben.
if zufallszahl1 >= 3:
    print("Größer-gleich 3")

## Aufgabe 32: Falls die Variable zufallszahl2 größer oder gleich 33 ist, gib "Größer-gleich 33" aus.
if zufallszahl2 >= 33:
    print("Größer-gleich 33")

## Aufgabe 33: Falls die Variable zufallszahl4 größer oder gleich 77 ist, gib "Größer-gleich 77" aus.
if zufallszahl4 >= 77:
    print("Größer-gleich 77")

## Aufgabe 34: Falls die Variable zufallszahl3 größer oder gleich 9 ist, gib "Größer-gleich 9" aus.
if zufallszahl3 >= 9:
    print("Größer-gleich 9")

## Aufgabe 35: Falls die Differenz aus zufallszahl1 und zufallszahl2 größer oder gleich der Summe aus zufallszahl3 und zufallszahl4 ist, gib "Größer-gleich Summe" aus.
if zufallszahl1 - zufallszahl2 >= zufallszahl3 + zufallszahl4:
    print("Größer-gleich Summe")