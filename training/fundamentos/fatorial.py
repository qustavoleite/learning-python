# crie um programa que receba um numero e imprima o fatorial daquele numero

numero = int(input('Digite um numero: '))
if numero > 0:
    fatorial = 1
    for item in range(1, numero + 1):
        fatorial *= item
    print('o fatorial de', numero, 'é', fatorial)
else:
    print('Digite um numero positivo')