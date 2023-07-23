from os import system
from math import *
system("cls")


print("----------------------------N10------------------------------")
# Foydalanuvchi 2 ta stringlar kiritadi. 
# Shu stringlarni ikkalasida ham bor belgilarni boshqa yangi listga o'zlashtiring.
# Va oxirida shu yangi listni ekranga chiqaring

str1 , str2 = input("1-string -> "), input("2-string -> ")
print(list(filter(lambda x:True if x in str2 else False, str1)))

print("----------------------------F33------------------------------")
#Foydalanuvchi gap kiritadi.
# Shu gapda dastlabki uchragan raqamning indexini ekranga chiqaring,
# Agar raqam yo'q bo'lsa ekranga "yo'q" degan yozuv chiqsin

def bormi(belgi: str) -> str | int:
    for i in belgi:
        if i.isdigit():
            return i
    return "yo'q"

str1 = input("Matn yoki soz kiriting: ")
print(bormi(str1))

print("----------------------------F34------------------------------")
#Foydalanuvchi string kiritadi.
# Shu stringda birinchi uchragan katta harf indexini ekranga chiqaring.
# Agar katta harf yo'q bo'lsa, "yo'q" ekranga chiqarilsin

def kattaHarf(soz: str) -> int | str:
    for i in soz:
        if i.isupper():
            return soz.index(i)
    return "Katta harf mavjud emas"

str1 = input("Matn yoki soz kiriting: ")
print(kattaHarf(str1))

print("----------------------------N5------------------------------")
# Foydalanuvchi string kiritadi va n son kiritadi.
# String dan n nchi belgini o'chirib yuboring

str1 = input("string kiriting: ")
n = int(input("index kiriting: "))

str1 = list(str1)
str1.pop(n)
print(''.join(str1))

print("----------------------------N6------------------------------")
# Foydalanuvchi string kiritadi.
# Shu string dan probel larni o'chirib yuboring

str1 = input("string kiriting: ")
print(''.join(list(filter(lambda x:False if x == ' ' else True, str1))))

print("-----------------------------O13-----------------------------")
# Quyidagi arraydan nusxa oling va olingan nusxani juft indexdagilarni 2 chi darajaga ko'tarib,
# toq indexdagilarni kubga ko'tarib nusxalangan 
# arrayga o'zlashtirib dastlabki va nusxa olingan arrayni ekranga chiqaring

lst = [7, 8, 1, 3, 4, 6, 7, 5]
print(list(map(lambda x:x**2 if not lst.index(x) % 2 else x**3, lst)))

print("-----------------------------O14-----------------------------")
# Berilgan arraylarni bir-biraga qo'shing ya'ni birlashtiring

lst1, lst2, lst3 = [2, 8, 5], [3, 7, 1], [10, -6, 2]
listlar = lst1 + lst2 + lst3
print(listlar)

print("-----------------------------O15-----------------------------")
# Berilgan tuple dagi oxirgi uchragan n qiymatning indexini toping.

n = int(input("Son kiriting: "))
numbers = (5, -3, 4, -2, 1, -9, 8, -6, 7, 0, 4)
new_number = numbers[::-1]
print((len(new_number) - 1) - new_number.index(n))

print("-----------------------------O16-----------------------------")
# Foydalanuvchi kiritgan n son, numbers nomli tuple da mavjud bo'lsa,
# barcha n larni o'chirib qo'ying va numbers ni ekranga chiqaring.
# Agar kiritilgan son, tuple da topilmasa hech narsa o'chirmaysiz

n = int(input("Son kiriting: "))
numbers = (5, -3, 4, -2, 1, -9, 8, -6, 7, 0, 4)
numbers=list(numbers)
for i in range(numbers.count(n)):
    numbers.remove(n)
print(numbers)