def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} corresponde a {s}')    

soma(6, 3)
soma(4, 7, 5)