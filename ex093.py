#! usr/bin/env python3
'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os(com a idade) em um dicionário se por acaso
a CTPS for diferente de ZERO, o dicionário receberá também
o ano de contratação e o salário. Calcule e acrescente
além da idade, com quantos anos a pessoa vai se aposentar.
(apoesentadoria com 35 anos de contribuição)
'''
from datetime import date


hoje = date.today()
hoje = int(hoje.strftime('%Y'))

ficha = {
        'nome': '',
        'idade': '',
        'carteira': '',
        'salario': '',
        'contrato': '',
        'aposentadoria': '',
        

}

nome = str(input('Nome: '))
ficha['nome'] = nome

idade = int(input('Ano de nascimento: '))
ficha['idade'] = hoje - idade

carteira = int(input('Carteira de trabalho (0 não tem): '))


if carteira == 0:
    print(f'- O nome tem valor {ficha["nome"]}')
    print(f"- idade tem valor {ficha['idade']}")
    print("- CTPS tem valor 0")
else:
    contrato = int(input('Ano de contratação: '))
    ficha['contrato'] = contrato

    salario = float(input('Salário R$: '))
    ficha['salario'] = salario

    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contrato'] +35) - hoje)

    print(f'- Nome tem valor {ficha["nome"]}')
    print(f"- Idade tem valor {ficha['idade']}")
    print(f"- CTPS tem valor {ficha['carteira']}")
    print(f"- Contratação tem valor {ficha['contrato']}")
    print(f"- Salário tem valor {ficha['salario']}")
    print(f"- Aposentadoria tem valor {ficha['aposentadoria']}")

