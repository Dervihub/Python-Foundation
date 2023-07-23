import os
os.system("cls")

import math as m
print("-------------------------------------T1---------------------------------------\n")

                                    #yechim-1
def manfiymi(son: int) -> bool:
    return True if son > 0 else False

print(manfiymi(int(input("Son kiriting -> "))))


                                    #yechim-2
#print((lambda x: True if x > 0 else False)(int(input("Son kiriting -> "))))


print("-------------------------------------T2---------------------------------------\n")

def sortlash(lst: list) -> tuple:
    lst.sort()
    return tuple(lst)

lst = [1, 3, 9, 6, 4, 2]
print(sortlash(lst))

print("-------------------------------------T3---------------------------------------\n")

                                    #yechim-1
def data_structure(any) -> bool:
    return isinstance(any, (list, tuple, set, dict))

lst = [1, 3, 5]
print(data_structure(lst))
print(data_structure(34))

                                    #yechim-2
#tpl = (1, 3, 5)
#print((lambda x: isinstance(x, (list, tuple, set, dict)))(tpl))
#print((lambda x: isinstance(x, (list, tuple, set, dict)))("matn"))

print("-------------------------------------T4---------------------------------------\n")

def peri_yuza(a: int, b: int, lst = []) -> tuple:
    lst.append((a + b) * 2)
    lst.append(a * b)
    return tuple(lst)

print(peri_yuza(int(input("Eni -> ")), int(input("Bo'yi -> "))))

print("-------------------------------------T5---------------------------------------\n")

                                    #yechim-1
def katta(a: int, b: int) -> int:
    return a if a > b else b

a = int(input("1-son: "))
b = int(input("2-son: "))
print(katta(a, b))
                                    #yechim-2
#a = int(input("1-son: "))
#b = int(input("2-son: "))
#print((lambda a, b: a if a>b else b)(a, b))

print("-------------------------------------T6---------------------------------------\n")

def max_lst(lst: list) -> int:
    return max(lst)

lst = [3, 6, 8, 1, 0]
print(max_lst(lst))

print("-------------------------------------T7---------------------------------------\n")

def kvadrat(lst = [], a = int(input("Qancha son kiritasiz -> ")), tartib = 0) -> list:
    while a != tartib:
        tartib += 1
        son = int(input(f"{tartib}-son kiriting: "))
        lst.append(son ** 2)
    return lst

print(kvadrat())

print("-------------------------------------T8---------------------------------------\n")

def sana(gap: str, kichik = 0, katta = 0):
    for i in range(len(gap)):
        if gap[i].islower():
            kichik += 1
        elif gap[i].isupper():
            katta += 1
    return [katta, kichik]

gap = input("Gap kiritng -> ")
print(sana(gap))

print("-------------------------------------T9---------------------------------------\n")

                                    #yechim-1
def oraliq(a: int, b: int, lst = [] ) -> list:
    if int(m.sqrt(a)) != int(m.sqrt(b)) and a+1 != b:
        for i in range(m.ceil(m.sqrt(a)) , m.ceil(m.sqrt(b))):
            lst.append(i)
        return lst
    return None


boshi = int(input("boshlang'ich son -> "))
ohiri = int(input("ohirgi son -> "))
print(oraliq(boshi, ohiri))


                                    #yechim-2
#def oraliq2(a: int, b: int, lst = [] ) -> list:
#    for i in range(a+1, b):
#        if m.sqrt(i).is_integer():
#            lst.append(int(m.sqrt(i)))
#    return lst if len(lst) != 0 else None
#    
#boshi = int(input("boshi -> "))
#ohiri = int(input("ohiri -> "))
#print(oraliq2(boshi, ohiri))

print("-------------------------------------T10--------------------------------------\n")

def kvadrat_dct(n: int, dct = {}) -> dict:
    dct = {x:x ** 2 for x in range(1, n)}
    return dct 

n = int(input("N = "))
print(kvadrat_dct(n))

print("-------------------------------------T11--------------------------------------\n")

def sum_tuple(lst: list) -> list:
    for i in range(len(lst)):
        lst[i] = sum(lst[i])
    return lst
        
lst_tpl = [(1,2),(2,3),(3,4)]
print(lst_tpl)
print(sum_tuple(lst_tpl))

print("-------------------------------------T12--------------------------------------\n")

def matrix(lst: list) -> list:
    lst = [list(lst[i]) for i in range(len(lst))]
    return lst

lst_tpl = [(1,2),(2,3),(3,4)]
print(matrix(lst_tpl))

print("-------------------------------------T13--------------------------------------\n")

def dictionary(lst1: list, lst2: list, lst3: list, lst = []) -> list:
    for i in range(len(lst1)):
        dct , dct2 = {}, {}
        dct[lst2[i]] = list3[i]
        dct2[lst1[i]] = dct
        lst.append(dct2)
    return lst

list1 = ['S001', 'S002', 'S003', 'S004']
list2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3 = [85, 98, 89, 92]
print(dictionary(list1, list2, list3))

print("-------------------------------------T14--------------------------------------\n")

def dict_sana(soz: str, dct = {}) -> dict:
    for i in soz:
        dct[i] = soz.count(i)
    return dct

soz = input("So'z kiriting -> ")
print(dict_sana(soz))

print("-------------------------------------T15--------------------------------------\n")

