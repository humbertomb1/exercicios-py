# Convertendo distancia em metros para outras medidas
metro = float(input('Digite a distância em metros: '))
km = metro / 1000
hm = metro / 100
am = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'A distanância de {metro}m corresponde a ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{am}am')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')