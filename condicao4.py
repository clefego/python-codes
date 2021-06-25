nome = str(input('Qual é o seu nome? '))
if nome == 'Cleyton':
    print('O seu sobrenome é Ferreira Gonçalves')
elif nome == 'Guilherme' or nome == 'João Gabriel' or nome == 'Manuela':
    print('O seu sobrenome é Borges')
elif nome in 'Lianne, Aline e Lorena':
    print('Você é filha de Antonio Maciel e Mary Anne Maciel ')
else: 
    print('Não sei o seu sobrenome')
print('Tenham um Bom dia, {}'.format(nome))