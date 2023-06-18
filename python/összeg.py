print("1. feladat: Számok összege")
aSzam=int(input('Kérem "a" értékét: '))
bSzam=int(input('Kérem "b" értékét: '))

sum=0
while aSzam>=bSzam:
    aSzam=int(input('Kérem "a" értékét: '))
    bSzam=int(input('Kérem "b" értékét: '))
else:
    aSzam1 = aSzam
    while aSzam1!=bSzam+1:
        sum+=aSzam1
        aSzam1+=1

print(f'A(z) [{aSzam},{bSzam}] zárt intervallumban a számok összege: {sum}')


import math

def Machszam(qc:float,p:float):
    m:float= math.sqrt(math.sqrt(qc/p)*5)
    if m>=1:
        raise ValueError('Hiba:nem szubszonikus sebesség!')
    return m

while True:
    qc=float(input('Kérem a torlónyomás értékét (qc): '))
    if qc == -1:
        break
    p0=float(input('Kérem a statikus nyomás értékét (p0): '))   
    if p0 == -1:
        break
    try:
        m = Machszam(qc,p0)
        print(m)
    except ValueError as error:
        print(error) 