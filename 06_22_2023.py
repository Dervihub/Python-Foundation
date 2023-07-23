#--------------------------------------------------K1-----------------------------------------------
"""
arr = list()
maximum = 0
for i in range(4):
    matrix = []
    print(f"{i+1}-ustun")
    for j in range(4):
        matrix.append(int(input(f"\t{j+1}-qator -> ")))
    maximum += sum(matrix)
    arr.append(matrix)

for i in range(4):
    for j in range(4):
        print(arr[i][j], end=",")
    print()
print()
print("summasi =",maximum)
"""
#----------------------------------------------------K2---------------------------------------------
"""
arr = list()
for i in range(3):
    matrix = []
    print(f"{i+1}-ustun")
    for j in range(4):
        matrix.append(int(input(f"\t{j+1}-qator -> ")))
    arr.append(matrix)

for i in range(3):
    for j in range(4):
        if j % 2:
            print(arr[i][j], end="")
"""
#----------------------------------------------------K3---------------------------------------------
"""
import random
arr = list()
for i in range(7):              #random son o'tilmagan
    matrix = []
    for j in range(4):
        a = random.randrange(100)
        matrix.append(a)
    arr.append(matrix)
print(arr,"\n")

for i in range(7):
    if not i % 2:
        print()
    for j in range(4):
        if not i % 2:
            print(arr[i][j], end=", ")         
"""
#----------------------------------------------------K4--------------------------------------------
"""
uzunligi = int(input("Uzunligi NxN: "))
arr = list()
for i in range(uzunligi):
    yordamchi = []
    print(f"{i+1}-ustun")
    for j in range(uzunligi):
        yordamchi.append(int(input(f"\t{j+1}-qator -> ")))
    arr.append(yordamchi)
print()
for i in range(uzunligi):
    for j in range(uzunligi):
        print(arr[j][i], end=" ")
    print()
"""
#----------------------------------------------------Q12--------------------------------------------
"""
a = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
son = 0

for i in a:
    i = str(i)
    if i[0] == '-':
        if i[1:].isdigit():
            son += 1
    if i.isdigit():
        son += 1
print(son, "ta")
"""
#----------------------------------------------------Q13--------------------------------------------
"""
a = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
sonlar = list()

for i in a:
    i = str(i)
    if i[0] == '-':
        if i[1:].isdigit():
            sonlar.append(int(i))
    elif i.isdigit():
        sonlar.append(int(i))
print(sonlar)
print("max =", max(sonlar))
"""
#----------------------------------------------------Q14--------------------------------------------
"""
arr = list(map(int, input("Ex(1,2,3): ").split(",")))
for i in range(len(arr)-1 , -1, -1):            #CHala
    if arr[i] == 9:
        arr[i] = 0
        if i == 0:
            arr.insert(0, 1)
    else:
        arr[i] += 1
        break
print(arr)
"""     
#----------------------------------------------------Q15--------------------------------------------
"""
arr = list(map(int, input("Ex(1,2,3): ").split(",")))
print(arr)
for i in range(1, len(arr)):
    if arr[i-1] < arr[i]:
        if i == len(arr)-1:    
            print("o'sish")
            exit()
    else:
        break
    
for i in range(1, len(arr)):
    if arr[i-1] > arr[i]:
        if i == len(arr)-1:    
            print("kamayish")
            exit()
    else:
        break

print("tartibsiz")
"""
#----------------------------------------------------Q16--------------------------------------------
"""
lst = [(),(),("",),('a','b'),('a','b','c'),('d')]
i = 0
while i < len(lst):
    if len(lst[i]) == 0:
        lst.remove(lst[i])
        i -= 1
    i += 1
print(lst)
"""
#########################################################################################################
########################################## 03.11.2022 Amaliyot ##########################################

"""                                         #1-masala
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
print(lst)
lst.reverse()
for i in lst:
    if lst.count(i) > 1:
        temp = lst.count(i)-1
        while temp:
            lst.remove(i)
            temp -= 1
lst.reverse()
print(lst)
"""
"""                                         #2-masala
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
target = int(input("Target -> "))
lst_len = len(lst)
for i in range(lst_len):
    for j in range(lst_len):
        if i == j:
            continue
        if lst[i] + lst[j] == target:
            print(f"[{i}, {j}]")
            exit()
print(" Listdagi ikki son topilmadi")
"""
"""                                         #3-masala
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
target = int(input("topmoqchi bo'lgan son: "))

lst_len = len(lst)
if lst[-1] < target:
    print(f"{lst_len}-index")
elif lst[0] > target:
    print("0-index")
else:
    for i in lst:
        if i >= target:
            print(f"{lst.index(i)}-index")
            break
"""
#########################################################################################################
################################################ List Masala ############################################

