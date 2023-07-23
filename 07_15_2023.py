import os
from random import *
from math import *

os.system('cls')

"""
print('--------------------------Masala-------------------------------')
class MyList(list):
    def random(self, n, rand_min: int=-100, rand_max: int=100):
        for i in range(n):
            self.append(randint(rand_min, rand_max))

lst = MyList()
lst.random(int(input('N = ')), )
print(lst)


print('--------------------------Masala.1---------------------------')
class Soldat():
    Odam = [
        'Herve, Lerven, Female, 38, 170, 64',
        'Karim, Firbanks, Male, 17, 164, 65',
        'Christalle, Kubacek, Male, 25, 182, 71',
        'Dyan, Castiglioni, Male, 50, 173, 60',
        'Esma, Weale, Female, 18, 156, 45',
        'Rafaelita, Lutas, Female, 40, 165, 53',
        'Robby, Salvadori, Male, 34, 164, 73',
        'Berna, Jordine, Female, 40, 177, 65',
        'Massimiliano, Fawcus, Male, 57, 182, 79',
        'Beatrix, Fibbitts, Male, 34, 188, 77',
        'Carlene, Cremer, Male, 18, 169, 68'
    ]

class Armiya(Soldat):
    def __init__(self):
        for i in range(len(self.Odam)):
            self.Odam[i] = self.Odam[i].split(', ')
        self.Odam = list(filter(lambda x: 'Male' in x and int(x[3]) > 17, self.Odam))

    def info(self):
        for i in self.Odam:
            rol = "Tank qo'shinlariga"
            if int(i[-1]) > 75 and int(i[-2]) > 150:
                rol = "Piyoda askarligiga"
            print(f'\nIsm familiya: {i[0]} {i[1]}\nYoshi: {i[3]}\n{rol}')
        
askarlar = Armiya()
askarlar.info()


print('--------------------------Masala.2---------------------------')
class Uchburchak:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

class Kvadrat(Uchburchak):
    def __init__(self, a: float, b: float, c: float, kv: float):
        super().__init__(a, b, c)
        self.kv = kv
    
    def __str__(_):
        if _.a + _.b > _.c and _.a + _.c > _.b and _.b + _.c > _.a:  #Uchburchakmi yo'qmi
            kv_d = hypot(_.kv, _.kv)    #kvadratni diagonal
            if _.a < kv_d and _.b < kv_d and _.c < kv_d:      #kv_gipa tomomlardan katta bo'lsa 
                return "Kvadratni ichiga Uchburchak sig'adi"
            uch_balandlik = 0.5/_.b * sqrt(_.a+_.b+_.c) * sqrt(-_.a+_.b+_.c) * sqrt(_.a-_.b+_.c) * sqrt(_.a+_.b-_.c)
            if _.kv <= (_.b * uch_balandlik) / (_.b + uch_balandlik):
                return "Uchburchak ichiga Kvadrat sig'adi"
            return "Kvadrat yoki Uchburchak bir biriga sig'maydi"
        return "Kiritilgan parametrdan Uchburchak chiqmaydi"

sigm = Kvadrat(float(input('a = ')), float(input('b = ')), float(input('c = ')), float(input("Kv bo'yi: ")))
print(sigm)


print('--------------------------3-Masala---------------------------')
class Cars:
    file = [
        "1,Rebecka,Monro,Female,Ford,1995,Pink,Japan",
        "2,Adi,Gainsboro,Female,Mercury,1996,Violet,Portugal",
        "3,Nissie,Leftly,Female,Mazda,2005,Mauv,Canada",
        "4,Abba,Janaszkiewicz,Male,GMC,2003,Khaki,Philippines",
        "5,Herschel,Spadeck,Male,Ford,1977,Fuscia,Indonesia",
        "6,Danica,Fontenot,Female,Lincoln,2010,Maroon,United Kingdom",
        "7,Cammie,Sidery,Female,Ford,1989,Blue,China",
        "8,Thorny,Rosberg,Male,Toyota,2010,Teal,Greece",
        "9,Jeromy,Luetkemeyers,Agender,Toyota,2007,Purple,Philippines",
        "10,Sumner,Tattershall,Male,Pontiac,1989,Khaki,Italy",
        "11,Clayborne,Frostdick,Male,Toyota,2000,Violet,Vietnam",
        "12,Collen,Boullin,Female,GMC,2005,Red,Indonesia",
        "13,Adah,Caughtry,Female,Mercedes-Benz,2007,Goldenrod,Philippines",
        "14,Dean,Goodread,Male,GMC,2008,Teal,China",
        "15,Maxie,De Vaux,Female,Mercury,1984,Fuscia,Philippines",
        "16,Ebeneser,Pack,Male,Pontiac,1991,Orange,Japan",
        "17,Adorne,Lodwig,Polygender,Alfa Romeo,1993,Goldenrod,China",
        "18,Lily,Scoyne,Female,Lexus,2004,Orange,Indonesia",
        "19,Tabb,Wyrall,Male,Infiniti,2006,Red,Albania",
        "20,Bentley,Camerello,Male,Dodge,1995,Teal,Philippines",
    ]
    
    def Method_1(self):
        w, m = 0, 0
        for i in range(len(self.file)):
            self.file[i] = self.file[i].split(',')
            if self.file[i][3] == 'Female':
                w += 1
            else:
                m += 1
        if w>m:
            print(f"Ayollar erkaklarga nisbatan {w/m *100-100 :.2f}% foiz ko'p")
        else:
            print(f"Erkakalar ayollarga nisbatan {m/w *100-100 :.2f}% foiz ko'p")


    def Method_2(self):
              pass
        
car = Cars()
car.Method_1()
car.Method_2()


print("-------------------------------U4-------------------------------")
"""
print("-------------------------------U7-------------------------------")
class Karta:
    def __init__(self, nomi,seriya: int,muddati, parol, summa: int):
        self.nomi = nomi
        self.seriya = seriya
        self.muddati = muddati
        self.__parol = parol
        self.__summa = summa
        
    def parol_ozgartir(self, parol: str, new_parol: str):
        if self.__parol == parol:
            self.__parol = new_parol
        else:
            print("Parol noto'ri")
            
    def parol_korsat(self, parol: str):
        if self.__parol == parol:
            return self.__parol

    def summani_korsat(self):
        return self.__summa
    
    def summaga_qosh(self, summa: int):
        self.__summa += summa
            
    def summadan_ol(self, summa: int):
        self.__summa -= summa

    
class User(Karta):
    def __init__(self, ism,familiya,naqat_pul: int, nomi,seriya: int,muddati,parol,summa: int):
        self.ism = ism
        self.familiya = familiya
        super().__init__(nomi, seriya,muddati,parol,summa)
        self.naqt_pul = naqat_pul
        
class ATM(User):
    def info(self):
        return f"""
Ism: {self.ism}
Familiya: {self.familiya}
Karta: {self.seriya}
Muddati: {self.muddati}
Parol: {self.__parol}"""

    def naqt_pul_olish(self, pul: int):
        super().summadan_ol(pul)

    def kartaga_pul_qoyish(self, pul: int):
        super().summaga_qosh(pul)

atm = ATM("Abdulla", "Vohidov", 1_000_000, "Asaka", "8600 3902 9201 2355", "02/25", '1111', 0)
print(atm.info())
atm.parol_ozgartir(input('eski parolni kiriting: ', input("yangi parolni kiriting: ")))
print(atm.info())

#TUGALLANMAGAN MISOLLAR