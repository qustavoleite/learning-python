caractere = input('Digite um caractere: ')
caractere = caractere.lower()

if caractere in 'aeiou':
    print(caractere, "é vogal")
else:
    print(caractere, 'é consoante')