'''

Create a function that takes a 5x5 2D list and returns True if it has at least one Bingo, and False if it doesn't.

Examples
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]) ➞ True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) ➞ True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) ➞ True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) ➞ False
Notes
Only check for diagonals, horizontals and verticals.

'''


def bingo_check(board):
    for i in range(5):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == "x":
            return True
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == "x":
            return True
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4] == "x":
        return True
    if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == "x":
        return True
    return False


if __name__ =="__main__":

    # board=([
    # [45, "x", 31, 74, 87],
    # [64, "x", 47, 32, 90],
    # [37, "x", 68, 83, 54],
    # [67, "x", 98, 39, 44],
    # [21, "x", 24, 30, 52]
    # ])

    board=([
        [45, "x", 31, 74, 87],
        [64, 78, 47, "x", 90],
        [37, "x", 68, 83, 54],
        [67, "x", 98, "x", 44],
        [21, "x", 24, 30, 52]
    ])
    print(bingo_check(board))
