#! usr/bin/env python3
def doc():
    """
    Faça um programa que tenha uma função notas() que pode
    receber várias notas de alunos e vai retornar um dicionário
    com as seguintes informações:
    - Quantidade de notas
    - A maior nota
    - A menor nota
    - A média da turma
    - A situação (opcional)
    - Adicione também as docstrings da função.
    '''
    :return: None
    """


def notas(*nota, status=False):
    """
    --> Função para guardar notas em um dicionário
    :param nota: Nota dos alunos
    :param status: Opcional. True: mostra a situação do aluno
    :return: Retorna um dicionário com notas, maior e menor nota, media e situação (se status == True).
    """
    def boletim():
        ficha = dict()
        ficha["total"] = len(nota)
        ficha["maior"] = max(nota)
        ficha["menor"] = min(nota)
        ficha["media"] = sum(nota) / len(nota)
        return ficha

    dic = boletim()
    if status:

        if dic["media"] <= 6:
            dic["situacao"] = "RUIM"
        elif dic["media"] <= 6.5:
            dic["situacao"] = "RAZOÁVEL"
        else:
            dic["situacao"] = "BOA"
        return dic
    return dic


resp = notas(6, status=False)
print(resp)

