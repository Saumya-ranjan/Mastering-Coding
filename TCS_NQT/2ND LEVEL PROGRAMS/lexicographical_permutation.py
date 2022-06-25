# #  Strings

# def func(arr):
#     arr = sorted(arr)
#     output = ""
#     arr1 = []
#     def permutation(arr,output,arr1):
#         if len(arr) == 0:
#             arr1.append(output)
#         for i in range(len(arr)):
#             new_output = output+arr[i]
#             new_input = arr[:i] + arr[i+1:]
#             permutation(new_input,new_output,arr1)

#     permutation(arr,output,arr1)
#     return arr1
# print(func('abc'))


# Arrays

# def permutation(bar):
#     arr = []
#     for i in bar:
#         arr.append(i)
#     if len(arr) == 0:
#         return []
#     if len(arr) == 1:
#         return [arr]
#     l = []
#     for i in range(len(arr)):
#        remLst = arr[:i] + arr[i+1:]
#        for p in permutation(remLst):
#            l.append([arr[i]] + p)
#     return l
# print(permutation('abc'))


def permutation(arr):
    
    def func(arr):
        
        arr = sorted(arr)
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [arr]
        arr1 = []
        for i in range(len(arr)):
            remaining = arr[:i] + arr[i+1:]
            for j in func(remaining):
                arr1.append([arr[i]]+j)
        return arr1
    res = func(arr)
    for i in range(len(res)):
        if res[i] == arr:
            if i == len(res)-1:
                return res[0]
            else:
                return res[i+1]
              
print(permutation([1,2,3]))