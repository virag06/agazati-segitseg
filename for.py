#for ciklus tartomány bejárására

for i in range(6):  #0-5.ig vesz fel értékeket
    print(i)

for i in range(2,10):   #2-9-ig vesz fel értékeket
    print(i)

#for ciklus teljes bejárása (pl. string/list/stb.)
for item in "alma": #string bejárása elejétől a végéig
    print(item) #a karaktereinek kiírása

    gyumolcsok=["alma","körte","barack","cseresznye","dinnye"]
    for item in gyumolcsok:#lista bejarasa
        print(item) #lista elemeinek kiírása

        print(gyumolcsok[3]) #3. indexű, azaz a 4. listaelem kiírása