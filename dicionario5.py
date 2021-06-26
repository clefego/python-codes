Estado = dict()
Brasil = list()
for c in range(0, 3):
    Estado['UF'] = str(input('Unidade Federativa: '))
    Estado['Sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(Estado.copy())
for e in Brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in Brasil:
    for v in e.values():
        print(v, end=' ')
    print()