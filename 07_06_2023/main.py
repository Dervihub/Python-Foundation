import os
#os.chdir(r'D:\python\06_07_2023')
os.system("cls")


print("------------------------------S1------------------------------")
# Erkaklarni ismi, familiyasi, davlatini chop eting

fayl = open("people_count.txt", encoding="utf-8")
people = fayl.read().split("\n")
for i in range(len(people)-1):
    people[i] = people[i].split(",")
men = list(filter(lambda x: "Male" in x , people))
for i in range(len(men)):
    people[i].pop(2)
    people[i].pop(2)
    print(f"{i+1}. {', '.join(people[i])}")

fayl.close()

print("------------------------------S2------------------------------")
# 1 - shahar nomi, 2 - aholi soni, 3 - tili
# Aholi soni 1 mln dan kop bo'lgan ma'lumotlarni ekranga chiqaring.

fayl = open("languages.txt", encoding="utf-8")
stat = fayl.read().split('\n')
for i in range(len(stat)):
    stat[i] = stat[i].split(',')
stat = list(filter(lambda x:len(x[1]) > 6, stat))
for i in range(len(stat)):
    print(f"{i+1}. {', '.join(stat[i])}")

fayl.close()

print("------------------------------S3.1------------------------------")
# 1-id, 2-produkt kodi, 3-material, 4-narxi, 5-bormi yo'qligi

# 1. Maqasadingiz shu ma'lumotlar orasidan narxi 500 va 1000 dollar orasida bo'lgan
# va omborda mavjud bo'lgan produktlar ID raqami
# va ishlab chiqarilgan materialini chop etish bo'ladi.

fayl = open("product_material.txt", encoding="utf-8")
product = fayl.read().split('\n')
for i in range(len(product)):
    product[i] = product[i].split(',')
product = list(filter(lambda x: 1000 > float(x[3][1:]) and float(x[3][1:]) > 500 and x[4][0] == 't',product))
for i in range(len(product)):
    print(f"{i+1} - ID: {product[i][0]}, {product[i][2]}")

fayl.close()

print("------------------------------S3.2------------------------------")

# 2. Foydalanuvchi material nomini kiritadi 
# va siz unga barcha omborda hozirda mavjud (true) bo'lgan produktlar 
# narxlarini o'sish tartibida chiqarib berishingiz lozim

nom = input("material nomini kiriting: ")
fayl = open("product_material.txt", encoding="utf-8")
product = fayl.read().split('\n')
for i in range(len(product)):
    product[i] = product[i].split(',')
product = list(filter(lambda x:x[2].lower() == nom and x[4][0] == 't',product))
product.sort(key=lambda x: float(x[3][1:]))
for i in range(len(product)):
    print(f"{i+1} - material - {product[i][2]}, {product[i][3]}")

fayl.close()

print("------------------------------S3.3------------------------------")
# 3. Omborda mavjud bo'lmagan (ya'ni false bo'lgan)
# va narxi 1000 dollardan arzon bo'lgan tovarlarning 
# ishlab chiqarilgan materialini ekranga chop eting.

fayl = open("product_material.txt", encoding="utf-8")
product = fayl.read().split('\n')
for i in range(len(product)):
    product[i] = product[i].split(',')
product = list(filter(lambda x: float(x[3][1:]) < 1000 and x[4][0] == 'f',product))
for i in range(len(product)):
    print(f"{i+1} - Materiali: {product[i][2]}")

fayl.close()

print("------------------------------S4.1------------------------------")
#id - film ID raqami
#movie - film nomi
#genre - film janri
#year - ishlab chiqarilgan yil
#cinema - kinoteatr adresi
#starts_at - film boshlanish vaqti

# 1. Foydalanuvchi taxminiy film ko'rish vaqtini kiritadi.
#Maqsadingiz kiritilgan vaqtdan keyingi hamma filmlar ro'yhatini chop etish.

hour = int(input("Filmni qaysi vaqtda(soat) ko'rishni hohlaysiz: "))
hour = 1 if hour + 1 == 24 else hour + 1

fayl = open("cinema.txt", encoding="utf-8")
kino = fayl.read().split('\n')
for i in range(len(kino)):
    kino[i] = kino[i].split(',')
kino = list(filter(lambda x: int(x[5][:x[5].find(':')]) == hour,kino))
for i in range(len(kino)):
    print(', '.join(kino[i]))

fayl.close()

print("------------------------------S4.2------------------------------")
# 2. Foydalanuvchiga 2000 yildan keyin ishlab chiqarilgan 
#va <genre> ichida Comedy yoki Drama yoki Romance bo'lgan 
#filmlar nomlari va kinoteatr adreslarini chop etib bering.

fayl = open("cinema.txt", encoding="utf-8")
kino = fayl.read().split('\n')
for i in range(len(kino)):
    kino[i] = kino[i].split(',')
kino = list(filter(lambda x: int(x[3]) > 2000 and (x[2] in "Comedy" or x[2] in "Drama" or x[2] in "Romance") ,kino))
for i in range(len(kino)):
    print(f"Nomi: {kino[i][1]}, Adresi: {kino[i][4]}")

fayl.close()

print("------------------------------S4.3------------------------------")
# 3. Soat 17:00 dan keyingi barcha Horror filmlar ro'yhatini chop eting.

fayl = open("cinema.txt", encoding="utf-8")
kino = fayl.read().split('\n')
for i in range(len(kino)):
    kino[i] = kino[i].split(',')
kino = list(filter(lambda x: int(x[5][:x[5].find(':')]) >= 17 and x[2] in "Horror" ,kino))
for i in range(len(kino)):
    print(', '.join(kino[i]))

fayl.close()

