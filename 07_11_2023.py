from os import system
system('cls')

print('----------------------------1-misol------------------------------')

class Kitob:
    def __init__(self, nomi: str, muallif: str, narxi: float, nashriyoti: str):
        self.nomi = nomi
        self.muallif = muallif
        self.narxi = narxi
        self.nashriyoti = nashriyoti
        
kutubxona = list()
for i in range(5):
    kutubxona.append('kitob' + str(i))
    print()
    kutubxona[i] = Kitob(input("Kitob nomi: "), input('Kitob mualliflari: '), input('Kitob narxi: '), input('Kitob nashyoti: '))

alifbo = ['a', 'b', 'd', 'e', 'f', 'g' ,'h']
kutubxona = list(filter(lambda x: x.nashriyoti[0].lower() in alifbo , kutubxona))

print('\nA dan H gacha boshlanadigan nashriyotlar:\n')
for i in range(len(kutubxona)):
    print(f"\nKitob nomi -> {kutubxona[i].nomi}")
    print(f'Kitob mualliflari -> {kutubxona[i].muallif}')
    print(f"Kitob narxi -> ${kutubxona[i].narxi}")
    print(f"Kitob nashiryoti -> {kutubxona[i].nashriyoti}\n")

print('----------------------------2-misol------------------------------')

class Kompyuter:
    def __init__(self, nomi: str, RAMi: str, narxi: float, protsessori: str):
        self.nomi = nomi
        self.RAMi = RAMi
        self.narxi = narxi
        self.protsessori = protsessori
        
foydalanuvchi = list()

for i in range(4):
    foydalanuvchi.append('komp' + str(i))
    print()
    foydalanuvchi[i] = Kompyuter(input("Kompyuter nomi: "), input('Kompyuter RAMi: '), input('Kompyuter narxi: '), input('Kompyuter protsessori: '))

foydalanuvchi = list(filter(lambda x: 4 < int(x.RAMi) and 16 > int(x.RAMi), foydalanuvchi))

print('\nNatija:\n')
for i in range(len(foydalanuvchi)):
    print(f"\nKompyuter nomi -> {foydalanuvchi[i].nomi}")
    print(f"Kompyuter RAMi -> {foydalanuvchi[i].RAMi}")
    print(f"Kompyuter narxi -> ${foydalanuvchi[i].narxi}")
    print(f"Kompyuter protsessori -> {foydalanuvchi[i].protsessori}\n")

print('----------------------------3-misol------------------------------')

class User:
    def __init__(self, ism: str,user_ism: str, email: str, password: str):
        self.ism = ism
        self.user_ism = user_ism
        self.email = email
        self.password = password
    
    def get_info(self, user: str):
        return f"Foydalanuvchi: {user.ism:10} || Ismi: {user.user_ism:10} || email: {user.email:10} || Parol: {user.password:10}"

user = list()
uzunlik = int(input('Qancha foydalanuvchi kiritmoqchisiz: '))

for i in range(uzunlik):
    user.append('user' + str(i))
    print()
    user[i] = User(input('User nomi: '), input('Foydalanuvchi ismi: '), input('email: '), input('Parol: '))

print('\nNatija:')
for i in range(uzunlik):
    print(user[i].get_info(user[i]))

print('----------------------------4-misol------------------------------')

class SpaceAircraft:
    def __init__(self, nomi, height: float, fuel: float) -> None:
        self.nomi = nomi
        self.height = height
        self.fuel = fuel

    def launch(self, km: int):      # 1 km  =  50 l tahminan 10 mertli raketada
        self.fuel_ketishi = (km * 50 * (self.height//10))

    def land(self, km: int):        # qo'nishda 2 karra kam yoqilg'i sarflanadi
        if self.fuel - (km // 2 * (self.height//10) + self.fuel_ketishi) < 5:
            return "No fuel"
        return 'SpaceAircraft qo\'ndi'

raketa = SpaceAircraft(input('Model: '), float(input('Raketa balandligi(m): ')), float(input('Yoqilg\'i(l): ')))
raketa.launch(int(input("Uchish balandligi (km): ")))
print(raketa.land(int(input('Qo\'nish masofasi (km): '))))

print('----------------------------5-misol------------------------------')

class MinuteConverter:
    def __init__(self, minutes: int):
        self.minutes = minutes
    
    def toHours(self):
        return self.minutes / 60
        
    def toSeconds(self):
        return self.minutes * 60
    
    def toDays(self):
        return self.minutes / 1440
minut = MinuteConverter(int(input('Minut kiriting: ')))
print(f"\n{minut.minutes} min = {minut.toHours():.1f} soat")
print(f"{minut.minutes} min = {minut.toSeconds()} sekund")
print(f"{minut.minutes} min = {minut.toDays():.1f} kun")