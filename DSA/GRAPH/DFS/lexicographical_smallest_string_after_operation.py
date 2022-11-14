class Solution:
    def findLexSmallestString(s,a,b):
        # DFS AND BFS
        
        def add(s , a):
            arr = list(s)
            for i in range(len(arr)):
                if i%2 != 0 :
                    k = str(int(arr[i]) + a)
                    arr[i] = k[-1]
            return ''.join(arr)
                    
            
        def rotate(s , b):
            arr = list(s)
            for i in range(b):
                p = arr.pop()
                arr.insert(0, p)
            return ''.join(arr)
        
        
        visited = set()
        ans = s
        def dfs(s):
            nonlocal ans
            if s in visited:
                return
            ans = min(ans, s)
            visited.add(s)
            dfs(rotate(s, b))
            dfs(add(s, a))
            
        dfs(s)
        return ans
            