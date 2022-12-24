from random import randint


def print_board():
    index = 0
    for _ in range(3):
        print(board[index] + '  |  ' + board[index+1] + '  |  ' + board[index+2])
        print('--------------')
        index += 3
            
            
def player_move(player, cord):
    board[cord] = player


def check_winner(player):
    #horizontal win
    index = 0
    for _ in range(3):
        if (board[index] == player) and (board[index+1] == player) and (board[index+2] == player):
            return True
        index += 3
        
    #vertical win
    index = 0
    for _ in range(3):
        if (board[index] == player) and (board[index+3] == player) and (board[index+6] == player):
            return True
        index += 1
    
    #diagonal win
    if (board[0] == player) and (board[4] == player) and (board[8] == player):
            return True
    if (board[2] == player) and (board[4] == player) and (board[6] == player):
            return True

    #no win
    return False


def check_move(cord):
    if board[cord] == "X" or board[cord] == "O":
        return True


def check_draw():
    draw = False
    for i in range(9):
        if board[i] == 'X' or board[i] == 'O':
            draw = True
        else:
            return False
            
    return draw


board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
player = 'X' if randint(0,1) == 1 else 'O'
is_gaming = True

while is_gaming:
    print_board()
    move = int(input(f'Player {player} move: '))
    move -= 1

    while check_move(move):
        print("Invalid Move!\nTry Again.")
        print_board()
        move = int(input(f'Player {player} move: '))
        move -= 1
        
    player_move(player, move)
    
    if check_winner(player):
        print_board()
        print(f'Player "{player}" Won!')
        is_gaming = False

    if check_draw():
        print_board()
        print("It's a draw!")
        is_gaming = False

    player = 'X' if player == 'O' else 'O'
