for numero in range(1, 11):
    print(numero)

nomes = ['jhon', 'roberto', 'henrique']
for nome in nomes:
    print(nome)

# imprima os valores de 1 a N

numero_maximo = int(input('Digite um numero:'))
valor_inicial = 1
for numero in range(valor_inicial, numero_maximo + 1):
    print(numero)


precos = [10, 20, 30]
print(precos[2])
print(precos.index(10))

diversidades = {20, True, "Rosa", 76.5}
for item in diversidades:
    print(item)


# Dados a uma coleção de idades [15, 46, 75, 34, 23], imprima na tela a soma desses valores 
    
idades = [15, 46, 75, 34, 23]
total = 0

for idade in idades:
    total += idade
print(total)