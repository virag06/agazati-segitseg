#Százalék számítás (hányan mennek át az alapvizsgán)

def atmentTanulokSzazaleka(osszesTanuloDb,bukottTanuloDb):
    szazalek=(1-bukottTanuloDb/osszesTanuloDb)*100
    return szazalek

osszes=-1   #kezdőérték, ami rossz, hogy mindenképpen kérjünk helyette jót a ciklusban
while osszes<1:     #ha a vizsgázók száma kisebb mint 1, akkor újrakérjük
    osszes=int(input("Összes tanuló száma: "))

bukott=-1
while bukott<0 or bukott>osszes:    #ha a bukott negatív vagy több, mint a vizsgázók száma, akkor újrakérjük
    bukott=int(input("Bukott tanulók száma: "))

print(f"A tanulók {atmentTanulokSzazaleka(osszes,bukott)} %-a ment át a vizsgán.")