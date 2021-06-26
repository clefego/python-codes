turma1 = list()
turma2 = list()
for c in range(0, 3):
    turma1.append(str(input('Nome: ')))
    turma1.append(str(input('Idade: ')))
    turma2.append(turma1[:])
    turma1.clear()
print(turma2)