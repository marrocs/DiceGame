'''Operador do jogo

Deve receber os lados dos dados e quantos dados jogar;
Deve retornar uma lista com os resultados dos dados.'''
import random


def roll_dice(dices, faces) -> list:

    result = []
    cont = 0

    while cont < dices:
        result.append(random.randint(1, faces))
        cont += 1

    return result
