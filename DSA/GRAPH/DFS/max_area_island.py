class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        column = len(grid[0])
        visit = set()
        res = 0
        maximer = 0
        
        def dfs(r , c ):
            nonlocal res
            if r < rows and r>=0 and c>=0 and c < column and grid[r][c] == 1 and (r,c) not in visit:
                visit.add((r,c))
                res+=1
                dfs(r+1 , c )
                dfs(r , c+1 )
                dfs(r-1 , c )
                dfs(r , c-1 )  
            return 
                
           
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i , j)
                    maximer = max(maximer , res)
                    res = 0
        return maximer
        
            