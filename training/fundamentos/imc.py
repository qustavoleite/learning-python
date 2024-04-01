altura = float(input("Digite sua altura em centímetros: ")) / 100 
peso = float(input("Digite seu peso em quilogramas: "))
imc = peso / (altura ** 2)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print("Abaixo do peso (Magro)")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 25 <= imc <= 29.9:
    print("Sobrepeso")
elif 30 <= imc <= 34.9:
    print("Obesidade Grau I")
elif 35 <= imc <= 39.9:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III (Mórbida)")