frase = ' curso de Python '
print(frase[0:15])
print(frase[3:15])
print(frase[:5])
print(frase.count('o'))
print(frase.upper().count('C'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Flutter'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('curso'))
quebra = frase.split()
print(quebra[2][3])
print(quebra[0][3])