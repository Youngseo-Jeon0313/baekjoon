def check_win(board, check_OX):
    check_num = 0
    if board[0]==check_OX:
        check_num +=1
    if board[1]==check_OX:
        check_num +=1
    if board[2]==check_OX:
        check_num +=1
    if board[0][0]+board[1][0]+board[2][0]==check_OX:
        check_num +=1
    if board[0][1]+board[1][1]+board[2][1]==check_OX:
        check_num +=1
    if board[0][2]+board[1][2]+board[2][2]==check_OX:
        check_num +=1
    if board[0][0]+board[1][1]+board[2][2]==check_OX:
        check_num +=1
    if board[0][2]+board[1][1]+board[2][0]==check_OX:
        check_num +=1
    if check_num :
        return 1
    else:
        return 0
    

def solution(board):
    O_num = 0; X_num = 0;
    answer = -1
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                O_num += 1
            elif board[i][j]=='X':
                X_num += 1
    if O_num == X_num:
        if check_win(board, 'OOO'):
            return 0
        else:
            return 1
    elif O_num == X_num+1:
        if check_win(board, 'XXX'):
            return 0
        else:
            return 1
    else:
        return 0    