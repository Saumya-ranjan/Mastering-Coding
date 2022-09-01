graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited,queue,node,graph):
    if node not in visited:
        visited.append(node)
        queue.append(node)
    while queue:
        a = queue.pop(0)
        print(a , end = " ")
        for i in graph[a]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
         
bfs(visited,queue,'A',graph)