# Programa para calcular desconto de 5%

preço = float(input('Qual é o preço do produto? '))
novoPreço = preço - (preço * 5 / 100)

print(f'O produto que custava R${preço}, na promoção de 5% vai custar R${novoPreço:.2f}')