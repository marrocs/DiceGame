'''Operador do jogo

Deve receber os lados dos dados e quantos dados jogar;
Deve retornar uma lista com os resultados dos dados.'''
import random


def roll_dice(dices, faces) -> list:

    res = []
    cont = 0

    while cont != dices:
        result = random.randint(1, faces)
        res.append(result)
        cont += 1

    cont = 0

    soma = sum(res)

    return res