print("------------------------------S5.1------------------------------")
# id - ID raqami
# departure - uchib ketish davlati
# d_time - uchish vaqti
# arrive - qo'nish davlati
# a_time - qo'nish vaqti
# cost - bilet narxi

# 1.Foydalanuvchi o'zida bor taxminiy pul miqdorini kiritadi.
# Maqsadingiz shu kiritlgan summadan $50 arzonroq 
# va $100 qimmatroq bo'lgan biletlar ro'yhatini ko'rsatish

pul = int(input("Pul miqdoringiz: "))
fayl = open("booking_data.txt", encoding="utf-8")
books = fayl.read().split()
for i in range(len(books)):
    books[i] = books[i].split(',')
books = list(filter(lambda x:float(x[5][1:]) > pul-50 and float(x[5][1:]) < pul+100 ,books))
for i in range(len(books)):
    print(', '.join(books[i]))

fayl.close()

print("------------------------------S5.2------------------------------")
# 2. Kiritilgan davlat bo'yicha barcha aviareyslarni toping.
# Lekin chiqishda faqat soat 12:00dan 21:00gacha bo'lgan reyslar chiqsin.

davlat = input("Davlatni tanlang(RU,FR,UZ, kabi kiriting): ")
fayl = open("booking_data.txt", encoding="utf-8")
country = fayl.read().split()
for i in range(len(country)):
    country[i] = country[i].split(',')
    
country = list(filter(lambda x: (x[1] == davlat or x[3] == davlat)
    and int(x[2][:x[2].find(':')]) >= 12 and int(x[2][:x[2].find(':')]) <= 21
    and int(x[4][:x[4].find(':')]) >= 12 and int(x[4][:x[4].find(':')]) <= 21,country))

for i in range(len(country)):
    print(', '.join(country[i]))

fayl.close()

print("------------------------------S5.3------------------------------")
# Men US davlatiga uchishim kerak. 
# Meni har kuni soat 21:00da Zoomda meetingim bo'ladi. 
# Shunga menga shunday reys tanlab beringki, 
# qo'nish vaqti meetingdan kamida 1 soat oldin bo'lsin.
# Menga shu reyslarning barchasini ko'rsatsangiz, uchish vaqti qiziq emas.

fayl = open("booking_data.txt", encoding="utf-8")
country = fayl.read().split()
for i in range(len(country)):
    country[i] = country[i].split(',')
country = list(filter(lambda x: x[3] == "US" and int(x[4][:x[4].find(':')]) > 17
            and int(x[4][:x[4].find(':')]) < 21, country))
for i in range(len(country)):
    print(', '.join(country[i]))

fayl.close()

print("------------------------------S7.1------------------------------")
# 1-Funcsiya.
# Moshinaning egalari bo'yicha nisbatini topadigan method yaratish. 
# Ya'ni Erkar va ayollar foizli nisbatini toping.
# Ayollar erkaklarga nisbatan nechi foiz ko'p
# yoki erkakalar ayollarga nisbatan nechi foiz ko'p.

fayl = open("car_model.txt", encoding="utf-8")
car = fayl.read().split('\n')
w, m = 0, 0
for i in range(len(car)):
    car[i] = car[i].split(',')
    if car[i][3] == 'Female':
        w += 1
    else:
        m += 1
if w>m:
    print(f"Ayollar erkaklarga nisbatan {w/m *100-100 :.2f}% foiz ko'p")
else:
    print(f"Erkakalar ayollarga nisbatan {m/w *100-100 :.2f}% foiz ko'p")

fayl.close()

print("------------------------------S7.2------------------------------")
# 2-Funcsiya. Mashinalar soni eng ko’p bo’lgan brendni topib, 
# uning mashinalari ayni qaysi davlatda ko’pligini va qaysi 
# davlatda kamligini aniqlaydigan method yarating.


fayl = open("car_model.txt", encoding="utf-8")
car = fayl.read().split('\n')
brand , country = [], []
for i in range(len(car)):
    car[i] = car[i].split(',')
    brand.append(car[i][4])
brand = max(brand, key=brand.count)
car = list(filter(lambda x: x[4] == brand, car))
for i in range(len(car)):
    country.append(car[i][7])
print("Mashinalari eng ko'p brand", brand)
print(f"{max(country, key=country.count)} da {brand} mashinalari ko'p", end=" va ")
print(f"{min(country, key=country.count)} da {brand} mashinalari kam")

fayl.close()

print("------------------------------S7.3------------------------------")
# 3-Funcsiya. Avtomashinasi 2005 yildan oldin ishlab chiqarilgan haydovchilarga
# quyidagi ko’rinishdagi xatni tayyorlaydigan method yarating:
############
# Kimdan: Auto Test Corp.
# Kimga: <first_name> <last_name>
# Joriy davlat: <country>

# Hurmatli <fisrt_name> <last_name>! <brand> tomonidan <year>da ishlab chiqarilgan 
# <color> rangli avtoulovingiz Texnik Holatini tekshirtirsh 
# maqsadida mahalliy Auto Test Corp. ofisiga murojaat qilishingizni so’raymiz!

fayl = open("car_model.txt", encoding='utf-8')
car = fayl.read().split('\n')
for i in range(len(car)):
    car[i] = car[i].split(',')
car = list(filter(lambda x: int(x[5]) < 2005, car))
for i in range(len(car)):
    print("""
Kimdan: Avto Test Corp.
Kimga: {0} {1}
Joriy davlat: {2}

Hurmatli {0} {1}!
{3} tomonidan {4}da ishlab chiqarilgan {5} rangli avtoulovingiz
Texnik Holatini tekshirtirsh maqsadida mahalliy
Auto Test Corp. ofisiga murojaat qilishingizni so'raymiz!

""".format(car[i][1], car[i][2], car[i][-1], car[i][4], car[i][5], car[i][-2]))

fayl.close()