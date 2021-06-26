pessoas = {'Nome': 'Cleyton', 'Gêreno': 'M', 'Idade':  40}
pessoas['Nome'] = 'Guilherme'
for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['peso'] = '84.0'
for k, v in pessoas.items():
    print(f'{k} = {v}')