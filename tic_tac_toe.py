def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    """
    Checks if a player has won the game.
    """
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal from top-left
        [2, 4, 6]   # Diagonal from top-right
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def is_full(board):
    """
    Checks if the board is full.
    """
    return all(space != " " for space in board)


def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    print("Welcome to Tic Tac Toe!")
    print("Player X and Player O will alternate turns.")
    print("Choose positions using numbers 1-9 corresponding to the board:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 \n")

    board = [" "] * 9  # 3x3 board initialized with empty spaces
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Please choose an empty position between 1 and 9.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # Place the player's marker on the board
        board[move] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a draw
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
