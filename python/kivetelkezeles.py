def terulet(a,b):
    ter=a*b
    if ter<100:
        raise ValueError('Hiba: Túl kicsi a telek!!!')
    return ter

print('2. feladat: Terület számítása')

while True:
    a=float(input('Kérem adja meg a telek szélességét (a):'))
    if a==-1:
        break
    b=float(input('Kérem adja meg a telek hosszúságát (b):'))
    if b==-1:
        break
    try:
        print(f'Telek területe: {terulet(a,b)} m2')
    except ValueError as error:
        print(error)



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