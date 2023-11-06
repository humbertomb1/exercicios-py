# COMO COLOCAR UM DICIONÁRIO EM ORDEM
importe da library 'operator' a função 'itemgetter':

'from operator import itemgetter'

a estrutura para ordenenar um dicionário:

dicionario = sorted(dicionario.item(), key =itemgetter(1), reverse=True)

no parametro 'key' usamos 0 para ordernar pelas chaves do dicionário e 1 para ordenar pelos valores do dicionário.

Se você não colocar o reverse=True o dicinário ficará ordenado da esquerda para direita
