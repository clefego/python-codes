teste = list()
teste.append('Cleyton')
teste.append(40)
turma = list()
turma.append(teste[:])
teste[0] = 'Lianne'
teste[1] = 22
turma.append(teste[:])
print(turma)
print(turma[0])
print(turma[0][0])
print(turma[0][1])