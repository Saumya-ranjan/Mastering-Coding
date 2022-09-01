class Solution():
    def topological(self,graph):
        visited = []
        stack = []
        self.dfs(graph,stack,visited)
        return stack
    
    # This Time complexity is more than general :

    # def dfs(self,graph,stack,visited):
    #     for i in range(len(graph)):
    #         if i not in visited:
    #             for j in graph[i]:
    #                 if j not in visited:
    #                     visited.append(j)
    #                     stack.append(j)
    #             visited.append(i)
    #             stack.append(i)

    # General time complexity:
    
    def dfs(self,graph,stack,visited):
        for i in range(len(graph)):
            if len(graph[i])!=0:
                self.adjacency_node(graph[i],visited,stack)
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
            elif i not in visited:
                stack.append(i)
                visited.append(i)
    
    def adjacency_node(self,graph,visited,stack):
        for i in graph:
            if i not in visited:
                visited.append(i)
                stack.append(i)

a = Solution()
print(a.topological([[],[],[3],[1],[0,1],[2]] ))