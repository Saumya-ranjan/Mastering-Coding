# GETTING SHORTEST VALUE IN GRAPH: 

def djikstra(graph , node , startNode):
    visited = set()
    priority = []
    result = []

    for u,v,w in graph:
        if u == startNode:
            priority.append([w,v])
    priority.sort(key = lambda x: x[0])
    visited.add(startNode)
    result.append([startNode,startNode,0])

    while len(priority)!=0:
        if priority[0][1] not in visited:
            for i in graph:
                if i[0] == priority[0][1]:
                    priority.append([i[2] + priority[0][0] , i[1]])
                    visited.add(i[0])
                    priority.sort(key = lambda x: x[0])
                    result.append([startNode , i[1] ,i[2] + priority[0][0] ])
            priority.pop(0)
                    
        else:
            result.append([])
            priority.pop(0)

    print(result)

djikstra([[2,1,1],[2,3,1],[3,4,1]] , 4 , 2)








    # distance array, priority Queue:
    # distance = [float('inf') for _ in range(len(graph))]
    
    # # Priority QUEUE:
    # priority = []
    # visited = []

    # if [0,src] not in priority:
    #     priority.append([0,src])
    #     distance[src] = 0
    
    # if len(graph[src])!=0 :
    #     while len(priority)!=0:
    #         for i in graph[src]:
    #             if [(i[1]+distance[src]) , (i[0])] not in visited or [(i[1]+distance[src]) , (i[0])] not in priority:
    #                 priority.append([(i[1]+distance[src]) , (i[0])])
    #             if i[1]+distance[src] < distance[i[0]]:
    #                 distance[i[0]] = i[1]+distance[src]
    #         visited.append(priority[0])
    #         priority.pop(0)
    #         priority.sort(key = lambda s:s[0])
    #         src = priority[0][1]
    

    # print(priority , distance)

    

# [node1 --> node 2 --> weight taken ]  
