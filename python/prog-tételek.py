#Programozási tételek

import random

szamok=[]

def feltolt():
    for i in range(15):
        szamok.append(random.randint(0,100))

def kiir():
    for item in szamok:
        print(f'{item} ',end='')

#------------------------------------------------------------------------------------
#Összegzés: mennyi a listában lévő számok összege
def osszegzes():
    osszeg=0
    for item in szamok:
        osszeg+=item
    return osszeg

#Megszámlálás: pl. páratlan elemek megszámolása (a feltétel bármi lehet)
def paratlan_db():
    darab=0
    for item in szamok:
        if item % 2 ==1:
            darab+=1
    return darab
def paros_db():
    return len(szamok)-paratlan_db()    #metódus is hívhat metódust!

#Szélsőérték (maximum) kiválasztása

def legnagyobb():
    max=szamok[0]
    maxIndex=0
    for i in range(1,len(szamok)):
        if szamok[i]>max:
            max=szamok[i]
            maxIndex=i
    return maxIndex

def legnagyobb2():
    maxIndex=0
    for i in range(1,len(szamok)):
        if szamok[i]>szamok[maxIndex]:
            maxIndex=i
    return maxIndex

def legnagyobb3():
    maxIndex=0
    for index,ertek in enumerate(szamok):
        if ertek>[maxIndex]:
            maxIndex=index
    return maxIndex

#Szélsőérték (minimum) kiválasztása

def legkisebb():
    minIndex=0
    for i in range(1,len(szamok)):
        if szamok[i]<szamok[minIndex]:
            minIndex=i
    return minIndex
#------------------------------------------------------------------------------------
feltolt()
kiir()
print(f'\nA számok összege: {osszegzes()}')
print(f'A számok átlaga: {osszegzes()/len(szamok)}')
print(f'A páratlan számok darabszáma: {paratlan_db()}')
print(f'A páros számok darabszáma: {paros_db()}')
print(f'A legnyagyonn elem sorszáma: {legnagyobb()+1}. Értéke: {szamok[legnagyobb()]}')
print(f'A legnyagyonn elem sorszáma: {legnagyobb2()+1}. Értéke: {szamok[legnagyobb2()]}')
print(f'A legkisebb elem sorszáma: {legkisebb()+1}. Értéke: {szamok[legkisebb()]}')