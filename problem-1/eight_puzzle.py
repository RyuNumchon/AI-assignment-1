import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h2(s): #Method that finds h2 utilizing the Manhattan distance of each tile.
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    dis = 0

    #'idx' => current index on the board. 
    #'g_idx' => index where the item should be (goal index)
    for idx, g_idx in zip(goal, board):     #zip joined 2 tuples
    #Calculate current row/column
        if idx == 0:
            current_row = 3
            current_col = 3
        else:
            current_row = int(idx/ 3) + 1
            current_col = idx % 3

        #Calculate goal row/column
        if g_idx == 0:
            goal_row = 3
            goal_col = 3
        else:
            goal_row= int(g_idx /3) + 1
            goal_col = g_idx % 3
        
        dis += abs(current_row - goal_row) + abs(current_col - goal_col)

    return dis

"""
def h2(s): #Method that finds h2 utilizing the position of the blank (0)
    # implement this function
    _, r, c = s

    # By manhattan distance
    mht = abs(r-2)+ abs(c-2)
    
    return mht
"""
