from os import system
from math import *
import random as r

#map va filter
#lambda

system("cls")
"""
print("---------------------------------------R1---------------------------------------\n")
#Sonlardan tashkil topgan listdagi barcha sonlarni float typega o'tkazib chiqing.
#lambda funksiya ishlating.

lst = list(map(int, input("Listga son kiriting: ").split()))
print(list(map(lambda x: float(x), lst)))

print("---------------------------------------R2---------------------------------------")

print("---------------------------------------R3---------------------------------------\n")
#Listda hodimlar to'g'risida ma'lumotlar tuple ko'rinishida berilgan:
#map dan foydalanib hodimlarning familiya-ismini alohida, tug'ilgan sanasini alohida va 
#maoshini alohhida ro'yxatga o'tkazing.

hodimlar = [("Karimov Sardor", "12.02,2002","400000"),
            ("Baxtiyorova Dildora", "28.12,2004","600000"),
            ("Karimova Maftuna", "30.05,2002","310000"),
            ("Zokirov Sardor", "01.02,2002","1600000")
            ]
hodimlar = list(map(list ,hodimlar))

ismf = list(map(lambda x: x[0], hodimlar))
tugulgan = list(map(lambda x: x[1], hodimlar))
oylik = list(map(lambda x: x[2], hodimlar))
print(f"Ism va familiyasi: {ismf}\nTug'ulgan yili: {tugulgan}\nMaoshi: {oylik}")

print("---------------------------------------R4---------------------------------------\n")
#Lambda funksiyadan foydalanib birinchi listdan ikkinchi listda mavjud elementlarni o'chirib tashlang.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
print(list(filter(lambda x: False if x in list2 else True, list1)))

print("---------------------------------------R5---------------------------------------\n")
#Lambda funksiyadan foydalanib berilgan satrli listda qidirilayotgan elemntlarni ajratib oling.

social = ["Instgram", "Facebook", "Telegram", "Tik-Tok", "Radiogram", ]
print(social)
search = input("Search = ")
print(list(filter(lambda x:True if search in x else False, social)))


#------------------------------------------------------------------------------------------
#-----------------------------------27.01.2023 Amaliyot------------------------------------


print("----------------------------------------1---------------------------------------\n")
#Funksiyaga son yuboriladi sizning vazifangiz 0 dan yuborilgan songacha oraliqda tub sonlarni ekranga chop etuvchi rekursiv funksiya tuzing.

def recursive(stop: int, start: int = 0):
    if start == stop:
        return 0    
    for i in range(2, start):
        if not start % i:
            break
        elif i+1 == start:
            print(start, end=' ')
    recursive(stop, start+1)

son = int(input("Son kiriting: "))
recursive(son)

print("----------------------------------------2---------------------------------------\n")
#Map funksiyasidan foydalangan xolda listdagi haqiyqiy sonlarni tepaga yaxlitlab oziga ozlashtiruvchi dastur tuzing.

lst = list(map(lambda x: float(x) if '.' in x else int(x), input("Listga float va int son kiriting: ").split()))
lst = list(map(lambda x: ceil(x) if type(x) == float else x, lst))
print(lst)
lst.clear()

print("----------------------------------------3---------------------------------------\n")
#Map funksiyasidan foydalangan xolda listdagi haqiyqiy sonlarni butun qismini o'ziga o'zlashtiruvchi dastur tuzing.

lst = list(map(lambda x: float(x) if '.' in x else int(x), input("Listga float va int son kiriting: ").split()))
print(list(map(lambda x: round(x), lst)))
lst.clear()

print("----------------------------------------4---------------------------------------\n")
#Map funksiyasi yordamida kiritilgan son musbat bo’lsa manfiyga o’giring aks xolda sonni 2 lab oziga ozlashtiruvchi dastur tuzing.

print(list(map(lambda x:-x if x>0 else x*2, list(map(int, input("Listga son kiriting: ").split())))))

print("----------------------------------------5---------------------------------------\n")
#Filter funksiyasi yordamida kiritilgan N sonini kubidan katta sonlarni listga ozlashtiruvchi dastur tuzing.

print("Shart tushunarsiz")

print("----------------------------------------6---------------------------------------\n")
#Filter funksiyasi yordamida butun sonlarni listga ozlashtiruvchi dastur tuzing.

lst = list(map(lambda x: float(x) if '.' in x else int(x), input("Listga float va int son kiriting: ").split()))
print(list(filter(lambda x:True if type(x) == int else False, lst)))
lst.clear()

print("----------------------------------------7---------------------------------------\n")
#Filter funksiyasi yordamida listda faqat tub sonlarni oladigan dastur tuzing.

def isprime(son: int) -> bool:
    for i in range(2, son):
        if not son % i:
            return False
    return True

lst = list(map(int, input("Listga son kiriting: ").split()))
print(list(filter(isprime , lst)))
lst.clear()

print("----------------------------------------8---------------------------------------\n")
#Filter funksiyasidan foydalangan xolda hamma stringlarni aloxida arrayga joylashtirib ekranga chop eting.

print("Shart tushunarsiz")

print("----------------------------------------9---------------------------------------\n")
#Filter funksiyasidan foydalangan xolda musbat sonlarni ekranga chop eting.

print(list(filter(lambda x: True if x>0 else False, list(map(int, input("Listga son kiriting: ").split())))))

print("----------------------------------------10---------------------------------------\n")
#Map funksiyasidan foydalangan xolda butun sonlarni float qiymatga float sonlarni int qiymatga almashtirib ekranga chop eting.

lst = list(map(lambda x: float(x) if '.' in x else int(x), input("Listga float va int son kiriting: ").split()))
print(list(map(lambda x:float(x) if type(x) == int else int(x), lst)))
lst.clear()

print("----------------------------------------11---------------------------------------\n")
#Map funksiyasidan foydalangan xolda 1 va 0 lardan tashkil topgan arrayni True va False qiymatlarga almashtirib ekranga chop eting.

lst = list(map(int, input("Listga 0 va 1 kiriting: ").split()))
print(list(map(lambda x:True if x else False, lst)))
lst.clear()

print("----------------------------------------12---------------------------------------\n")
#String kiritiladi. Belgilarni alifbo tartibida sortlab ekranga chop eting.

string = input("So'z yoki matn kiriting: ")
print(''.join(sorted(str(string.split()))))

print("----------------------------------------13---------------------------------------\n")
#String kiritiladi. Belgilarni alifboga nisbatan teskri tartibida sortlab ekranga chop eting.

string = input("So'z yoki matn kiriting: ")
print(''.join(sorted(str(string.split()), reverse=True)))

print("----------------------------------------14---------------------------------------\n")
#Lambdadan foydalangan xolda 3 ta sondan maksimumini qaytaruvchi funksiya tuzing. (max funksiyasidan foydalanmag!)

a, b, c = int(input("1-son -> ")), int(input("2-son -> ")), int(input("3-son -> "))
print((lambda a, b, c:a if a>b and a>c else b if b>a and b>c else c)(a,b,c))

print("----------------------------------------15---------------------------------------\n")
#Listdagi xamma raqamlarni listdagi maksimal sonning qiymatiga o'zgaritring.

lst = list(map(int, input("Listga son kiriting: ").split()))
print(list(map(lambda x:max(lst), lst)))

print("----------------------------------------16---------------------------------------\n")
#listdagi manfiy sonlarni listdan ongga, musbatlarni listdan ortaga nollarni chapga joylashtiring.

def sortlash(lst: list) -> list:
    manfiy = lst[:lst.index(0)]
    while lst.index(0) != 0:
        lst.pop(0)
    return lst + manfiy

lst = list(map(int, input("Listga son kiriting: ").split()))
lst.sort()
print(sortlash(lst))

print("----------------------------------------17---------------------------------------\n")
#Dictionaryni keylarini aloxida KEYS nomli listga valuelarini esla VALUES nomli listga joylashtiring
#songra VALUES nomli listni teskari tartibda sortlab ekranga chop eting.

dict1 = {"bir": 1,"ikki": 2, "uch": 3}
keys = list(dict1.keys())
values = list(dict1.values())
print("keys:",keys,"\nvalues:", values)
print(sorted(values, reverse=True))

print("----------------------------------------18---------------------------------------\n")
#Foydalanuvchi gap kiritadi kiritgan gapni ekranga chop eting.
#5 ta taqiqlanuvchi so'zlar mavjud agar foydalanuvchi shu sozlardan foydalangan bo’lsa
#shu so'z uzunligicha '*' belgisini ekranga chop eting.

taqiq = ["salom", "eshmat", "toshmat", "dunyo", "noutbuk"]
print(f"Taqiqlanuvchi so'zlar: {taqiq}")
gap = input("Gap kiriting: ")
print(gap.split())
print(' '.join(map(lambda x:len(x)*'*' if x in taqiq else x, gap.split())))

print("----------------------------------------19---------------------------------------\n")
#Foydalanuvchi tomondigan listga sonlar berilgan.
#Berilgan sonlarni minimum 2 ta nollari borlarini saralab ekranga chop eting.

lst = input("Listga son kiriting: ").split()
lst_new = list(filter(lambda x:True if x.count('0') >= 2 else False, lst))
print(list(map(int, lst_new)))

print("----------------------------------------20---------------------------------------\n")
#Foydalanuvchi gap kiritadi gapdagi eng ko'p takrorlangan so'zni ekranga chop etuvchi funksiya tuzing.

string = input("gap yoki matn kiriting: ")
lst = string.split()
print(max(lst, key=lst.count))
"""
print("----------------------------------------21---------------------------------------\n")
#Kiritilgan rim raqamini son korinishida tasvirlang.

