try:
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))
    n3 = int(input("Digite o ultimo numero: "))

    if n1 < n2 and n1 < n3: 
        print(n1, "é menor")
    elif n2 < n1 and n2 < n3:
        print(n2, "é menor")
    elif n3 < n1 and n3 < n2:
        print(n3, "é menor")
except ValueError:
    print("Entrada inválida, digite numero")