
def isBipartite(graph):
  # BFS
  queue = []
  color=  [None for _ in range(len(graph))]
  for i in range(len(graph)):
    if color[i] == None:
      color[i] = 1
      queue.append(i)
      while queue:
        a = queue.pop(0)
        for i in graph[a]:
            if color[i] == None:
              color[i] = 1 - color[a]
              queue.append(i)
            elif color[i] == color[a]:
              return False
    return True



isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
