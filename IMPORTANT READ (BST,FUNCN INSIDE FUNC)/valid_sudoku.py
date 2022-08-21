class Solution:
    def isValidSudoku(board):
        # FOR ROW --> O(N^2)
        def is_row_valid(board):
            for i in board:
                arr = []
                for j in i:
                    if j != ".":
                        if j not in arr:
                            arr.append(j)
                        else:
                            return False
            return True
        
        # FOR COLUMN -->> More considerably -- > O(N^3)
        def is_column_valid(board):
            count = 0
            while count != 9 :
                arr = []
                for i in board:
                    if i[count] !=".":
                        if i[count] not in arr:
                            arr.append(i[count])
                        else:
                            return False
                count+=1
            return True
        
        # For Small Square:
        def valid_small_square(board): 
            arr = []
            for i in range(3):
                for j in range(3):
                    if board[i][j] !='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
                    
            arr = []
            for i in range(3):
                for j in range(3,6):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = []       
            for i in range(3):
                for j in range(6,9):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = []       
            for i in range(3,6):
                for j in range(3):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = []        
            for i in range(3,6):
                for j in range(3,6):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = []       
            for i in range(3,6):
                for j in range(6,9):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = []        
            for i in range(6,9):

                for j in range(3):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = [] 
            for i in range(6,9):
                for j in range(3,6):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            arr = [] 
            for i in range(6,9):
                for j in range(6,9):
                    if board[i][j]!='.':
                        if board[i][j] not in arr:
                            arr.append(board[i][j])
                        else:
                            return False
            return True

        if is_row_valid(board) and is_column_valid(board) and valid_small_square(board) == True:
            return True
        return False
            
           
            
                                           
            
        
                    
                