import os
os.system("cls")
"""
#--------------------------------------------N8-----------------------------------------

def kattala(string: str) -> str:
    string = list(string)
    for i in range(round(len(string)/2), len(string)):
        string[i] = string[i].upper()
    return ''.join(string)

str = input("So'z kiriting: ")
print(kattala(str))

#--------------------------------------------N9------------------------------------------

def capital(string: str) -> str:
    string = string[-1::-1].title()
    katta = list(string[-1::-1].title())
    string = list(string[-1::-1])

    for i in range(len(katta)):
        if katta[i].islower() and string[i].isupper():
                katta[i] = string[i]
    return ''.join(katta)

str = input("So'z kiriting: ")
print(capital(str))
"""
#--------------------------------------------N10-----------------------------------------

def qaytarilgan(str1: str, str2: str) -> list:
    str1, str2 = set(str1), set(str2)
    return list(str1.intersection(str2))

str1 = "abcd"
str2 = "asdf"
print(qaytarilgan(str1, str2))

#--------------------------------------------N11-----------------------------------------
