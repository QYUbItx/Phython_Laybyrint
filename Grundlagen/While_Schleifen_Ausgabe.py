## Aufgabe 1: Schreibe eine while-Schleife, die alle Zahlen zwischen 1 und 10 ausgibt.
i = 1
while i <= 10:
    print(i)
    i = i + 1

## Aufgabe 2: Schreibe eine while-Schleife, die alle Zahlen von 50 bis 75 ausgibt.
i2 = 50
while i2 <= 75:
    print(i2)
    i2= i2 + 1

## Aufgabe 3: Schreibe eine while-Schleife, die alle Zahlen von -15 bis 15 ausgibt.
i3 = -15
while i3 <= 15:
    print(i3)
    i3 = i3 + 1

## Aufgabe 4: Schreibe eine while-Schleife, die alle geraden Zahlen von 0 bis 40 ausgibt.
i3 = 0
while i3 <= 40:
    print(i3)
    i3 = i3 + 2

## Aufgabe 5: Schreibe eine while-Schleife, die alle durch 5 teilbaren Zahlen von 125 bis 250 ausgibt.
i4 = 125
while i4<= 250:
    if i4 % 5 == 0:
        print(i4)
    i4= i4 + 1

## Aufgabe 6: Schreibe eine while-Schleife, die alle durch 3 teilbaren Zahlen von -33 bis 0 ausgibt.
i5 = -33
while i5 <= 0:
    if i5 % 3 == 0:
        print(i5)
    i5= i5 + 1

## Aufgabe 7: Schreibe eine while-Schleife, die alle Zahlen von 10 bis 1 ausgibt.
i6 = 10
while i6 >= 1:
    print(i6)
    i6 = i6 - 1

## Aufgabe 8: Schreibe eine while-Schleife, die alle Zahlen von 87 bis 39 ausgibt.
i = 87
while i >= 39:
    print(i)
    i = i - 1

## Aufgabe 9: Schreibe eine while-Schleife, die alle geraden Zahlen von 80 bis 50 ausgibt.
i = 80
while i <= 50:
    if i % 2 == 0:
        print(i)
    i = i - 1

## Aufgabe 10: Schreibe eine while-Schleife, die alle durch 7 teilbaren Zahlen von 14 bis -63 ausgibt.
i = 14
while i >= -63:
    if i % 7 == 0:
        print(i)
    i = i - 1

print("Aufgabe 11")
## Aufgabe 11: Schreibe eine while-Schleife, die die Zahlen 1 2 4 8 16 32 64 128 256 512 1024 ausgibt.
i = 1
while i <= 1024:
    print(i)
    i = i + i

## Aufgabe 12: Schreibe eine while-Schleife, die 100 mal die Zahl 100 ausgibt.
i = 1
while i <= 100:
    print(100)
    i = i + 1

## Aufgabe 13: Schreibe eine while-Schleife, die die Zahlen 0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 ausgibt.
i = 0
while i <= 15:
    print(i * i)
    i = i + 1

print("aufgabe 14")
## Aufgabe 14: Schreibe eine while-Schleife, die die Zahlen 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 ausgibt.
i = 1
i2 = 0
i3 = 0
while i <= 987:
    print(i)
    i3 = i2
    i2 = i
    i = i + i3

## Aufgabe 15: Schreibe eine while-Schleife, die die Zahlen 225 196 169 144 121 100 81 64 49 36 25 16 9 4 1 0 1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 ausgibt.
i = -15
while i <= 15:
    print(i * i)
    i = i + 1

## Aufgabe 16: Schreibe eine while-Schleife, die alle Zahlen 225 224 221 216 209 200 189 176 161 144 125 104 81 56 29 0 ausgibt.
i = -15
while i <= 0:
    print(i * i)
    i = i + 1