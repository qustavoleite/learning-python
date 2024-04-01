lado_um = float(input())
lado_dois = float(input())
lado_tres = float(input())

if lado_um + lado_dois > lado_tres and lado_um + lado_tres > lado_dois and lado_dois + lado_tres > lado_um:
    if lado_um == lado_dois == lado_tres:
        print("equilátero")
    elif lado_um == lado_dois or lado_um == lado_tres or lado_tres == lado_dois:
        print("isóceles")
    else:
        print('escaleno')
else:
    print("Não é um triângulo válido.")