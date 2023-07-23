#------------------------------1-Vazifa-----------------------------
print("\t\t\t\t 1-Vazifa")
for i in range(1, 801):
    print(i)
#------------------------------2-Vazifa-----------------------------
print("\t\t\t\t 2-Vazifa")
for i in range(1000, 0, -1):
    print(i)
#------------------------------3-Vazifa-----------------------------
print("\t\t\t\t 3-Vazifa")
for i in range(400, 501):
    print(i)
#------------------------------4-Vazifa-----------------------------
print("\t\t\t\t 4-Vazifa")
for i in range(300, 149, -1):
    print(i)
#------------------------------5-Vazifa-----------------------------
print("\t\t\t\t 5-Vazifa")
for i in range(-400, 251):
    print(i)
#------------------------------6-Vazifa-----------------------------
print("\t\t\t\t 6-Vazifa")
for i in range(200, -501, -1):
    print(i)
#------------------------------7-Vazifa-----------------------------
print("\t\t\t\t 7-Vazifa")
for i in range(1, 141):
    if i % 2 == 0:
        print(i)
#------------------------------8-Vazifa-----------------------------
print("\t\t\t\t 8-Vazifa")
for i in range(100, 241):
    if i % 2 == 1:
        print(i)
#------------------------------9-Vazifa-----------------------------
print("\t\t\t\t 9-Vazifa")
for i in range(40, 181):
    if i % 7 == 0:
        print(i)
#------------------------------10-Vazifa-----------------------------
print("\t\t\t\t 10-Vazifa")
for i in range(50, 441):
    if i % 11 == 0:
        print(i)
#------------------------------10.2-Vazifa-----------------------------
print("\t\t\t\t 10.2-Vazifa")
for i in range(50, 441):
    if i % 11 == 0:
        print(i)
#------------------------------11-Vazifa-----------------------------
print("\t\t\t\t 11-Vazifa")
for i in range(25, 691):
    if i % 5 == 0 and i % 9 == 0:
        print(i)
#------------------------------12-Vazifa-----------------------------
print("\t\t\t\t 12-Vazifa")
for i in range(1, 4001):
    if i % 11 == 0 and i % 3 == 0:      #3 ga bo'linadiganlar 9 ga ham bo'linadi
        print(i)
#------------------------------13-Vazifa-----------------------------
print("\t\t\t\t 13-Vazifa")
for i in range(20, 421):
    if i % 5 == 0 and i % 10 != 0:
        print(i)
#------------------------------14-Vazifa-----------------------------
print("\t\t\t\t 14-Vazifa")
a = int(input("Son kiriting: "))

for i in range(1, a+1):
    i *= i
    print(i)
#------------------------------15-Vazifa-----------------------------
print("\t\t\t\t 15-Vazifa")
a = int(input("Son kiriting: "))

for i in range(1, a+1):
    if i*i >= a:
        break
    
    i *= i
    print(i)