board = None
turn = None
winner = None
winningSquares = None
numberOfMoves = None


def reset():
    global board, turn, winner, numberOfMoves, winningSquares
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    turn = "X"
    winner = None
    winningSquares = []
    numberOfMoves = 0


reset()


def makeMove(xPos, yPos):
    global board, turn, winner, numberOfMoves

    board[yPos][xPos] = turn
    numberOfMoves += 1
    checkWinner()
    turn = "X" if turn == "O" else "O"


def checkWinner():
    global board, turn, winner, numberOfMoves, winningSquares

    rowNumber = 0
    columnNumber = 0
    # Check for a horizontal winner
    while rowNumber < 3:
        if board[rowNumber][0] == board[rowNumber][1] == board[rowNumber][2] == turn:
            winner = turn
            winningSquares += [(rowNumber, 0), (rowNumber, 1), (rowNumber, 2)]
            break
        rowNumber += 1

    # Check for a vertical winner
    while columnNumber < 3:
        if (
            board[0][columnNumber]
            == board[1][columnNumber]
            == board[2][columnNumber]
            == turn
        ):
            winner = turn
            winningSquares += [(0, columnNumber), (1, columnNumber), (2, columnNumber)]
            break
        columnNumber += 1

    # Check for a diagonal winner
    if board[0][0] == board[1][1] == board[2][2] == turn:
        winner = turn
        winningSquares += [(0, 0), (1, 1), (2, 2)]
    if board[2][0] == board[1][1] == board[0][2] == turn:
        winner = turn
        winningSquares += [(2, 0), (1, 1), (0, 2)]

    # Check for draw
    if numberOfMoves >= 9 and winner is None:
        winner = "Draw"
        return
