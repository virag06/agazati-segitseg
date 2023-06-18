# faktoriális számítás

from re import I


print("Faktoriális")
n=int(input("n: "))     #5!=5*4*3*2*1
faktorialis=1
i=n
while i>0:
    faktorialis*=i
    i-=1
print(f"{n}!={faktorialis}")