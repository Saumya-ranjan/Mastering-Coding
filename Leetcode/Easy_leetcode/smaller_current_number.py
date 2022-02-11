# def func(x):                              #o(n^2)
    
#     arr = []
#     for i in range(len(x)):
#         count = 0
#         for j in range(len(x)):
#             if x[i]>x[j]:
#                 count+=1
#         arr.append(count)
#     print(arr)
        


def func(x):                 #o(n)
    hash = {}
    temp = sorted(x)
    res = []
    for i in range(len(temp)):
        if temp[i] not in hash:
            hash[temp[i]]=i
    for i in range(len(x)):
        res.append(hash[x[i]])
    print(res)
            


func([3,3,8,1,2,2,3])