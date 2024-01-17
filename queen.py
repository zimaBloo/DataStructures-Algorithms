#This source provided a lot of insight for solving this task: https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/

def safetyCheck(board, row, column):
    #Return binary safety value
    
    for i in range(column):

        if board[row][i] == 1:
            return False

    for k in range(row, -1, -1):
        j = column - (row - k)
        if j < 0:
            break
        if board[k][j] == 1:
            return False

    l, m = row, column

    while l < len(board) and m >= 0:
        if board[l][m] == 1:
            return False
        l += 1
        m -= 1

    return True

def calculateNumber(board, column, m):
    counter = 0

    if m == 0:
        return 1
    elif column >= len(board) or len(board) - column < m:
        return 0

    for i in range(len(board)):
        if safetyCheck(board, i, column) is True:

            board[i][column] = 1
            counter += calculateNumber(board, column + 1, m-1)
            
            board[i][column] = 0

    if len(board) - column - 1 >= m:
        counter += calculateNumber(board, column + 1, m)

    #Counter implementation in a recursive function was learned here: https://stackoverflow.com/questions/15052704/how-to-create-a-counter-inside-a-recursive-function
    return counter

def queen(n, m):
    board = []

    for a in range(n):
        row = []

        for b in range(n):
            
            row.append(0)

        board.append(row)
    
    answer = calculateNumber(board, 0, m) #Trigger recursion

    return  answer


if __name__ == "__main__":
    print(queen(4, 4))  # 2
    print(queen(4, 2))  # 44
    print(queen(6, 4))  # 982
    print(queen(7, 2))  # 700
    print(queen(8, 8))  # 92