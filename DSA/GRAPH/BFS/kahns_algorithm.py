def kahnsalgo(graph):
    # Bfs:
    visited = []
    queue = []
    ans = []
    indegree = [0]* len(graph)
    
    for i in range(len(graph)):
        for j in graph[i]:
            indegree[j]+=1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            visited.append(i)
            queue.append(i)
    
    while queue:
        u = queue.pop(0)
        ans.append(u)

        for i in graph[u]:
            indegree[i] -= 1
                # If in-degree becomes zero, add it to queue
            if indegree[i] == 0 and i not in visited:
                queue.append(i)

    if len(ans) != len(graph):
        print("cycle exist")
    else:
        print(ans)



kahnsalgo([[],[],[3],[1],[0,1],[0,2]])