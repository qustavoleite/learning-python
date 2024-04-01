idade = int(input("Digite sua idade: "))

if idade <= 12:
    print('criança')
elif idade >= 13 and idade <= 19:
    print('adolescente')
elif idade >= 20 and idade <=59:
    print('adulto')
else:
    print('idoso')