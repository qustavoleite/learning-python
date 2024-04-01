try:
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        print("é par")
    else:
        print("é impar")
except ValueError:
    print("Entrada inválida. Por favor, insira apenas números.")