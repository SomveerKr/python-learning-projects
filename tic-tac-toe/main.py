game_board = [['_', '_', '_'],
              ['_', '_', '_'],
              ['_', '_', '_']]

game_over = False

def generate_game_shape(game_board):
    return f"""
    {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]}
    {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]}
    {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]}
    """

print("Welcome to Tic Tac Toe!")
print("Player 1 is X and Player 2 is O.")


print(f"""
To make a move, enter the `row,column` numbers (e.g., '1,2' for row 1, column 2).
=====================
Let's start the game!
=====================
{generate_game_shape(game_board)}
""")



def update_game_board(row_move, column_move, player):
    if player =='X':
        game_board[row_move][column_move] = 'X'
        print(game_result(game_board))
    else:
        game_board[row_move][column_move] = 'O'
        print(game_result(game_board))


def game_result(board):
    global game_over
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            game_over = True
            print(generate_game_shape(game_board))
            return f"Player {row[0]} wins!"
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '_':
            game_over = True
            print(generate_game_shape(game_board))
            return f"Player {board[0][col]} wins!"
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '_':
        game_over = True
        print(generate_game_shape(game_board))
        return f"Player {board[0][0]} wins!"
        
    if board[0][2] == board[1][1] == board[2][0] != '_':
        game_over = True
        print(generate_game_shape(game_board))
        return f"Player {board[0][2]} wins!"
    #check whether all the spaces all filled with player moves
    if any('_' in row for row in game_board):
        return generate_game_shape(game_board)
    else:
        game_over = True
        return "It's a draw!"
while not game_over:
    x_move = input("Player 1 (X), enter your move: ")
    x_row, x_col = map(int, x_move.split(","))    
    print(f"Player 1 (X) moved to row {x_row}, column {x_col}.")
    update_game_board(row_move=x_row-1, column_move=x_col-1, player='X')
    y_move = input("Player 2 (O), enter your move: ")
    y_row, y_col = map(int, y_move.split(","))
    print(f"Player 2 (O) moved to row {y_row}, column {y_col}.")
    update_game_board(row_move=y_row-1, column_move=y_col-1, player='O')
