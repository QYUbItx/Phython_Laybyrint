# Auf den 11.05.2024 als Hausaufgabe:


# Schreibe eine Funktion string_zu_liste(string: str) -> list, die einen String erhält und eine Liste zurückgibt, die die
# Buchstaben dieses Strings als einzelne Buchstaben enthält.
# Beispiel: string_zu_liste("abc123") == ["a", "b", "c", "1", "2", "3"]

# TODO
def string_zu_liste(string:str):
    return list(string)

# Schreibe eine Funktion quersumme(integer: int) -> int, die einen Integer erhält und die Quersumme dieses Integers zurückgibt.
# Beispiel: quersumme(417) == 12

# TODO
def quersumme(input:int):
    output:int = 0
    for item in input.__str__():
        output += int(item)
    return output