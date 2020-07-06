# Devlop Tic Tac Toe game
import random

# For Display Board
def board(game_input) :
    print(game_input[7]+" | "+game_input[8]+" | "+game_input[9])
    print(game_input[4]+" | "+game_input[5]+" | "+game_input[6])
    print(game_input[1]+" | "+game_input[2]+" | "+game_input[3])
    print()


# Choosing player marker
def choose_marker(player):
    marker = ' '
    while marker!='X' and marker!='O':
        marker = input(f"{player} Choose Your Marker (O/X) :")
    if marker == 'X':
        return ('X' , 'O')
    else:
        return ('O', 'X')


# Put marker to position
def put_marker(game_input,marker,position):
    game_input[position]=marker



# Winning Conditions
def win(game_input, marker):
    return ((game_input[1] == game_input[2] == game_input[3] == marker) or
            (game_input[4] == game_input[5] == game_input[6] == marker) or
            (game_input[7] == game_input[8] == game_input[9] == marker) or
            (game_input[7] == game_input[5] == game_input[3] == marker) or
            (game_input[1] == game_input[5] == game_input[9] == marker) or
            (game_input[1] == game_input[4] == game_input[7] == marker) or
            (game_input[2] == game_input[5] == game_input[8] == marker) or
            (game_input[3] == game_input[6] == game_input[9] == marker))

# Randomly choose the 1st player
def choose_player():
    player = random.randint(1,2)
    if player == 1: 
        return player1
    else:
        return player2

# Check for space availability
def space(game_input, position):
    return game_input[position] == ' '

# Check the board is full or not
def full_board_check(game_input):
    for i in range(1, 10):
        if space(game_input, i):
            return False
    return True

# Choose the position 
def player_choise(game_input,player):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space(game_input, position):
        position = int(input(f"{player} Choose position (1-9) :: "))
    return position


def play_again():
    choice = input('Would you like to play again[Y/N]: ')
    return choice == 'Y'

#  Main function for playing game..
def starting(player, player_marker,the_board):
    board(the_board)
    position = player_choise(the_board,player)
    turn = ' '
    game_on = True
    put_marker(the_board, player_marker, position)

    if win(the_board, player_marker):
        board(the_board)
        print(f"{random.choice(msg)}, {player}  Won !!!")
        game_on = False
    else:
        if full_board_check(the_board):
            board(the_board)
            print('Ohh!, This game is Tie...')
            game_on = False

        else:
            if player == player1:
                turn = 'player_2'
            else:
                turn = 'player_1'

    return turn, game_on


# Start The Game ::
while True:
    the_board=[' ']*10

    msg=['Hii', 'Hey', 'hello']
    print('*'*30)
    print("Welcome, Let\'s Play...'Tic-Tac-Toe'")
    print('*'*30)
    player1 = input("Hey Enter 1st Player name:")
    player2 = input("Hey Enter 2st Player name:")
    player1_marker, player2_marker = choose_marker(player1)
    print(f"{random.choice(msg)}, {player1} Your sign is '{player1_marker}'")
    print(f"{random.choice(msg)}, {player2} Your sign is '{player2_marker}'")

    turn = choose_player()

    print(turn + ' will Play first')

    play_game = input('Ready to play[Y/N]: ')
    print('*'*25)

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player_1':
            turn, game_on = starting(player1, player1_marker,the_board)
        else:
            turn, game_on = starting(player2, player2_marker,the_board)

    if not play_again():
        print("Quit The game....")
        break
