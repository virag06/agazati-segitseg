# Fibonacci számsor első 40 eleme

elozo_elotti=0  #n-2. elem
elozo=1         #n-1. elem

print(elozo_elotti,end=' ')
print(elozo,end=' ')

for i in range(2,40):
    osszeg=elozo_elotti+elozo
    print(osszeg,end=' ')
    elozo_elotti=elozo
    elozo=osszeg