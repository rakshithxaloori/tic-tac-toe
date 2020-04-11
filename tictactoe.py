"""
Tic Tac Toe Player
"""

from math import inf
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

NEGATIVE_INFINITY = -inf
POSITIVE_INFINITY = inf


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # print("-------------------------------")
    # for row in board:
    #     print(row)
    # print("-------------------------------")
    countX = 0
    countO = 0
    for row in board:
        for column in row:
            if column == X:
                countX += 1
            if column == O:
                countO += 1

    if countX == countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionsSet = set()
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == EMPTY:
                actionsSet.add((i, j))
            j += 1
        i += 1

    return actionsSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    actionI, actionJ = action

    if board[actionI][actionJ] != EMPTY:
        raise NameError("Invalid action")

    deepCopyBoard = deepcopy(board)

    deepCopyBoard[actionI][actionJ] = player(deepCopyBoard)

    return deepCopyBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check the rows
    i = 0
    while i < 3:
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            if board[i][0] == X:
                return X
            else:
                return O
        i += 1

    # Check the columns
    i = 0
    while i < 3:
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY:
            if board[0][i] == X:
                return X
            else:
                return O
        i += 1

    # Check the diagonals
    # 00, 11, 22
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O
    # 02, 11, 20
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    # The game board is not full, return False
    for row in board:
        for column in row:
            if column == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1

    # The match has drawn
    return 0


def maxValue(board):
    if terminal(board):
        return utility(board)

    v = NEGATIVE_INFINITY
    for action in actions(board):
        minValAction = minValue(result(board, action))
        if v < minValAction:
            v = minValAction

    return v


def minValue(board):
    if terminal(board):
        return utility(board)

    v = POSITIVE_INFINITY
    for action in actions(board):
        maxValAction = maxValue(result(board, action))
        if v > maxValAction:
            v = maxValAction

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        # Maximise
        optimalMax = NEGATIVE_INFINITY
        optimalAction = None
        for action in actions(board):
            tempMin = minValue(result(board, action))
            print(tempMin, " ", action)
            if tempMin >= optimalMax:
                optimalMax = tempMin
                optimalAction = action
        print("OptimalMove: ", optimalMax, ", ", optimalAction)
        return optimalAction

    else:
        # Minimise
        optimalMin = POSITIVE_INFINITY
        optimalAction = None
        for action in actions(board):
            tempMax = maxValue(result(board, action))
            print(tempMax, " ", action)
            if tempMax <= optimalMin:
                optimalMin = tempMax
                optimalAction = action
        print("OptimalMove: ", optimalMin, ", ", optimalAction)
        return optimalAction
