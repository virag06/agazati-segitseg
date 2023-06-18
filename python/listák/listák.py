#listák

üresLista=[]    #üres lista
print(üresLista)

listaKezdőértékkel=[4,6,5,4,3,2]
print(listaKezdőértékkel)

gyümölcsLista=["alma","körte","barack","eper","dinnye"]
print(gyümölcsLista)

#egy elem elérése az index segítségével
#az indexelés 0-tól kezdődik, az utolsó elem indexe elemszám-1
print(gyümölcsLista[0])         #gyümölcslista első elemét írjuk ki
#print(gyümölcsLista[5])         #HIBA - IndexError: list index out of range (túlmutattunk a listán)

#teljes lista tartalmának kiírása
for item in listaKezdőértékkel:
    print(item,end=' ')

#teljes lista elemeinek kiírása (range)
print(f'\nA lsita {len(listaKezdőértékkel)} elemű.')  #a lista elemszámát adja meg
for i in range(0,len(listaKezdőértékkel)):
    print(listaKezdőértékkel[i],end=' ')

#új elem hozzáadása a listához
újGyümölcs=input('\nKérem adjon meg egy gyümölcsöt: ')
gyümölcsLista.append(újGyümölcs)        #új elem a lista végére

print(gyümölcsLista)