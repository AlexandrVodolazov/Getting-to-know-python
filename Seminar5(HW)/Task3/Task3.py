# Создайте программу для игры в ""Крестики-нолики"".

import random

def print_map(game_board):
    print('Playing field and cell numbering:')
    print(f'1:{game_board[0]}\t 2:{game_board[1]}\t 3:{game_board[2]}\t')
    print(f'4:{game_board[3]}\t 5:{game_board[4]}\t 6:{game_board[5]}\t')
    print(f'7:{game_board[6]}\t 8:{game_board[7]}\t 9:{game_board[8]}\t')
    print()
    print('Player 1 plays X')
    print('Player 2 plays 0')
    print()

def check_win(game_board):
    winner = ''
    if  (game_board[0] != '') and (game_board[0] == game_board[1] == game_board[2]): winner = game_board[0]
    if  (game_board[3] != '') and (game_board[3] == game_board[4] == game_board[5]): winner = game_board[3]
    if  (game_board[6] != '') and (game_board[6] == game_board[7] == game_board[8]): winner = game_board[6]
    if  (game_board[0] != '') and (game_board[0] == game_board[3] == game_board[6]): winner = game_board[0]
    if  (game_board[1] != '') and (game_board[1] == game_board[4] == game_board[7]): winner = game_board[1]
    if  (game_board[2] != '') and (game_board[2] == game_board[5] == game_board[8]): winner = game_board[2]
    if  (game_board[0] != '') and (game_board[0] == game_board[4] == game_board[8]): winner = game_board[0]
    if  (game_board[1] != '') and (game_board[2] == game_board[4] == game_board[6]): winner = game_board[2]
    if winner == 'X':
        print_map(game_board)
        print(f'Game over. Player number 1 wins!')
        return True;
    elif winner == '0':
        print_map(game_board)
        print(f'Game over. Player number 2 wins!')
        return True;
    else:
        return False

print("Tic-Tac-Toe")
active_player = random.randint(1, 2)
signs_player = {1: 'X', 2: '0'}

game_active = True;
game_board = ['', '', '', '', '', '', '', '', '']

while game_active:
    if active_player == 1: active_player = 2
    else: active_player = 1
    print_map(game_board)
    game_turn = int(input(f'player number {active_player} make a move: '))
    if game_turn > 0 and game_turn < 10:
        if game_board[game_turn-1]  == '':
            game_board[game_turn-1] = signs_player[active_player]
            if check_win(game_board):
                game_active = False;
            elif '' not in game_board:
                print(f'The field ran out of cells. The game ended in a draw!')
                game_active = False;
        else:
            print('The cell is busy. Lets start over again.')
    else:
        print(f'player number {active_player} deceives. Lets start over again.')