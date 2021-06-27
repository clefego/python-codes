def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')    

contador(3, 12, 3)