#-------------------------------------------------1-misol------------------------------------------------
"""
print("\t" *5,"1-masala")
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
print(sorted(lst)[-2])
"""
#-------------------------------------------------2-misol------------------------------------------------
"""
print("\t" *5,"2-masala")
tpl = tuple(map(int, input("Ex(1,2,3): ").split(",")))
print(sorted(tpl)[1])
"""
#-------------------------------------------------3-misol------------------------------------------------
"""
print("\t" *5,"3-masala")
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
lst.sort(reverse=True)
print(lst)
"""
#-------------------------------------------------4-misol------------------------------------------------
"""
print("\t" *5,"4-masala")
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
max_takror = 0
for i in lst:
    if max_takror < lst.count(i):
        max_takror = lst.count(i)
        son = i
print(son)    
"""
#-------------------------------------------------5-misol------------------------------------------------
"""
print("\t" *5,"5-masala")
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
min_takror = lst.count(lst[0])
son = lst[0]

for i in lst:
    if min_takror > lst.count(i):
        min_takror = lst.count(i)
        son = i
print(son)    
"""
#-------------------------------------------------6-misol------------------------------------------------
"""
print("\t" *5,"6-masala")
lst = list(map(int, input("Ex(1,2,3): ").split(",")))
juft = list()
for i in lst:
    if not i % 2:
        juft.append(i)
if juft:
    print(max(juft))
else:
    print(-1)
"""
#-------------------------------------------------7-misol------------------------------------------------
"""
print("\t" *5,"7-masala")
lst = list(map(int, input("Ex(1,2,3): ").split(",")))

lst.sort()
musbat = 0
for i in lst:
    if i > -1:
        musbat += 1
print(lst[:musbat-1]+ lst[-1:-musbat:-1])
"""
#-------------------------------------------------8-misol------------------------------------------------
"""
print("\t" *5,"8-masala")
lst = [1, True, "Salom", [1, 2, 3], "Nimadur", 44, 3.14]
son = 0
for i in lst:
    i = str(i)
    if i.isdigit():
        son += 1
print(son, "ta son int") 
"""
#-------------------------------------------------9-misol------------------------------------------------
"""
print("\t" *5,"9-masala")
lst = [1, True, "Salom", [1, 2, 3], "Nimadur", 44, 3.14]

for i in lst:
    if type(i) == bool:
        continue
    i = str(i)
    if i[0].isupper():
        print(i, end="  ")
"""
#------------------------------------------------10-misol------------------------------------------------
"""
print("\t" *5,"10-masala")
lst = [1, True, "Salom", [1, 2, 3], "Nimadur", 44, 3.14]
for i in range(len(lst)):
    lst[i] = type(lst[i])
print(lst)
"""
#------------------------------------------------11-misol------------------------------------------------
"""
print("\t" *5,"11-masala")
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list2.sort(reverse=True)
for i in range(len(list1)):
    print(list1[i], list2[i])
"""
#------------------------------------------------12-misol------------------------------------------------
"""
print("\t" *5,"12-masala")
lst = list(map(str, input("Ex(a,b,c): ").split(",")))
harflar = list()
for i in lst:
    if i.islower():
        harflar.append(i)
for i in lst:
    if i.isupper():
        harflar.append(i)
print(harflar)
"""
#------------------------------------------------13-misol------------------------------------------------
"""
print("\t" *5,"13-masala")
lst = [[1,2,3],[9,1,5],[1,8,7]]
d1 = d2 = 0
for i in range(3):
    for j in range(3):
        print(lst[i][j], end=" ")
        if i == j:
            d1 += lst[i][j]
        if i+j == 2:
            d2 += lst[i][j]
    print()    
print(f"farqi {d1} - {d2} = {d1-d2}")
"""
#------------------------------------------------14-misol------------------------------------------------
"""
print("\t" *5,"14-masala")
matn = input("Matn kiriting: ")
lst = matn.split()
for i in range(len(lst)):
    for a in lst[i]:
        if a.isdigit():
            print(lst[i], end=" ")
            break
"""
#------------------------------------------------15-misol------------------------------------------------
"""
print("\t" *5,"15-masala")
matn = input("Matn kiriting: ")
matn = matn.replace(',',' ').replace('.',' ').replace('?',' ').replace('!',' ').split()
for i in matn:
    if len(i) <= 5:
        print(i, end="  ")
"""
#------------------------------------------------16-misol------------------------------------------------
"""
print("\t" *5,"16-masala")
matn = input("Matn kiriting: ")
matn = matn.replace(',',' ').replace('.',' ').replace('?',' ').replace('!',' ').split()
for i in matn:
    if i.istitle():
        print(i, end="  ")
"""
#------------------------------------------------17-misol------------------------------------------------
"""
print("\t" *5,"17-masala")
lstuple = [(1,4,3), (3,2), (2,0,1), (1,3,2)]
for j in range(2):
    for i in range(1, len(lstuple)):
        if lstuple[i-1][1] > lstuple[i][1]:
            temp = lstuple[i-1]
            lstuple[i-1] = lstuple[i]
            lstuple[i] = temp
print(lstuple)
"""
#------------------------------------------------18-misol------------------------------------------------
"""
print("\t" *5,"18-masala")
lst = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

max_max = max(lst[0])
for i in lst:
    if max_max < max(i):
        max_max = max(i)
        saqla = i
print(saqla)
"""
#------------------------------------------------19-misol------------------------------------------------
"""
print("\t" *5,"19-masala")
lst = ["A","B","C","D","E","F","G","L","Q","U"]

print(lst)
son = int(input("son -> "))
new_lst = list()
i = 0

while i != len(lst):
    list2 = []
    list2.append(lst[i])
    i += 1
    while i % son:
        if i >= len(lst):
            break
        list2.append(lst[i])
        i += 1
    new_lst.append(list2)
print(new_lst)
"""
#------------------------------------------------20-misol------------------------------------------------
"""
print("\t" *5,"20-masala")
matn = input("Matn kiriting: ")
step = int(input("Qadam -> "))
print(matn[::step])
"""
#------------------------------------------------21-misol------------------------------------------------
"""
print("\t" *5,"21-masala")
son = input("Raqam -> ")

raqam = ""
for i in range(len(son)):
    if i % 2:
        raqam += son[i]
print(f"Javob: {int(raqam) / 10}")
"""
#------------------------------------------------22-misol------------------------------------------------
"""
print("\t" *5,"22-masala")
string = list(input("So'z yoki raqam -> "))
teskari = string.copy()
teskari.reverse()
print("Palindrome" if string == teskari else "Not palindrome")
"""
#------------------------------------------------23-misol------------------------------------------------
"""
print("\t" *5,"23-masala")
son = input("Raqam -> ")
print(son[-1::-1])
"""