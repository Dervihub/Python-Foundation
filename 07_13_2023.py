from os import *
import sys

system('cls')


print("------------------------------1-----------------------------")
class MyList(list):
    def remove(self, value: int):
        while value in self:
            super().remove(value)


lst = MyList(list(map(int, input("listga son kiriting: ").split())))
lst.remove(int(input("O'chirmoqchi bo'lgan son: ")))
print(lst)

print("-------------------------------2---------------------------")
class ElementDuplicationError(Exception):
    pass

class MyList(list):
    def append(self, son: int):
        try:
            if not son in self:
                super().append(son)
            else:
                raise ElementDuplicationError("Element is duplicated\n")
        except Exception as qaytarilgan:
            print(qaytarilgan)
            return False


lst = MyList()
sikl = None

while sikl == None:
    print(lst)
    sikl = lst.append(int(input('Son kiriting: ')))

print("----------------------------Masala----------------------------")
class MyList(list):
    def save(self, son: int, i: int = 0):
        while len(self) != self.count(son):
            if self[i] != son:
                self.pop(i)
                i -= 1
            i += 1
            
lst = MyList(list(map(int, input("listga son kiriting: ").split())))
lst.save(int(input("Saqlamoqchi bo'lgan sonni kiriting: ")))
print(lst)

print("-------------------------------3------------------------------")
class Asosiy:
    Phone= ['+998 33 651 31 24',
            '+998 33 677 41 04',
            '+998 33 566 62 04',
            '+998 33 742 82 45',
            '+998 62 299 67 26',
            '+998 33 554 13 04',
            '+998 55 909 84 80',
            '+998 90 474 95 41',
            '+998 90 061 55 33',
            '+998 88 796 23 94',
            '+998 33 571 33 62',
            '+998 33 404 57 99',
            '+998 33 301 37 38',
            '+998 88 117 73 49',
            '+998 33 211 04 23',
            '+998 55 906 58 43',
            '+998 55 909 42 11',
            '+998 33 835 00 54',
            '+998 62 299 75 40',
            '+998 88 621 52 65',
            '+998 88 895 68 28',
            '+998 88 605 56 87',
            '+998 71 982 19 12',
            '+998 33 124 79 13',
            '+998 88 636 74 68',
            '+998 55 903 88 20',
            '+998 33 297 52 01',
            ]
class Operator(Asosiy):
    def __str__(self) -> str:
        return '\n'.join(self.Phone)

class Unical(Asosiy):
    def funksiya(self, telefon: str) -> bool:
        telefon = telefon[7:].replace(' ', '')
        for i in telefon:
            if telefon.count(i) != 1:
                return False
        return True
    
    def __str__(self) -> None:
        unikal = list(filter(self.funksiya, self.Phone))
        return f"\nUnikal raqam -> {unikal}"


raqam = Operator()
print(raqam)
raqam = Unical()
print(raqam)


print("-------------------------------4------------------------------")

class SureName:
    Names = [
        'Vivian Kidd', 
        'Bradyn Grant',
        'Alexis Strickland',
        'Madeleine Dunn',
        'Emanuel Deleon',
        'Charlotte Moody',
        'lan Wells',
        'Greyson Sellers',
        'Abril Cordova',
        'Julissa Wolf',
        'Gabrielle Osborne',
        'Brian Webster',
        'Ethen Charles',
        'Ashtyn Cowan',
        'Brycen Benson',
        'Thomas Sexton',
        'Brynlee Park',
        'Keaton Pena',
        'Lily Ochoa',
        'Jaycee Glass',
        'Anderson Stark',
        'Alexandria Harper',
        'Derek Cooley',
        'Savannah Coleman',
        'Chase Cantu',
        'Maverick Gonzales',
        'Wyatt Browning',
        'Brenden Walter',
    ]

class Sortlash(SureName):
    def __str__(self) -> str:
        self.Names.sort(key=lambda x: x[x.index(' '):])
        return '\n'.join(self.Names)

lst = Sortlash()
print(f"\nSortlandi:\n{lst}")