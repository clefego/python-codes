Estado = dict()
Brasil = list()
for c in range(0, 3):
    Estado['UF'] = str(input('Unidade Federativa: '))
    Estado['Sigla'] = str(input('Sigla do Estado: '))
    Brasil.append(Estado)
print(Brasil)