import math, random
#from math import sqrt, floor
num1 = int(input('Digite um número: '))
raiz = math.sqrt(num1)
print('A raiz de {} é igual a {}'.format(num1, raiz))
print('A raiz de {} é igual a {}'.format(num1, math.ceil(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num1, math.floor(raiz)))
num2 = random.randint (1, raiz)
print('O valor de Random é {}'.format(num2))