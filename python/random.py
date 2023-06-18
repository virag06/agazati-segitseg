# Számok kíírása intervallumon, lépésközzel

i=1     #intervallum alsó határa (mettől)
while i<=100:        #i<=100 --> intervallum felső határa (meddig)
    print(i,end=' ')
    i+=1                #i növelése lépésközzel
    #------------------------------------------------------------------

    #Véletlen számok generálása (kockadobások)

    from random import randint  #random generáláshoz elengedhetetlen!

    print("\n\nKockadobások:")
    #addig dobálunk 2 db dobókockát, amíg mind a 2 nem lesz 6-os

    elso_dobas=randint(1,6) #generál egy egész számot 1-6-ig
    masodik_dobas=randint(1,6)

    #while elso_dobas+masodik_dobas!=12:     #!= --> nem egyenlő
    while elso_dobas!=6 or masodik_dobas!=6:
        print(f"{elso_dobas},{masodik_dobas}")
        elso_dobas=randint(1,6)
        masodik_dobas=randint(1,6)
    print("Mindkét kockával 6-ost dobtál, Vége.")