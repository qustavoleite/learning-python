nome_vendedor = input("")
salario_fixo = float(input())
total_vendas = float(input())
salario_bonus = (total_vendas * 0.15) + salario_fixo
print('TOTAL = R$ {:.2f}'.format(salario_bonus))