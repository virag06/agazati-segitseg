# Egysoros komment

"""
Ez
egy
több soros komment
"""
print("helló")
print('Ez "egy" szöveg')
print("Ez \"egy\" szöveg")


szam=2,6
print(szam)
print(type(szam))

a=2
b=3
c=a+b
print(a+b)
print(c)

print("c="+str(c)) #"c" változót karakterlánccá kell konvertálni az összefügg
print(f"c változó értéke = {c}")
print("c értéke=" ,c) #felsoroljuk a kiírandó részeket
print(a,'+',b,'=',c) #a+b=c --> 2 + 3 = 5
print(a,'+',b,'=',c,sep='') #a+b=c --> 2+3=5
print(a,'+',b,'=',c,sep='&',end='') #mivel az end='' azaz a semmi, így sirt sem emel!!
print("szöveg")

#--------------------------------------------------------------------------------------
#változónevekkel kapcsolatos szabályok:

#1péter - nem kezdődhet számmal!
#péter neve - nem lehet benne szóköz!
#peter'sname - nem lehet benne speciális karakter, csak a-z vagy A-Z vagy 0-9 vagy _
#péter1=12 - EZ JÓ!
#péter_neve="Péter" - EZ IS JÓ!
#pÉtEr_21neve="Péter" - EZ IS JÓ!

#case sensitive - nagy és kis betűk különbözőek!
#A nem egyenlő a-val
#Alma nem egyenlő alma

#--------------------------------------------------------------------------------------
#Mire figyeljünk (hogy ne kapjunk instant 1-est)

#olyan változóneveket válasszunk, ami utal annak tartalmára!

#asd - TILOS! 
a=10
b=34
c=321              #ha pl. háromszög oldalai, akkor elmegy, de lehetne aoldal/b_oldal/c_Oldal
d="körte"
e=True

#példa jó változónevekre:

#Autó adatait szeretnénk tárolni (típus, tulajdonos, stb)
autó_típus="Audi"      #snake case
autó_tulajdonos="Gipsz Jakab"

autóTípus="Opel"       #camel case
AutóTípus="BMW"        #Pascal case

#----------------------------------------------------------------------------------------
print("3. feladat")
print("\tKérem adjon meg egy számot!") #\t kapcsoló --> 1 db tabulátor
print("\n\n\t\tSzám=")                 #\n kapcsoló --> 1 db soremelés (mintha entert ütnénk)