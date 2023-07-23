from math import sqrt
import os
from abc import *

os.system('cls')


print('----------------------------------1----------------------------------')


class Canculator():
    def __init__(self, N: int) -> None:
        self.N = N
        
    def plus(self, son: int = 1):
        self.N += son
        print("N =", self.N)

    def minus(self, son: int = 1):
        self.N -= son
        print("N =",self.N)

    def multiply(self, son: int = 2):
        self.N *= son
        print("N =", self.N)

    def divide(self, son: int = 2):
        self.N //= son
        print("N =", self.N)

    def sqrt(self, son: float = 2.0):
        self.N = sqrt(self.N, son)
        print("N =", self.N)
    
    def pow(self, son: int = 2):
        self.N **= son
        print("N =", self.N)
    
    def mod(self, son: int = 1):
        self.N %= son
        print("N =", self.N)

    def get_answer(self):
        print("N ning qiymati", self.N)


calc = Canculator(int(input("N = ")))
calc.plus(5)       # N = 15
calc.plus()	       # N = 16
calc.mod(2)        # N = 0
calc.plus()        # N = 1
calc.multiply(100) # N = 100
calc.multiply()    # N = 200
calc.minus(40)     # N = 160
calc.minus()       # N = 159
calc.N             # bu xolatda error berishi kerak.
calc.get_answer()  # N ning qiymati 159.


print('----------------------------------2----------------------------------')



hammasi = []

class Mashina:
    def __init__(self,nomi,turi,ishlab_chiqarilgan_yili: int,narxi: int = 4000):
        self.nomi = nomi
        self.turi = turi
        self.yili = ishlab_chiqarilgan_yili
        self.narxi = narxi

    def malumot(self):
        hammasi.append([self.nomi,self.turi,self.narxi,self.yili])
        if len(hammasi) ==  takror:
            hammasi.sort(key=lambda x:x[3])
            print('\n\nNatija:')
            for i in hammasi:
                print(f"\nNomi: {i[0]}\nTuri: {i[1]}\nNarxi: ${i[2]:}\nIshlab chiqarilgan yili: {i[-1]}")


takror = int(input('Qancha mashina malumotini kiritmoqchisiz: '))
for i in range(takror):
    nom = input('Mashina nomi: ')
    tur = input('Turi(yengil, yuk avtomobili): ')
    try:
        narx = int(input("Narxi: "))
    except:
        narx = ''
    yil = int(input("Ishlab chiqarilgan yili: "))
    print()
    
    car = Mashina(nom, tur, yil,narx)
    car.malumot()



print('----------------------------------3----------------------------------')


lst = []

class Countries:
    def __init__(self,davlat_nomi, poytahti, aholi_soni, yer_maydoni, prezidenti):
        self.nomi = davlat_nomi
        self.poytaxti = poytahti
        self.aholi_soni = aholi_soni
        self.yer_maydoni = yer_maydoni
        self.prezidenti = prezidenti

    def info(self):
        lst.append([self.nomi,self.poytaxti,self.aholi_soni,self.yer_maydoni,self.prezidenti])
        if len(lst) ==  urunish:
            lst.sort()
            for i in lst:
                print('\n\nNatija:')
                print(f"\nDavlat nomi: {i[0]}\nPoytaxi: {i[1]}\nAholi soni: {i[2]:} kishi\nYer maydoni: {i[3]} km²\nPreizdenti: {i[-1]}")


urunish = int(input('Qancha mamlakat malumotini kiritmoqchisiz: '))
for i in range(urunish):
    nom = input('Davlat nomi: ')
    poytaxt = input('Poytaxti: ')
    soni = int(input('Aholi soni: '))
    maydon = int(input('Yer maydoni: '))
    pre = input('Prezidenti: ')
    print()
    
    car = Countries(nom, poytaxt, soni, maydon, pre)
    car.info()