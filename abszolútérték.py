# Abszolútérték meghatározása (manuális módszer)

def abszolutertek(number):      #a kapott paraméter abszolút értékét adja vissza
    if number<0:
        number=number*-1
    return number

print("Kérem adjon meg egy egész számot!")

szam=int(input("szám= "))

if szam<0:
    szam=szam*-1            #feltételes végrehajtás

print(f"A szám abszolút értéke: {abszolutertek(szam)}") #meghívjuk a függvényt a "szam" változóval

#bármennyiszer meghívhatjuk az abszolutertek függvényt!