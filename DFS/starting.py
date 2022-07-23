graph = {'A':['B','C','D'],'B':['E'],'C':['D','E'],'D':[],'E':[]}
visited = set()

# DFS Traversing Technique
# Recursion : 


def dfs(graph,visited,root):
    if root not in visited:
        print(root)
        visited.add(root)
        for i in graph[root]:
            dfs(graph,visited,i)

dfs(graph,visited,'A')