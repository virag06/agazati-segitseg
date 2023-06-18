class Repulo:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.Tipus=adatok[0]
        self.Ev=int(adatok[1])
        self.Utas=adatok[2]
        self.Szemelyzet=adatok[3]
        self.Utazósebesség=int(adatok[4])
        self.Felszallotomeg=int(adatok[5])
        self.Fesztav=float(adatok[6].replace(",","."))

repulok:list[Repulo]=[]

f=open('utasszallitok.txt','r',encoding='utf-8')
f.readline()
for sor in f:
    repulok.append(Repulo(sor))
f.close

print(f'3.3 feladat: Repülők száma: {len(repulok)}')

ossz=0
for i in repulok:
    ossz+=i.Utazósebesség
print(f'3.4 feladat: Az átlagsebesség: {(ossz/len(repulok)):.2f} km/h')

maxFeszt=repulok[0]
for i in repulok:
    if i.Fesztav>maxFeszt.Fesztav:
        maxFeszt=i
print('3.5 feladat: A legnagyobb fesztávú repülő adatai')
print(f'\tTípus: {maxFeszt.Tipus}')
print(f'\tÉv: {maxFeszt.Ev}')
print(f'\tUtazó sebesség: {maxFeszt.Utazósebesség}')
print(f'\tFelszállótömeg: {maxFeszt.Felszallotomeg}')
print(f'\tFesztáv: {maxFeszt.Fesztav}')

stat={}
print("3.6 feladat: Statisztika")
for i in repulok:
    j=str(i.Ev//10)+"0s"
    if j in stat:
        stat[j]+=1
    else:
        stat[j]=1
for i in stat:
    print(f"\t{i} -> {stat[i]} db")