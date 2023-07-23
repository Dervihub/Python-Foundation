#------------------------------------G53---------------------------------------
print("\t\t\t\t G53")
a = int(input("Son kiriting: "))

for i in range(0, a):
    for j in range(0, a):
        if i >= j:
            if (i+j) % 2 == 0:
                print("1 ", end="")
            else:
                print("0 ", end="")
    print("")
#------------------------------------P1---------------------------------------
print("\t\t\t\t P1")
a = int(input("Qator -> "))
b = int(input("Ustun -> "))

if (a+b) % 2 == 1:
    print("qora")
else:
    print("oq")
#------------------------------------P2---------------------------------------
print("\t\t\t\t P2")
a = int(input("5 xonali son -> "))
max = 0

while a != 0:
    max += (a % 10) 
    a = int(a / 10)

print(max)
#------------------------------------P3---------------------------------------
print("\t\t\t\t P3")
a = int(input("Son -> "))

for i in range(1, a+1):
    if i % 2 == 0:
        print(i)
#------------------------------------P4---------------------------------------
print("\t\t\t\t P4")
a = int(input("N -> "))

print("Kutilayotgan natija:")
print("1", end="")

bir = "1"
had = 1
max = 1

for i in range(2, a+1):
    had = int(bir * i)
    max += had
    print(" +", bir * i, end="")
print(" = ", max)
#------------------------------------P5---------------------------------------
print("\t\t\t\t P5")
for i in range(1, 1000):
    temp = 0
    for j in range(1, i+1):
        if temp > 9:
            break
        if i % j == 0:
            temp += 1        
    if temp == 9:   
        print(i)
#------------------------------------P6---------------------------------------
print("\t\t\t\t P6")
sana = 0

for i in range(0, 100):
    if i % 10 == 3 or int(i / 10) == 3:
        sana += 1
        print(i, end="  ")
print("= ", sana ,"ta")
#------------------------------------P7---------------------------------------
print("\t\t\t\t P7")
for i in range(1, 100):
    for j in range(2, i+1):
        if i == j:
            j = i
            if i > 10:
                j = (i % 10)* 10 + i // 10
            print(j, end="  ")
        if i % j == 0:
            break
print("")
#------------------------------------P8---------------------------------------
print("\t\t\t\t P8")
a = int(input("Son kiriting: "))

max = 0
for i in range(0, a+1):
    max += i
print(max)
#------------------------------------P9---------------------------------------
print("\t\t\t\t P9")
yigindi = 0                 
yigindi2 = 0

for i in range(10, 50000):
    if i > 18420:           #50000dan kichiklari 220 dan 18416 gacha davom etadi 
        break               #davom ettirishni ma'nosi yo'q
    yigindi = 0
    for bolinuvchi in range(1, int(i/2)+1):
        if i % bolinuvchi == 0:
            yigindi += bolinuvchi
    if yigindi == 1 or yigindi <= i:
        continue
    j = yigindi
    yigindi2 = 0
    for bolinuvchi in range(1, int(j/2)+1):
        if j % bolinuvchi == 0:
            yigindi2 += bolinuvchi
    if yigindi == j and yigindi2 == i:
        print(i,"va",j)