from operador import roll_dice

print('Welcome to Dice Game!')


def main():
    roll_dices()


def roll_dices():

    mtz1, mtz2 = [], []
    win, tie, loss = 0, 0, 0

    dices = int(input('Enter how many dices: '))
    faces = int(input('Enter how many sides (up to 100): '))
    while 0 >= faces > 100:
        faces = int(input('Enter how many sides (up to 100): '))
    rolls = int(input('How many rolls do you want: '))

    for x in range(0, rolls):
        mtz1.append(roll_dice(dices, faces))
        mtz2.append(roll_dice(dices, faces))

        if sum(mtz1[x]) == sum(mtz2[x]):
            tie += 1
        elif sum(mtz1[x]) > sum(mtz2[x]):
            win += 1
        else:
            loss += 1

    if tie == 0:
        print(f'Results: \n Yours: {mtz1} \n Oponent: {mtz2} \n\n'
                f'Times played: {rolls};\n'
                f'The final score was: \n\n'
                f'You win: {win} times ({(win / rolls) * 100:.2f}%).\n'
                f'You tied: {tie} times ({tie}%).\n'
                f'You lost: {loss} times ({(loss / rolls) * 100:.2f}%).')

    else:
        print(f'Results: \n\n Yours: {mtz1} \n Oponent: {mtz2} \n\n'
                f'Times played: {rolls};\n'
                f'The final score was: \n\n'
                f'You win: {win} times ({(win / rolls) * 100:.2f}%).\n'
                f'You tied: {tie} times ({(tie/rolls) * 100:.2f}%).\n'
                f'You lost: {loss} times ({(loss / rolls) * 100:.2f}%).')

    asw = input('\n\nWanna play again? (y/n)')

    if asw == 'y':
        roll_dices()
    else:
        print('\n\nEND GAME')


if __name__ == '__main__':
    main()
