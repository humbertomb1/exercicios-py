# Programa para calcular preço a pagar por carro alugado com base no KM e dias alugado
diasQant = int(input('Quantos dias de alugado? ')) # input dias rodados
kmPer = float(input('Quantos KM rodados? ')) #input Km rodados
preço = kmPer * 0.15 + diasQant * 60

print(f'O total a pagar é de {preço}')

 