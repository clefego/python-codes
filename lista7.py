turma1 = list()
turma2 = list()
totmai = 0
totmen = 0
p = 0
for c in range(0, 3):
    turma1.append(str(input('Nome: ')))
    turma1.append(int(input('Idade: ')))
    turma2.append(turma1[:])
    turma1.clear()
for p in turma2:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')