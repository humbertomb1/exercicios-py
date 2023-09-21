# Calculando aumento de salário em %

salario = float(input('Qual é o salário do funcionário? '))
novoSala = salario + (salario * 15 / 100)
print(f'Um funcionário que ganahva {salario}, com 15% de aumento, passa a receber {novoSala:.2f}')