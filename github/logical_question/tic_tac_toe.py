'''
Create a function that takes a list of character inputs from a Tic Tac Toe game. Inputs will be taken from player1 as "X", player2 as "O", and empty spaces as "#". The program will return the winner or tie results.

Examples
tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]
]) ➞ "Player 1 wins"


tic_tac_toe([
  ["X", "O", "O"],
  ["O", "X", "O"],
  ["X", "#", "O"]
]) ➞ "Player 2 wins"


tic_tac_toe([
  ["X", "X", "O"],
  ["O", "X", "O"],
  ["X", "O", "#"]
]) ➞ "It's a Tie"
Notes
All inputs are valid (there will be no games where both players win).
'''

def tic_tac_toe(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '#':
            return f"Player {1 if board[i][0] == 'X' else 2} wins"
        elif board[0][i] == board[1][i] == board[2][i] != '#':
            return f"Player {1 if board[0][i] == 'X' else 2} wins"
    if board[0][0] == board[1][1] == board[2][2] != '#':
        return f"Player {1 if board[0][0] == 'X' else 2} wins"
    elif board[0][2] == board[1][1] == board[2][0] != '#':
        return f"Player {1 if board[0][2] == 'X' else 2} wins"
    else:
        return "It's a Tie"
        



if __name__=="__main__":
    board1 = [
            ["X", "O", "O"],
            ["O", "X", "O"],
            ["O", "#", "X"]
    ]

    print(tic_tac_toe(board1)) 
    board2=([
            ["X", "O", "O"],
            ["O", "X", "O"],
            ["X", "#", "O"]
    ])
    print(tic_tac_toe(board2))

    board3=([
        ["X", "X", "O"],
        ["O", "X", "O"],
        ["X", "O", "#"]
    ])
    print(tic_tac_toe(board3))

