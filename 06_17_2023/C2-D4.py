#------------------------------C2------------------------------------
print("\t\t\t\t C2")

for i in range(4):
    for j in range(5):
        if j == 0:
            print("|", end="")
        if i+1 == j:
            print("\\", end="")
        if i == 3 and j < 3:
            print("_", end="")
        if j != 0 and i != 3 and i+1 != j:
            print(" ", end="")
    print("")
#------------------------------D4--------------------------------------

#-----------------------------if1---------------------------------------
print("\t\t\t\t if1")

a = int(input("Butun son -> "))
if a > 0:
    a += 1
print(a)
#-----------------------------if2---------------------------------------
print("\t\t\t\t if2")

a = int(input("Butun son -> "))
if a > 0:
    a += 1
else:
    a -= 2
print(a)
#-----------------------------if3---------------------------------------
print("\t\t\t\t if3")

a = int(input("Butun son -> "))
if a > 0:
    a += 1
elif a < 0:
    a -= 2
else:
    a = 10
print(a)
#------------------------------if4---------------------------------------
print("\t\t\t\t if4")

a = int(input("1-son -> "))
b = int(input("2-son -> "))
c = int(input("3-son -> "))

musbat = 0

if a > 0:
    musbat += 1
if b > 0:
    musbat += 1
if c > 0:
    musbat += 1
print("Musbatlar soni " + str(musbat))
#------------------------------if5---------------------------------------
print("\t\t\t\t if5")

a = int(input("1-son -> "))
b = int(input("2-son -> "))
c = int(input("3-son -> "))

musbat = 0
manfiy = 0

if a > 0:
    musbat += 1
elif a < 0:
    manfiy += 1
if b > 0:
    musbat += 1
elif b < 0:
    manfiy += 1
if c > 0:
    musbat += 1
elif c < 0:
    manfiy += 1
print("Musbatlar soni " + str(musbat) + " va Manfiylar soni " + str(manfiy))
#-----------------------------------if6---------------------------------------
print("\t\t\t\t if6")

a = int(input("1-son -> "))
b = int(input("2-son -> "))

if a>b:
    print("Max =", a)
else:
    print("Max =", b)
#-----------------------------------if7---------------------------------------
print("\t\t\t\t if7")

a = int(input("1-son -> "))
b = int(input("2-son -> "))

if a<b:
    print("tartib raqami = 1")
else:
    print("tartib raqami = 2")
#-----------------------------------if8---------------------------------------
print("\t\t\t\t if8")

a = int(input("1-son -> "))
b = int(input("2-son -> "))

if a>b:
    print(a,"va",b)
else:
    print(b,"va", a)
#-----------------------------------if9---------------------------------------
print("\t\t\t\t if9")

A = float(input("1-son -> "))
B = float(input("2-son -> "))

if A < B:
    print(A, "va", B)
else:
    B += A
    print(A, "va", B)
#-----------------------------------if10---------------------------------------
print("\t\t\t\t if10")

a = int(input("1-son -> "))
b = int(input("2-son -> "))

if a != b:
    a = a+b
    b = a
elif a == b:
    a = 0
    b = 0

print(a,"va",b)