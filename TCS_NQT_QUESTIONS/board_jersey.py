def board_jersey(board):
    for i in range(len(board)):
        board[i] = board[i] -1
    
    jersey = sorted(board)
    perm_jersey = jersey.copy()
    counter = 0
    temp_board = [0 for _ in range(len(board))]
    for i in range(len(jersey)):
        temp_board[board[i]] = jersey[i]
    counter+=1
    
    while temp_board != perm_jersey:
        jersey = temp_board.copy()
        for i in range(len(jersey)):
            temp_board[board[i]] = jersey[i]
        counter+=1
    print(counter)
    

board_jersey([ 1,2,3])