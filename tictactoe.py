def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    return all(cell != " " for row in board for cell in row)

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        game_over = False

        print("Tic-Tac-Toe Game")
        print_board(board)

        while not game_over:
            print(f"Player {current_player}'s turn")
            move = get_move()

            row, col = (move - 1) // 3, (move - 1) % 3

            if board[row][col] == " ":
                board[row][col] = current_player
                print_board(board)

                if check_winner(board, current_player):
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif check_tie(board):
                    print("It's a tie!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("That position is already taken. Try again.")

        replay = input("Do you want to play again? (yes/no): ")
        if replay.lower() != "yes":
            break

if __name__ == "__main__":
    play_game()