def rim_raqami(rim_son: list,) -> int:
    raqam = dict1.get(rim_son[0])       #Chala
    for i in range(len(rim_son)-1):
        son1 = dict1.get(rim_son[i+1])
        if raqam < son1:
            raqam = son1 - raqam
        else:
            raqam += son1
    return raqam
            
dict1 = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M':1000}        
rim_son = list(input("Rim raqamini kiriting: "))
print(rim_raqami(rim_son))
"""
print("----------------------------------------22---------------------------------------\n")
#2 o'lchovli listdan maksimal sonni topuvchi dastur tuzing.

matrix = [[3,0,9],[23,9,10],[89,43,21]]
print(max(map(max, matrix)))

print("----------------------------------------25---------------------------------------\n")
#Har bir talaba [0, 100] oralig'idagi baho bilan baholanadi.
#Baho va undan keyingi 5 ga karrali son orasidagi farq 3 dan kichik bo’lsa, 
#bahoni undan keyingi 5 ga karrali songa yaxlitlaydi, aks holda o’zgartirishsiz qoldiradi.
#Agar baho 38 dan kam bo'lsa, bu talaba baribir o'qishdan chetlashtirilishini inobatga olib bahoni o’zgartirishsiz qoldiradi.

baho = int(input("baho kiriting: "))
if baho >= 38:
    if baho % 5 >= 3 :
        baho = (baho // 5 + 1) *5
print(f"Hosil bo'lgan ball -> {baho}")
"""