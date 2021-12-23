import random
import operador

print('Welcome to Dice Game!')    # Initiating game
acao = input('Press anything to start: ')

if acao is not False:
    num1, num2 = [], []
    mtz1, mtz2 = [], []
    vit = 0
    emp = 0
    der = 0

    dices = int(input('Enter how many dices: '))
    faces = int(input('Enter how many sides (up to 100): '))
    while 0 >= faces > 100:
        faces = int(input('Enter how many sides (up to 100): '))
    rolls = int(input('How many rolls do you want: '))

    for x in range(0, rolls):
        num1.append(operador.roll_dice(dices, faces))
        num2.append(operador.roll_dice(dices, faces))

        lst1 = [i[0] for i in num1]    # thanks, stackoverflow stranger
        lst2 = [i[0] for i in num2]    # Problems here...

        # Comparando e adicionando ao placar # problemas aqui
        if sum(lst1) > sum(lst2):
            vit += 1
        elif sum(lst1) == sum(lst2):
            emp += 1
        else:
            der += 1

    if emp == 0:
        print(f'Os Jogos foram: \n seu: {num1} \n oponente: {num2} \n\n'
                f'O placar final foi: \n\n'
                f'Vezes jogadas: {rolls};\n'
                f'Vitórias: {vit} vezes ({(vit/rolls)*100:.2f}% das vezes).\n'
                f'Empates: {emp} vezes ({emp}% das vezes jogadas).\n'
                f'Derrotas: {der} vezes ({(der/rolls)*100:.2f}% das vezes jogadas).')

    else:
        print(f'Os Jogos foram: \n {num1} \n {num2} \n\n'
                f'O placar final foi: \n\n'
                f'Vezes jogadas: {rolls};\n'
                f'Vitórias: {vit} ({(vit / rolls) * 100:.2f}% das vezes jogadas).\n'
                f'Empates: {emp} ({(emp / rolls)*100:.2f}% das vezes jogadas).\n'
                f'Derrotas: {der} ({(der / rolls)*100:.2f}% das vezes jogadas).')


print('\n\nFIM DE JOGO.')
