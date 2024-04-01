velocidade = int(input('Digite sua velocidade: '))
velocidade_max = 80

if velocidade <= velocidade_max: 
    print('não houve multa')
elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
    print('levou multa leve')
elif velocidade > velocidade_max + 11 and velocidade <= velocidade_max + 20:
    print('levou multa grave')
elif velocidade > velocidade_max + 20:
    print('levou multa gravissima')