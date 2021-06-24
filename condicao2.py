n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Você foi aprovado! Parabéns!')
else:
    print('Você foi reprovado!' 'Tente novamente!') 

print ('Parabéns!' if m>=6 else 'Tente novamente!') 