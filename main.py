import random
from turtledemo.nim import randomrow

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]


turn = random.choice('X0')

def render():
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                print(board[i][j], end='')
                if j == 0:
                    print(' | ', end='')
                if j == 1:
                    print(' | ', end='')
            print()
            if i != 2:
                print('_________')



def end_game():
    global winner
    print(f'Winer {turn}')
    render()
    winner = True

words_numbers = {
    'upper': 0,
    'center': 1,
    'lower': 2,
    'left': 0,
    'right': 2,
 }

winner = False

for round in range(9):
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    print('next Run')
    print(f'Run: {turn}')
    render()

    try:
        inp_str = input('Ввди назву рядка та стовбця в один рядок через пробіл '
          '\nЗначення для радків: [Upper|Center|Lower]'
          '\nЗначення для стовбців: [Left|Center|Right]>>>').lower()
        coords = inp_str.split()
        row = words_numbers[coords[0]]
        col = words_numbers[coords[1]]

        if board[row][col] == ' ':
            board[row][col] = turn
        else:
            print('Комірка зайнята.Введи інші номери')


    except Exception as e:
        print('!!!!!!!!!!Введено невірне значеня Хід перейшов наступному')


    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' ':
        end_game()
        break

    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' ':
        end_game()
        break

    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' ':
        end_game()
        break

    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ':
        end_game()
        break

    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ':
        end_game()
        break

    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' ':
        end_game()
        break

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        end_game()
        break

    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != ' ':
        end_game()
        break

if not winner:
    print('нічия')