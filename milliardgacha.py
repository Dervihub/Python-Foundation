# Kiritilgan sonni o'zbek tilida o'qiydigan dastur tuzing.
# 1 dan 1000000000 gacha

birlik = {0: '', 1: 'bir', 2: 'ikki', 3: 'uch', 4: "to'rt", 5: 'besh', 6: 'olti', 7:'yetti', 8: 'sakkiz', 9: "to'qqiz"}

onlik = {0: '', 1: "o'n", 2: 'yigirma', 3: "o'ttiz", 4: 'qirq', 5: 'ellik', 6:'oltmish', 7: 'yetmish', 8: 'sakson', 9: "to'qson"}

yuzlik = {0: '', 1: 'yuz', 2: 'ming', 3: 'million', 4: 'milliard'}

son = list()

while True:
    a = int(input('Son kiriting -> '))
    if not(0 < a and a < 1_000_000_000_000):
        print('Imkoniyatimiz cheklangan \n')
    else:
        break

x, n = 1, 0
while a // x != 0:
    y = a//x % 10
    if n == 0:
        son.append(birlik.get(y)); n += 1
    elif n == 1 or n == 5 or n == 9 or n == 13:
        son.append(onlik.get(y)); n += 1
    elif n == 2 or n == 6 or n == 10 or n == 14:
        if y != 0: son.append(birlik.get(y) +' '+ yuzlik.get(1))
        else: son.append(birlik.get(y))
        n += 1
    elif n == 3:
        son.append(yuzlik.get(2))
        son.append(birlik.get(y))
        n += 2
    elif n == 7:
        if son[n-1] == '' and son[n-2] == '' and son[n-3]: son[n-4] = ''
        son.append(yuzlik.get(3))
        son.append(birlik.get(y))
        n += 2
    elif n == 11:
        if son[n-1] == '' and son[n-2] == '' and son[n-3]: son[n-4] = ''
        son.append(yuzlik.get(4))
        son.append(birlik.get(y))
        n += 2
    x *= 10

while True:
    if '' in son:
        son.remove('')
    else: break
son.reverse()
natija = ' '.join(son)

istisno = ['sh', 'ch', 'ng', "o'"]
n = 0
for i in range(len(natija) -1):
    if (natija[i] + natija[i+1] in istisno) or natija[i] == ' ':
        continue
    n += 1
n += 1

print('\"{0}\" da {1} ta harf bor'.format(natija, n))