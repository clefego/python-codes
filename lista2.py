num  = [2, 5, 9, 1]
print(num)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei número 4')
print(num)
print(f'Essa lista tem {len(num)} elemento')