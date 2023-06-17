import math

def prim(szam):                                     
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:       
            return False
    return True

also_hatar=0
while also_hatar<=0:
    also_hatar=int(input('Kérem adja meg az intervallum alsó határát: '))

felso_hatar=0
while felso_hatar<=also_hatar:
    felso_hatar=int(input('Kérem adja meg az intervallum felső határát: '))

    szam=also_hatar

while szam<=felso_hatar:
    if prim(szam) and szam!=1:
        print(szam,end=' ')
    szam+=1