def katta_son(lst: list) -> int:
    lst = [str(x) for x in lst]
    son = ''.join(sorted(lst, key=lambda x:x[0:], reverse=True))
    return int(son)

lst = [61, 228, 9]
print(katta_son(lst))

print("-------------------------------------T16--------------------------------------\n")

def kirituvchi(lst: list):
    lst = []
    for i in range(1, int(input("Uzunligini kiriting: "))+ 1):
        vaqtincha = []
        vaqtincha = input(f"{i}-list (Ex: raqam,ism,belgi)-> ").split(",")
        for j in range(3):
            if vaqtincha[j].isdigit():
                vaqtincha[j] = int(vaqtincha[j])
        lst.append(vaqtincha)


def dictionary(lst: list) -> dict:
    dct = dict()
    for i in range(len(lst)):
        son = lst[i].pop(0)
        dct[son] = lst[i]
    return dct



lst = [
    [1, 'Jean Castro', 'V'],
    [2, 'Lula Powell', 'V'],
    [3, 'Brian Howell', 'VI'],
    [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']
       ]
#kirituvchi(lst)
print("Input:\n",lst,"\n")
print("Output:\n",dictionary(lst))

print("-------------------------------------T17--------------------------------------\n")

def juft_int(lst: list) -> list:
    son = int(input("Son -> "))
    while son != 0:
        lst.append(str(son))
        son = int(input("Son -> "))
    lst = [int(i) for i in lst if not int(i[0]) % 2]
    print(*lst)

lst = []
juft_int(lst)

################################################################################
############################  20.12.2022 Amaliyot  #############################

print("-------------------------------------1----------------------------------------\n")

def max_2(lst: list) -> int:
    lst.remove(max(lst))
    return max(lst)

lst = [int(x) for x in input('Listga son kiriting = ').split()]
print("2-max ->",max_2(lst))

print("-------------------------------------2----------------------------------------\n")

def min_2(lst: list) -> int:
    lst.remove(min(lst))
    return min(lst)

lst = [int(x) for x in input('Listga son kiriting = ').split()]
print("2-min ->",min_2(lst))

print("-------------------------------------3----------------------------------------\n")

def sortlash(lst: list) -> list:
    return sorted(lst)

lst = [int(x) for x in input('Listga son kiriting = ').split()]
print(sortlash(lst))

print("-------------------------------------4----------------------------------------\n")

def qaytarilgan(lst: list) -> int:
    son = max(lst, key=lst.count)
    return "({0}, {1}) - {0} soni {1} marta takrorlangan".format(son, lst.count(son))

    
lst = [int(x) for x in input('Listga son kiriting = ').split()]
print(qaytarilgan(lst))

print("-------------------------------------5----------------------------------------\n")

def qaytarilgan(lst: list) -> int:
    son = min(lst, key=lst.count)
    return "({0}, {1}) - {0} soni {1} marta takrorlangan".format(son, lst.count(son))

    
lst = [int(x) for x in input('Listga son kiriting = ').split()]
print(qaytarilgan(lst))

print("-------------------------------------6----------------------------------------\n")

def max_value(dct: dict):
    dct_value = list(dct.values())
    print(max(dct_value))
    
dct = {1:10, 2:20, 3:30, 4:40, 5:50}
max_value(dct)

print("-------------------------------------7----------------------------------------\n")

def max_value(dct: dict):
    dct_key = list(dct.keys())
    print(max(dct_key))
    
dct = {1:10, 2:20, 3:30, 4:40, 5:50}
max_value(dct)

print("-------------------------------------8----------------------------------------\n")

def set_kv(dct: dict, st: list = []) -> set:
    st = set(list(dct.values()) + list(dct.keys())) 
    return st

dct = {1:10, 2:20, 3:30, 4:40, 5:50}
print(set_kv(dct))

print("-------------------------------------9----------------------------------------\n")

def ozgartir(dct: dict, dict_new: dict = {}) -> dict:
    dict_new = {v:k for k, v in dct.items()}
    return dict_new

dct = {1:10, 2:20, 3:30, 4:40, 5:50}
print("Orginal:\n",dct)
print("\nO'zgartirildi:\n",ozgartir(dct))

print("------------------------------------10----------------------------------------\n")

def key_remove(dct: dict, key: str) -> dict:
    while key in dct:
        dct.pop(key)
    return dct

dct = {1:10, 2:20, 3:30, 4:40, 5:50}
print(dct)
key = int(input("Key = "))
print(key_remove(dct, key))

print("------------------------------------11----------------------------------------\n")

def value_0(dct: dict) -> dict:
    dct_new = {x:0 for x in dct}
    return dct_new

dct = {1:10, 2:20, 3:30, 4:40, 5:50}
print("Orginal:\n",dct)
print("\nO'zgardi:\n",value_0(dct))

print("------------------------------------12----------------------------------------\n")

def juft_max(lst: list) -> int:
    while len(lst) != 0:
        son = lst.pop(lst.index(max(lst)))
        if not son % 2:
            return son
    return -1

lst = [int(x) for x in input("listga son kiriting: ").split()]
print(juft_max(lst))

print("------------------------------------13----------------------------------------\n")

def min_value(st: set) -> int:
    return min(st)

set_ = {45, 9, 2, 3, 4, 5, 10}
print("min son ->",min_value(set_))


    #QOLGAN MASALALAR O'TILMAGAN MAVZUDAN BERILGAN