import os
os.system("cls")

#--------------------------------------------Q1--------------------------------------------
"""
print("\t\t\t\t Q1")
lst = [True, "Salom", 5, 5.6]

for i in range(len(lst)):
    lst[i] = type(lst[i])
print(lst)
"""
#---------------------------------------------Q2-------------------------------------------
"""
print("\t"*4, "Q2")
lst = [
        [2, 15, 4],
        [19, 24, 11],
        [7, 9, 5],
        [10, 3, 1]
    ]

for i in range(4):
    lst[i][1] *= lst[i][1]
print(lst)
"""
#---------------------------------------------Q3-------------------------------------------
"""
print("\t"*4, "Q3")
lst = [7, 8, 1, 3, 4, 6, 7, 5]

for i in range(len(lst)):
    if i % 2:
        lst[i] **= 3
    else:
        lst[i] **=  2
print(lst)
"""
#---------------------------------------------Q4-------------------------------------------
"""
print("\t"*4, "Q4")
lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]

for i in range(lst.count(0)):
    lst.remove(0)
    lst.insert(len(lst)+1, 0)
print(lst)
"""
#---------------------------------------------Q5-------------------------------------------
"""
print("\t"*4, "Q5")
numbers = (5, -3, 4, -2, 1, -9, 8, -6, 7, 0, 4)
print(numbers)
son = int(input("Son kiriting: "))
list_numbers = list(numbers)

if son in numbers:
    for i in range(list_numbers.count(son)):
        list_numbers.remove(son)
numbers = tuple(list_numbers)
print(numbers)
"""
#---------------------------------------------Q6-------------------------------------------
"""
print("\t"*4, "Q6")
number = [
    [5, 3, 7],
    [1, 4, 9],
    [2, 8, 6]
]
maximum = 0
for i in range(len(number)):
    if maximum < sum(number[i]):
        maximum = sum(number[i])
print(f"Max qator sum = {maximum}")

number.clear()
"""
#---------------------------------------------Q7-------------------------------------------
"""
print("\t"*4, "Q7")
number1 = [2, -1, 5, -3, 8, -4, 6, 7, 9]
number2 = [1, 6, 7, -3, -9, -4, -5]

orqaga = 0
for i in range(len(number2)):
    if not number1.count(number2[i-orqaga]):
        number2.remove(number2[i-orqaga])
        orqaga += 1
print(number2)

number1.clear()
number2.clear()
"""
#---------------------------------------------Q8-------------------------------------------
"""
print("\t"*4, "Q8")
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
#---------------------------------------------Q9-------------------------------------------
print("\t"*4, "Q9")
number = []

uzunlik = int(input("Listni uzunligi: "))

for i in range(uzunlik):
    number.append(int(input(f"{i}-index -> ")))
number.remove(max(number))
print("2-max son",max(number))

number.clear()
#---------------------------------------------Q10-------------------------------------------
print("\t"*4, "Q10")
number = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]

for i in range(len(number)):
    if len(number) <= i:
        break
    had = 0
    for j in range(i+1-had, len(number)-had-1):
        if number[i] == number[j]:
            had += 1
            number.pop(j)
print(number)
#---------------------------------------------Q11-------------------------------------------
print("\t"*4, "Q11")
sample_list = [11, 33, 50]

son = ""
for i in range(len(sample_list)):
    son += str(sample_list[i])
print(int(son))
#---------------------------------------------Q12-------------------------------------------
print("\t"*4, "Q12")
number1 = [1, 1, 3, 4, 4, 5, 6, 7]
number2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
orta_arifmetigi = (sum(number1) + sum(number2)) / (len(number1) + len(number2))
print("O'rta arifmategi ->", orta_arifmetigi)
"""