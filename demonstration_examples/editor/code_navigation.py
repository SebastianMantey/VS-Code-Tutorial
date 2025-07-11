from itertools import cycle


def create_initial_game_board():

    game_size = int(input("How many rows/columns should the game board have? "))
    game_board = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        
        game_board.append(row)
            
    return game_board


def show(game_board):
    
    # separator between moves
    print("---------------------------------")

    # header indicating column numbers
    header_row = " "
    for i in range(len(game_board)):
        header_row += "  " + str(i)
    print(header_row)
    
    # row numbers and actual game board
    for row_index, row in enumerate(game_board):
        print(row_index, row)
    
    # empty line for clarity
    print("")
    
    return


def make_move(game_board, player):
    
    # game interaction
    print(f"Player {player}:")
    choice = input("Which position (row, column) do you want to play?: ")
    row, column = choice.split(",")
    row, column = int(row), int(column)

    # making the actual move
    if game_board[row][column] != 0:
        raise Exception("This position is already taken!")

    else:
        game_board[row][column] = player
        return game_board


def determine_game_status(game_board):

    # helper function
    def all_the_same(lst):
        player = lst[0]
        if (lst.count(player) == len(lst)) and player != 0:
            return True
        else:
            return False
    
    # horizontal winner
    for row in game_board:
        if all_the_same(row):
            return "horizontal win"
        
    # vertical winner
    for index in range(len(game_board)):
        column_elements = []
        for row in game_board:
            column_elements.append(row[index])
        
        if all_the_same(column_elements):
            return "vertical win"
        
    # diagonal winner (\)
    diagonal_elements = []
    for index in range(len(game_board)):
        diagonal_elements.append(game_board[index][index])
    
    if all_the_same(diagonal_elements):
        return "diagonal win"
        
    # diagonal winner (/)
    diagonal_elements = []
    indices = range(len(game_board))
    for row, column in zip(indices, reversed(indices)):
        diagonal_elements.append(game_board[row][column])
    
    if all_the_same(diagonal_elements):
        return "diagonal win"

    # draw
    free_positions = []
    for row in game_board:
        for position in row:
            if position == 0:
                free_positions.append(position)

    if len(free_positions) == 0:
        return "draw"
        
    return "ongoing"




players = cycle([1, 2])
playing = True

while playing:

    # game preparations
    game_board = create_initial_game_board()
    game_status = determine_game_status(game_board)

    while game_status == "ongoing":
        show(game_board)

        # player move
        current_player = next(players)
        valid_move = False
        while not valid_move:
            try: 
                game_board = make_move(game_board, current_player)
                valid_move = True
                
            except Exception as e:
                print("\n")
                print("Something went wrong:", e)
                print("Hint: The chosen position must be available on the board.")
                print("Hint: The values must be separated by a comma e.g. '0, 1'.")
                print("Try again!", "\n")

        # stopping condition for while-loop
        game_status = determine_game_status(game_board)
        if game_status != "ongoing":
            show(game_board)
            print("Game finished!!!")

            if game_status == "draw":
                print("It is a draw! \n")
            else:
                print(f"Player {current_player} has achieved a {game_status}! \n")
            
    keep_playing = input("Do you want to play again? (y/n) ")
    if keep_playing != "y":
        playing = False
