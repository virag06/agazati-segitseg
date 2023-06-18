#Listák kezelése

import random
lista=[]
elemszam=int(input('Hány elemű legyen a lista?: '))
for i in range(elemszam):
    lista.append(random.randint(0,100))
print(lista)
lista.sort()        #növekvő rendezés
print(f'Növekvő: {lista}')
lista.sort(reverse=True)        #csökkenő rendezés
print(f'Csökkenő: {lista}')

print(f'A listában {len(lista)} elem van')
print('A listában ' + str(len(lista)) +' elem van.')

print(f'A lista utolsó eleme: {lista[len(lista)-1]}')
print(f'A lista utolsó eleme: {lista[-1]}')

print(f'A lista első 5 eleme: {lista[0:5]}')
reszlista=lista[0:5]

print(f'A lista az első 3 és az utolső 3 elem nélkül: {lista[3:-3]}')
