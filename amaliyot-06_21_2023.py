import math
"""                                                  #1-misol
j = 0
for i in range(100, 1000):
    i = str(i)
    if i.count(i[j]) == 2:
        print(i)
    elif i.count(i[j+1]) == 2:
        print(i)
"""
"""                                                 #2-misol
a = int(input("Yozing: "))
while a != 0:
    hona = int(math.log10(a))
    print(a // (10 ** hona), end=" ")
    a = int(a % (10 ** hona))
"""
"""                                                  #3-misol
a = list(map(int, input("Son kiriting: ").split()))
for i in a:
    orginal = i
    while i > 9:
        i //= 10
    if not i % 2:
        print(orginal, end="") 
"""
"""                                                #5-masala
a = list(map(int, input("Son kiriting: ").split()))
maximum = max(a)
minimum = min(a)

son_max = 0
for i in range(minimum, maximum+1):
    if not a.count(i):
        son_max += i
print(son_max)
"""
"""                                                #6-masala
a = list(map(int, input("Son kiriting: ").split()))
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if int(math.log10(a[i])) > int(math.log10(a[i+1])):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
print(a)
"""