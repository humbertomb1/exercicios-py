#! /usr/bin/env python3
'''
Programa para criar vários arquivos
'''
import json

arq_json = open("/home/humberto/Documentos/exercicios-python/data.json")

data = json.load(arq_json)

ultimo = data["ultimo"]

num_arquivo = ultimo

arq_json.close()

print('~='*10)
print('CRIADOR DE ARQUIVOS')
print('~='*10, '\n')


#tipo = input('Que tipo de arquivo você quer criar? ')

fim = int(input('Quantos arquivos você quer criar? '))


inicio = 0

while inicio < fim:
    if num_arquivo >= 100:
        arquivo = open(f'ex{num_arquivo}.py', "x")
    elif num_arquivo < 100:
        arquivo = open(f'ex0{num_arquivo}.py', "x") # Criando arquivo
    arquivo.write('#! /usr/bin/env python3') #Escrevendo shebang no arquivo
    inicio += 1
    num_arquivo += 1

data["ultimo"] = num_arquivo # Jogando último número do arquivo dentro de 'data'
 
arq_json = open("data.json", "w") #Abrindo o arquivo data.json em modo write

json.dump(data, arq_json) #jogando data dentro do arquivo data.json

arq_json.close()

print('FIM!')
print(f'Foram criados {fim} arquivos')