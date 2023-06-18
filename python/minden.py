class Valami:
    def __init__(self,sor:str):
        adatok=sor.strip().split(';')
        self.Nev=adatok[0]
        self.Szam=int(adatok[1])

valamik:list[Valami]=[]

f=open('__.txt','r',encoding='utf-8')
f.readline()
for sor in f:
    valamik.append(Valami(sor))
f.close

