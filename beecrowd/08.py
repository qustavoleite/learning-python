numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())
salario = valor_hora * horas_trabalhadas

print("NUMBER =", numero_funcionario)
print('SALARY = U$ {:.2f}'.format(salario))