# GETTING SHORTEST VALUE IN GRAPH: 

def djikstra(graph , src):
    # distance array, priority Queue:
    distance = [float('inf') for _ in range(len(graph))]
    
    # Priority QUEUE:
    priority = []
    visited = []

    if [0,src] not in priority:
        priority.append([0,src])
        distance[src] = 0
    
    if len(graph[src])!=0 :
        while len(priority)!=0:
            for i in graph[src]:
                if [(i[1]+distance[src]) , (i[0])] not in visited or [(i[1]+distance[src]) , (i[0])] not in priority:
                    priority.append([(i[1]+distance[src]) , (i[0])])
                if i[1]+distance[src] < distance[i[0]]:
                    distance[i[0]] = i[1]+distance[src]
            visited.append(priority[0])
            priority.pop(0)
            priority.sort(key = lambda s:s[0])
            src = priority[0][1]
    

    print(priority , distance)

    


djikstra([[(1,2),(3,1)] , [(0,2),(2,4),(4,5)] , [(3,3),(1,4),(4,1)] , [(0,1),(2,3)] , [(1,5),(2,1)]] , 2)