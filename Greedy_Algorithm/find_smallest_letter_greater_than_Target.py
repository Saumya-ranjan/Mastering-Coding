# def func(letters,target):             #1st bruteforce method
#     hash = {}
#     arr = []
#     for i in letters:
#         arr.append(i)
#     arr.append(target)
#     arr.sort()   
#     for j in arr:
#         if j not in hash:
#             hash[j] = 1
#         else:
#             hash[j]+=1
#     arr.clear()
#     for k in hash.keys():
#         arr.append(k)
#     if target == arr[-1]:
#         return arr[0]   
#     for j in range(len(arr)):
#         if target == arr[j]:
#             return arr[j+1]

# print(func(["c","f","e"], "f"))


def func(x,y):
    arr = []  
    x.append(y)
    x.sort()
    for i in x:
        if i not in arr:
            arr.append(i) 
    for i in range(len(arr)):
        if y == arr[i]:
            if arr[i] == arr[-1]:
                return arr[0]
            else:
                return arr[i+1]


print(func(["c","c","f","e"], "a"))