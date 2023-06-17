# Ellenőrzött bekérés

szam=0          #kezdőértéknek egy nem jó értéket kell megadni, hogy a ciklusban helyette újat kérjünk
while szam<1 or szam>100:   #ismétli amíg a szám kisebb 1 vagy nagyobb 100
    szam=int(input("Kérek egy számot 1 és 100 között: "))

print("Köszönöm.")