def make_pass(board):
    #fill undetermined squares with all possiblities
    reallot(board)
    #remove parities
    rem_parities(board)
    #check for only single possibilities in a square
    for r in range(9):
        for c in range(9):
            if board[r][c] not in ("1","2","3","4","5","6","7","8","9"):
                if len(board[r][c]) == 1:
                    board[r][c] = board[r][c][0]
    #check for only valid option in a row/column/square
    for r in range(9):
        for c in range(9):
            if board[r][c] not in ("1","2","3","4","5","6","7","8","9"):
                poss = []
                for num in board[r][c]:
                    if num not in parsed(board_row(board,r,c)) or num not in parsed(board_col(board,r,c)) or num not in parsed(board_sq(board,r,c)):
                        poss.append(num)
                if len(poss) == 1:
                    board[r][c] = poss[0]

def rem_parities(board):
    return board

def parsed(nums):
    num_list = []
    for num in nums:
        if num not in ("1","2","3","4","5","6","7","8","9"):
            for sub_num in num:
                if sub_num not in num_list:
                    num_list.append(sub_num)
        elif num not in num_list:
            num_list.append(num)
    return num_list

def board_row(board,r,col):
    contained = []
    for c in range(9):
        if board[r][c] != "0" and col != c:
            contained.append(board[r][c])
    return contained

def board_col(board,row,c):
    contained = []
    for r in range(9):
        if board[r][c] != "0" and row != r:
            contained.append(board[r][c])
    return contained

def board_sq(board,r,c):
    if r < 3:
        rows = (0,1,2)
    elif r > 5:
        rows = (6,7,8)
    else:
        rows = (3,4,5)
    if c < 3:
        cols = (0,1,2)
    elif c > 5:
        cols = (6,7,8)
    else:
        cols = (3,4,5)
    contained = []
    for row in rows:
        for col in cols:
            if board[row][col] != "0" and row != r or col != c:
                contained.append(board[row][col])
    return contained

def reallot(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] not in ("1","2","3","4","5","6","7","8","9"):
                poss = []
                for n in range(1,10):
                    if str(n) not in board_row(board,r,c) and str(n) not in board_col(board,r,c) and str(n) not in board_sq(board,r,c):
                        poss.append(str(n))
                board[r][c] = poss
    return board

def solve(board):
    solved = True
    for line in board:
        for slot in line:
            if slot not in ("1","2","3","4","5","6","7","8","9"):
                solved = False
    if not solved:
        make_pass(board)
    return board
