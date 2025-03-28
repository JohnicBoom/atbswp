# In this chapter, we used the dictionary value {'1h': 'bking',
# '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
# to represent a chess board. Write a function named
# isValidChessBoard() that takes a dictionary argument and returns
# True or False depending on if the board is valid.
#
# A valid board will have exactly one black king and exactly one
# white king. Each player can only have at most 16 pieces, at most
# 8 pawns, and all pieces must be on a valid space from '1a' to '8h';
# that is, a piece can’t be on space '9z'. The piece names begin with
# either a 'w' or 'b' to represent white or black, followed by 'pawn',
# 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should
# detect when a bug has resulted in an improper chess board.
#
#
# Define our function
def isValidChessBoard(board):
    # Initialize our piece-counting dictionary
    piecesCount = {'wpawn': 0, 'bpawn': 0, 'wknight': 0, 'bknight': 0,
              'wbishop': 0, 'bbishop': 0, 'wrook': 0, 'brook': 0,
              'wqueen': 0, 'bqueen': 0, 'wking': 0, 'bking': 0}
    # Generate a tuple of legal chess board spaces
    boardSpaces = tuple(f"{row}{col}" for row in range(1,9) for col in 'abcdefgh')
    # Generate a tuple of valid pieces
    validPieces = tuple(piecesCount.keys())
    # Loop through all items
    for k, v in board.items():
        # Check move location (keys) to see if it is valid
        if k not in boardSpaces:
            return False
        # Check piece to see if it is valid
        if v not in validPieces:
            return False
        # Count pieces (values) to see if there are more than allowed
        piecesCount[v] += 1
    # Outside of our loop
    # Get piece totals for both players
    whitePieces = piecesCount['wpawn'] + piecesCount['wknight'] + piecesCount['wbishop'] + piecesCount['wrook'] + piecesCount['wqueen'] + piecesCount['wking']
    blackPieces = piecesCount['bpawn'] + piecesCount['bknight'] + piecesCount['bbishop'] + piecesCount['brook'] + piecesCount['bqueen'] + piecesCount['bking']
    # Check pawn counts
    if piecesCount['wpawn'] > 8 or piecesCount['bpawn'] > 8:
        return False
    # Check number of kings
    if piecesCount['wking'] != 1 or piecesCount['bking'] != 1:
        return False
    # Check total piece counts
    if whitePieces > 16 or blackPieces > 16:
        return False
    # All checks have passed, so return True
    return True
# Test cases
testBoard1 = {'1h': 'bking','8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(testBoard1))
testBoard2 = {'11h': 'bking','8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(testBoard2))
testBoard3 = {'1h': 'bbking','8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(testBoard3))
testBoard4 = {'1h': 'bking', '2h': 'bking', '8c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(testBoard4))