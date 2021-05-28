# gloabal variables
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

game_is_on = True                                       # if game still on
winner = None                                           # if tie, winner stays None
current_player = input("starting player (X or O) : ")   # whose turn


# display board
def print_board() :
    print(" | " + "- + - + -" + " | ")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | " + "     1 | 2 | 3")
    print(" | " + "- + - + -" + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | " + "     4 | 5 | 6")
    print(" | " + "- + - + -" + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | " + "     7 | 8 | 9")
    print(" | " + "- + - + -" + " | ")


# play game
def play_game() :
    """ defines the game """
    # display initial board
    print_board()

    # main game loop
    while game_is_on :
        turn(current_player)

        check_game_over()

        flip_player()
        
    # game over
    if winner == "X" or winner == "O" :
        print("The WINNER is : " + winner + "!!!")
    elif winner == None :
        print("It's a TIE!!!")
    
    # restart game
    restart_game()


# handle a single turn of the current player
def turn(player) :
    """ defines the current payer's move """

    print("{}'s turn : ".format(player))
    posn = input("Choose a position from 1 to 9 : ")

    valid = False
    while not valid :

        while posn not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] :
            posn = input("Invalid input! Choose a position from 1 to 9 : ")
        
        posn = int(posn) - 1

        if board[posn] == " " :
            valid = True
        else :
            print("That position is already filled. Try again!")
        
    board[posn] = player

    print_board()


# check if game over
def check_game_over() :
    check_for_win()
    check_if_tie()


# check win
def check_for_win() :   
    global winner 

    # check rows
    row_win = check_rows()

    # check columns
    col_win = check_columns()

    # check diagonals
    diag_win = check_diagonals()

    if row_win :
        winner = row_win
    elif col_win :
        winner = col_win
    elif diag_win :
        winner = diag_win
    else :
        winner = None
    
    return 

def check_rows() :
    global game_is_on

    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "

    # check for equal non-empty rows
    if row_1 or row_2 or row_3 :
        game_is_on = False
    # return the winner (X or O)
    if row_1 :
        return board[0]
    if row_2 :
        return board[3]
    if row_3 :
        return board[6]

def check_columns() :
    global game_is_on

    column_1 = board[0] == board[3] == board[6] != " "
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "

    # check for equal non-empty columns
    if column_1 or column_2 or column_3 :
        game_is_on = False
    # return the winner (X or O)
    if column_1 :
        return board[0]
    if column_2 :
        return board[1]
    if column_3 :
        return board[2]

def check_diagonals() :
    global game_is_on

    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "

    # check for equal non-empty diagonals
    if diagonal_1 or diagonal_2 :
        game_is_on = False
    # return the winner (X or O)
    if diagonal_1 :
        return board[0]
    if diagonal_2 :
        return board[2]


# check tie
def check_if_tie() :
    global game_is_on

    if " " not in board :
        game_is_on = False


# flip player
def flip_player() :
    """ switches between players """

    global current_player

    if current_player == "X" :
        current_player = "O"
    elif current_player == "O" :
        current_player = "X"


# ask if player wants to restart the game or not
def restart_game() :
    global board, game_is_on, winner, current_player
    restart = input("Do want to play again? (Y/N) : ")
    if restart == "y" or restart == "Y" :
        board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

        game_is_on = True                                       
        winner = None                                          
        current_player = input("starting player (X or O) : ")   
        play_game()

if __name__ == "__main__" :
    play_game()