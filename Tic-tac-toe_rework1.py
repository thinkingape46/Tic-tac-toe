from IPython.display import clear_output
''' This list stores symbol choice of players. '''
symbol_choice = ['', '']

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


'''clear_output clears the board.'''
clear_output

def print_board(board):

    '''This function prints the tic-tac-toe board.'''

    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

def tic_tac():

    '''players are asked whether they wish to play game?'''

    try:
        start = input("Do you wish to play the game (yes or no)? ")
    except:
        print("I am not using this, because the input accepts anything")
    if start in ['yes', 'oui']:
        print("\nWELCOME TO TIC-TAC-TOE!\n")
        start_code()
    elif start in ['no', 'non']:
        print('See you later!')
    else:
        print("please enter 'yes' or 'no' to continue...\n")
        tic_tac()

def tic_tac_next():

    '''upon completion of the game, players are given option to restart the game.'''
    
    try:
        start = input("\nDo you wish to play the game again (yes or no)? ")
    except:
        print("I am not using this, because the input accepts anything")
    if start in ['yes', 'oui']:
        start_code()
    elif start in ['no', 'non']:
        print('See you later!')
    else:
        print("please enter 'yes' or 'no' to continue...\n")
        tic_tac()

def start_code():

    '''player 1 is asked to choose their symbol between 'X' and 'O'.'''

    player1_symbol = input("Player1, Enter your symbol X or O: ")

    if player1_symbol not in ['X', 'O']:
        print("Plese enter the symbol 'X' or 'O'")
        start_code()
        
    elif player1_symbol == 'X':
        player2_symbol = 'O'
        symbol_choice[0] = player1_symbol
        '''Once the first player choose a symbol, the second player is assigned the second one inthe next line.'''
        symbol_choice[1] = player2_symbol
        print(f"\nPlayer1 is assigned {player1_symbol} and Player2 is assigned {player2_symbol}\n")
        play_game()

    elif player1_symbol == 'O':
        player2_symbol = 'X'
        symbol_choice[0] = player1_symbol
        '''Once the first player choose a symbol, the second player is assigned the second one inthe next line.'''
        symbol_choice[1] = player2_symbol
        print(f"Player1 is assigned {player1_symbol} and Player2 is assigned {player2_symbol}")
        play_game()

def play_game():

    '''This function accepts input input from the player1, and finishes the game if player1 wins or draw. Otherwise it will move on to play_game2(). '''

    player1_choice = input("Player1, please enter your choice of number: ")

    if int((player1_choice)) not in range(1, 10):
        print("\nOnly numbers between 1 and 9 are allowed\n")
        play_game()

    else:
        player1_num = int(player1_choice)

        if board[player1_num] != ' ':
            print('The cell is already filled')
            clear_output()
            print_board(board)
            play_game()
        else:
            board[player1_num] = (symbol_choice[0])
            clear_output()
            '''clear_output(), it is to refresh the screen. '''

            print_board(board)

            if ' ' not in board:
                '''Checking if board is completely filled. no spaces ---> board is filled'''
                print("This game is a tie, well done!")
                for n in range(1,10):
                    board[n] = ' '
                tic_tac_next()

            elif board[7] == board[8] == board[9] != ' ' or board[1] == board[2] == board[3] != ' '  or board[4] == board[5] == board[6] != ' '  or board[7] == board[4] == board[1] != ' '  or board[8] == board[5] == board[2] != ' '  or board[9] == board[6] == board[3] != ' '  or board[7] == board[5] == board[3] != ' '  or board[9] == board[5] == board[1] != ' ':
                '''Checking player1 won the game.'''
                print("\nPlayer 1 has won, well done!\nPlayer 2, good luck next time.\n")
                for n in range(1,10):
                    '''emptying the board for the next round.'''
                    board[n] = ' '
                tic_tac_next()

            else:
                play_game2()

def play_game2():

    '''This function accepts input input from the player1, and finishes the game if player1 wins or draw. Otherwise it will move on to play_game2().'''
    
    player2_choice = int(input("Player2, please enter your choice of number: "))        

    if int((player2_choice)) not in range(1, 10):
        print("\nOnly numbers between 1 and 9 are allowed\n")
        play_game2()

    else:
        player2_num = int(player2_choice)

        if board[player2_num] != ' ':
            print('The cell is already filled')
            clear_output()
            print_board(board)
            play_game2()

        else:
            board[player2_num] = (symbol_choice[1])
            clear_output()
            print_board(board)

            if ' ' not in board:
                '''Checking if board is completely filled. no spaces ---> board is filled'''
                print("This game is a tie, well done!")
                for n in range(1,10):
                    board[n] = ' '
                tic_tac_next()

            if board[7] == board[8] == board[9] != ' ' or board[1] == board[2] == board[3] != ' '  or board[4] == board[5] == board[6] != ' '  or board[7] == board[4] == board[1] != ' '  or board[8] == board[5] == board[2] != ' '  or board[9] == board[6] == board[3] != ' '  or board[7] == board[5] == board[3] != ' '  or board[9] == board[5] == board[1] != ' ':
                '''Checking player2 won the game.'''
                print("Player 2 has won, well done!\nPlayer 1, good luck next time.")

                for n in range(1,10):
                    '''emptying the board for the next round.'''
                    board[n] = ' '
                tic_tac_next()
            else:
                play_game()
tic_tac()
