from os import *
import random
system('cls')

class Kanallar():
    k = ["Yoshlar",
         "Toshkent",
         "O'zbekiston 24",
         "Madaniyat va Marifat",
         "Sport TV",
         "Dunyo bo'ylab",
         "Bolajon",
         "Milliy",
         "MY5",
         "Zo'r TV",
         ]

class Pult(Kanallar):
    def __init__(self, on_off: int):
        if on_off:
            self.ovoz = 5
            self.kanal = random.randint(0, 9)
        else:
            exit()
        
    def boshqaruv(self, control: int):
        if control == 1:
            exit()
        if control == 2:
            if self.ovoz != 0:
                self.ovoz -= 1
        if control == 3:
            if self.ovoz < 10:
                self.ovoz += 1
        if control == 4:
            self.kanal += 1
            self.kanal %= 10
        if control == 5:
            if self.kanal == 0:
                self.kanal = 9

    def __str__(self):
       return f"""
Kanal: {self.k[self.kanal]}
Ovoz: {self.ovoz}"""

pult = Pult(int(input("1 - Yoqish , 0 - O'chirish: ")))
while True:
    print(pult)
    pult.boshqaruv(int(input("on/off(1) , Ovoz(2,3) , Kanal(4,5) :")))