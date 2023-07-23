import os
os.system("cls")

"""                                     #1-misol
for i in range(1, 11):
    sum = 0
    for j in range(10):
        sum += i
        print(sum, end=" ")
    print()
"""
"""
for i in range(1, 11):
    print("Hozirgi son {} Bita olding son  {} Yigindi = {}".format(i, i-1, i*2-1))
"""
"""
lst = input("Matn kiriting: ").split()
for i in lst:
    if i[0].lower() == "k":
        print(i)
"""
"""
son = int(input("son kiriting: "))
birlik = {0: '', 1: "bir", 2: "ikki", 3: "uch", 4: "to'rt", 5: "besh", 6: "olti", 7: "yetti", 8: "sakkiz", 9: "to'qqiz"}
onlik = {0: '', 1: "o'n", 2: "yigirma", 3: "o'ttiz", 4: "qiriq", 5: "ellik", 6: "oltmish", 7: "yetmish", 8: "sakson", 9: "to'qson"}

if son < 100: 
    bir = birlik.get(son % 10)
    on = onlik.get(son//10)
    print(on ,bir)
    on_sum = len(on)
    bir_summa = len(bir)
    if on.count("sh"):
        on_sum -= 1
    if bir.count("sh") or bir.count("ch"):
        bir_summa -= 1
    print(on_sum + bir_summa, "ta bor")
else:
    print("son katta")
"""
"""
lst = [1,2,4,33,8,45,23,54,6]
print(lst)
son = int(input("Son kiriting: "))

for i in range(len(lst)):
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[i] + lst[j] == son:
            print(f"{i} va {j} - indexlar")
            exit()
print("bunday indexlar yo'q")
"""
"""
import math as m                                #!son faktorial
print(m.factorial(int(input("Istalgan son kiriting: "))))
"""

