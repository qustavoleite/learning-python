try:
    numero = float(input("Digite um número: "))
    if numero < 0:
        print('O número é negativo')
    elif numero > 0:
        print('O número é positivo')
    else:
        print('O número é zero')
except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")