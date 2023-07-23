#--------------------------------------O1--------------------------------------
print("\t\t\t\t\t O1")
a = input("Yozing: ")
print(type(a),)
#--------------------------------------O2--------------------------------------
print("\t\t\t\t\t O2")
a = int(input("1-son: "))
b = int(input("2-son: "))
print((a + b) / 2)
#--------------------------------------O3--------------------------------------
print("\t\t\t\t\t O3")
a = input("1-belgi kiriting: ")
b = int(input("2-son kiriting: "))
print(a*b)
#--------------------------------------O4--------------------------------------
print("\t\t\t\t\t O4")
a = input("2 xonali son: ")
print(int(a[::-1]))
#--------------------------------------O5--------------------------------------
print("\t\t\t\t\t O5")
a = int(input("Sekund kiriting: "))
print(a//3600, "soat",a%3600//60,"min", a%60,"sek")
#--------------------------------------O6--------------------------------------
print("\t\t\t\t\t O6")
a = int(input("Baytni kiriting: "))
print(a//1024, "Kb")
#--------------------------------------O7--------------------------------------
print("\t\t\t\t\t O7")
a = input("A = ")
b = input("B = ")
son = int(a.lstrip("-"))
son2 = int(b.lstrip("-"))
korinish = "("+son2*"-"+")"
print(str(korinish) * int(son//son2) + "-" * (son%son2) + str(son//son2))
#--------------------------------------O8--------------------------------------
print("\t\t\t\t\t O8")
a = input("3 xonali son: ")
print("-".join(a))
#--------------------------------------O9--------------------------------------
print("\t\t\t\t\t O9")
a = int(input("a tomoni: "))
b = int(input("b tomoni: "))
c = int(input("c tomoni: "))
print(a+b+c,"sm")
#--------------------------------------O10-------------------------------------
print("\t\t\t\t\t O10")
a = input("Ism kiriting: ")
print("Salom {} , yaxshimisiz?".format(a))
#--------------------------------------O11-------------------------------------
print("\t\t\t\t\t O11")
M = int(input("Milodiy yil = "))
print("Hijriy yil =", int(M - 622 +(M - 622)/ 32))
#--------------------------------------O12-------------------------------------
print("\t\t\t\t\t O12")
a = int(input("Yil -> "))
print(a//100+1,"asr")
#--------------------------------------O13-------------------------------------
print("\t\t\t\t\t O13")
a = input("So\'z kiriting: ")
print(a[0].upper() + a[1:len(a)] + a[-1].upper())
#--------------------------------------O14-------------------------------------
print("\t\t\t\t\t O14")
a = "Welcome to najot talim. najot talim awesome, isn't it"
print(a)
b = input("So\'zni yozing: ") 
print(a.count(b))