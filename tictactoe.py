DEFAULT_SIGN = '*'

def getBoard(size):
    board = [[DEFAULT_SIGN]*size for _ in range(size)]
    return board

def updateBoard(board):
    for i in board:
        print(i)


def winDiagonal(board, size):
    for rows in board:
        countSame = 0
        firstCond = rows[0]
        for xs in rows:
            if xs == firstCond:
                if firstCond != DEFAULT_SIGN:
                    countSame += 1
        if countSame == size:
            return True
    return False

def winHorizontal(board, size):

    for indxRow in range(size):
        countSame = 0
        firstCond = board[indxRow][0]
        for indxCol in range(size):
            if board[indxRow][indxCol] == firstCond:
                if firstCond != DEFAULT_SIGN:
                    countSame += 1
        if countSame == size:
            return True
    return False

def winTopLeftDiagonal(board, size):
    firstCond = board[0][0]
    countSame = 0
    for x in range(size):
        y = x
        if board[x][y] == firstCond:
            if firstCond != DEFAULT_SIGN:
                countSame += 1
        if countSame == size:
            return True
    return False

def winBottomLeftDiagonal(board, size):
    firstCond = board[size-1][0]
    countSame = 0
    x = size - 1
    for y in range(size):
        if board[x][y] == firstCond:
            if firstCond != DEFAULT_SIGN:
                countSame += 1
        if countSame == size:
            return True
        x -= 1
    return False
        
def getPlayer(player):
    if player == 1:
        return 2
    else:
        return 1

def getSign(player):
    if player == 1:
        return 'X'
    else:
        return 'O'

def move(row, col, sign, board, size):
    if 0 > row or row > size or 0 > col or col > size:
        print('ROW OR COLUMN OUT OF BOUNDS, TRY AGAIN')
        return board, False

    elif board[row-1][col-1] != DEFAULT_SIGN:
        print('INVALID MOVE, SLOT TAKEN')
        return board, False
    else:
        board[row-1][col-1] = sign
        return board, True



def main():
    size = int(input("Enter size of board "))
    board = getBoard(size)
    done = False
    player = 2
    while not done:
        updateBoard(board)
        player = getPlayer(player)
        sign = getSign(player)
        validTurn = False
        while not validTurn:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            print('')
            print('')
            board, validTurn = move(row, col, sign, board, size)
            updateBoard(board)
        if winDiagonal(board, size) == True or winHorizontal(board, size) == True or winBottomLeftDiagonal(board, size) == True or winTopLeftDiagonal(board, size) == True:
            done = True
            winner = player

        print('')
        print('')
    print("GAME OVER, PLAYER ", winner, "WON!")







main()
        
                
