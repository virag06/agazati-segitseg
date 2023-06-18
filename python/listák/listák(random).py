# Listák kezelése

import random

szamok=[]

def listaFeltolt(elemszam,alsoKuszob,felsoKuszob):
    for i in range(elemszam):
        szamok.append(random.randint(alsoKuszob,felsoKuszob))

def listaSorszamozottKiir():
    index=1
    for item in szamok:
        print(f'{index}.: {item}')
        index+=1

def listaSorszamozottKiir2():
    for i in range(0,len(szamok)):
        print(f'{i+1}.: {szamok[i]}')

def listaSorszamozottKiir3():
    for index,szam in enumerate(szamok):    #(0,lista[0];1,lista[1];...)
        print(f'{index+1}.: {szam}')

listaFeltolt(20,20,60)
listaSorszamozottKiir3()

sorszam=int(input('Hányadik számra kíváncsi?: '))
if sorszam<=len(szamok) and sorszam>0:
    print(f'A(z) {sorszam}. szám: {szamok[sorszam-1]}')
else:
    print('Nincs ilyen elem!')

torlendo=int(input('Hányadik elemet töröljük?: '))
#szamok.remove(szamok[torlendo-1])
szamok.pop(torlendo-1)
listaSorszamozottKiir3()