def minFallingPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i ==0:
                grid[i][j] = grid[i][j]
            elif j ==0 and i >0:
                grid[i][j] = min(grid[i-1][j+1:]) + grid[i][j]
            elif j ==len(grid[0])-1 and i>0:
                grid[i][j] = min(grid[i-1][:j]) + grid[i][j]
            else:
                grid[i][j] = min( min(grid[i-1][:j] )+ grid[i][j], min(grid[i-1][j+1:] )+grid[i][j])
    return min(grid[-1])
minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])