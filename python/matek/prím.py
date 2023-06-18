#Prímszám-e a bekért szám

import math

def prim(szam):                                     #a kapott szám prím-e vagy nem
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:       #== vizsgálati egyenlőségjel!
            return False
    return True

print("Prímszám vizsgálat")
szam=int(input("\nKérek egy számot: "))

if prim(szam):   #True értékkel tért vissza
    print("A megadott szám prím.")
else:            #False értékkel tért vissza
    print("A megadott szám NEM prím.")