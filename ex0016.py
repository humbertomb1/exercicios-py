# Calculando hipotenusa com a biblioteca math
import math
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
hipo = math.hypot(co, ca)
print(f'Com o cateto oposto sendo {math.trunc(co)} e o cateto adjacente sendo {math.trunc(ca)} a hipotenusa será de {hipo:.2f}')