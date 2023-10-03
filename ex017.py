# Calculando seno, coseno e tangente
import math
ang = float(input('Digite o angulo que você deseja '))
seno = math.sin(math.radians(ang))
cossen = math.cos(math.radians(ang))
tangen = math.tan(math.radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
print(f'O ângulo de {ang} tem o CONSSENO de {cossen:.2f}')
print(f'O ângulo de {ang} tem a TANGENTE de {tangen:.2f} ')