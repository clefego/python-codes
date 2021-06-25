nome = str(input('Qual é o seu nome? '))
if nome == 'Cleyton':
    print('O seu sobrenome é Ferreira Gonçalves')
elif nome == 'Guilherme' or nome == 'João Gabriel' or nome == 'Manuela':
    print('O seu sobrenome é Borges')
else: 
    print('Não sei o seu sobrenome')
print('Tenham um Bom dia, {}'.format(nome))