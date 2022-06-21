# Prints all subsequences

# def func(arr,i,output,k):
#     if i >=len(arr):
#         if sum(output) == k:
#             print(output)
#             return output
#         return 
#     output.append(arr[i])
#     func(arr,i+1,output,k)
#     output.remove(arr[i])
#     func(arr,i+1,output,k)

# func([1,2,3],0,[],3)

# Same but print in one value: 
# arr1 = []
# def func(arr,i,output):
#     if i >=len(arr):
#         arr1.append(tuple(output))
#         return 
#     output.append(arr[i])
#     func(arr,i+1,output)
#     output.remove(arr[i])
#     func(arr,i+1,output)

# func([1,2,3],0,[])
# count = 0
# k = 3
# arr2 = []
# for i in arr1:
#    arr2.append(sum(i))
# for i in arr2:
#     if i == 3:
#         count+=1
# print(count)


def func(arr,i,output,k,count):
    if i >=len(arr):
        if sum(output) == k:
            count+=1
            print(count)
            return output
        return 
    output.append(arr[i])
    func(arr,i+1,output,k,count)
    output.remove(arr[i])
    func(arr,i+1,output,k,count)

func([1,2,3,3],0,[],3,0)