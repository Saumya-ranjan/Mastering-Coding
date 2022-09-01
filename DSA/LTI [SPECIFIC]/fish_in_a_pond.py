# VERY LONG BRUTE FORCE 

# def fish_in_a_pond(values,queries):
#     hash = {}
#     hash1= {}
#     for i in values:
#         if str(i) not in hash:
#             hash[str(i)] = []
#     for i in queries:
#         # ATTACKING IN POND B
#         if i[-1] == 2:
#             for j in hash.values():
#                 if i[1] in j:
#                     j.remove(i[1])
#             hash[str(values[i[0]-1])].append(i[1])
        
#         # ATTACKING IN POND A
#         if i[-1] == 1:
#             if values[i[0]-1] > values[i[1]-1]:
#                 hash[str(values[i[0]-1])].extend(hash[str(values[i[1]-1])])
#                 hash[str(values[i[0]-1])].append(str(values[i[1]-1]))
#                 del(hash[str(values[i[1]-1])])
#     for i in hash.keys():
#         if i not in hash1:
#             hash1[i] = len(hash[i])
#     key_max = max(hash1.keys(), key=(lambda k: hash1[k]))
    
#     print(values.index(int(key_max)) +1 , hash1[str(key_max)])

# fish_in_a_pond(4,4,[4,3,2,1],[[2,1,2],[2,2,2],[2,3,2],[3,3,2],[2,4,2],[1,3,1]])


def fish_in_a_pond(pond_a,pond_b,values,queries):
    arr = []
    hash = {}
    for i in range(1,pond_a+1):
        hash[str(i)] = []
    for i in queries:
        # ATTACK ON POND B -->
        if i[-1] == 2:
            for j in hash.values():
                if i[1] in j:
                    j.remove(i[1])
            hash[str(i[0])].append(i[1])
        # ATTACK ON POND A -->
        elif i[-1] == 1:
            if values[i[0]-1] > values[i[1]-1]:
                hash[str(i[0])].extend(hash[str(i[1])])
                hash[str(i[0])].append(str(i[1]))
                del(hash[str(i[1])])
    for v in hash.values():
        arr .append(len(v))
    for i in hash.keys():
        if len(hash[i]) == max(arr):
            print(i , max(arr))
        


fish_in_a_pond(4,4,[4,3,2,1],[[2,1,2],[2,2,2],[2,3,2],[3,3,2],[2,4,2],[1,2,1],[1,3,1]])