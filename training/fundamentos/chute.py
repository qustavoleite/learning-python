# escreve um programa que ao iniciar gere um numerto de 1 ate 10 e epermita o usuario chutar um numero ate o numero aleatorio ser acertado, o programa deve informar se o chute foi acima ou abaixo ou igual o numero gerado
 
import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int(input('chute valores de 1 ate 10:'))
    if chute > valor_aleatorio:
        print('Chute acima do valor aleatorio')
    elif chute < valor_aleatorio:
        print('chute abaixo do valor aleatorio')
    elif chute == valor_aleatorio:
        acertou = True
        print('voce acertou')