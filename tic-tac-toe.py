import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    if all(cell != ' ' for row in board for cell in row):
        return 'D'  # Draw
    
    return None

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif winner == 'D':
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0]][move[1]] = 'O'

def human_move(board):
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter row and column.")
            continue
        try:
            row, col = int(move[0]), int(move[1])
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken. Choose another cell.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column numbers between 0 and 2.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        human_move(board)
        print_board(board)
        if check_winner(board):
            break
        
        ai_move(board)
        print_board(board)
        if check_winner(board):
            break
    
    winner = check_winner(board)
    if winner == 'D':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    play_game()
