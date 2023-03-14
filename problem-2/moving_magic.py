import copy


def initial_state():
    return (((6, 9, 8), (7, 1, 3), (2, 5, 4)), 0, 1)


def is_goal(s):
    # checking a condition for row, col and diagonal sum
    s = s[0] # to get only board
    
    s = list(s) # convert the tuple into list
    s_cvt = []
    for elem in s:
        s_cvt.append(list(elem))
        
    row, col, diag = False, False, False
    if sum(s_cvt[0]) == 15 and sum(s_cvt[1]) == 15 and sum(s_cvt[2]) == 15:
        row = True
    if (s_cvt[0][0]+s_cvt[1][0]+s_cvt[2][0] == 15) and (s_cvt[0][1]+s_cvt[1][1]+s_cvt[2][1] == 15) and (s_cvt[0][2]+s_cvt[1][2]+s_cvt[2][2] == 15):
        col = True
    if (s_cvt[0][0]+s_cvt[1][1]+s_cvt[2][2] == 15) and (s_cvt[0][2]+s_cvt[1][1]+s_cvt[2][0] == 15):
        diag = True
    
    
    return row and col and diag


def successors(s):
    
    # where s is the successors
    _, r, c = s
    # can move in four direction -> up, down, left and right
    # up
    new_row, new_col = r-1, c
    if is_valid(new_row, new_col): # check that it is not exceed the board boundary
        yield move_nine(s, new_row, new_col), 1
    # down
    new_row, new_col = r+1, c
    if is_valid(new_row, new_col):
        yield move_nine(s, new_row, new_col), 1
    # left
    new_row, new_col = r, c-1
    if is_valid(new_row, new_col):
        yield move_nine(s, new_row, new_col), 1
    # right
    new_row, new_col = r, c+1
    if is_valid(new_row, new_col):
        yield move_nine(s, new_row, new_col), 1



def is_valid(r, c):
    # check that our moves didn't exceed the 3x3 board
    return 0 <= r <= 2 and 0 <= c <= 2 


def move_nine(s, new_row, new_col):
    # moving a pile that has 9, in other word, just swap its position with
    # the place that in the condition
    current_board, r, c = s
    current_board = list(current_board)
    board = []
    for elem in current_board:
        board.append(list(elem))
        
    new_board = copy.deepcopy(board)
    new_board[r][c] = new_board[new_row][new_col]
    new_board[new_row][new_col] = 9

    moved_board = []
    for elem in new_board:
        moved_board.append(tuple(elem))
    return (tuple(moved_board), new_row, new_col)
