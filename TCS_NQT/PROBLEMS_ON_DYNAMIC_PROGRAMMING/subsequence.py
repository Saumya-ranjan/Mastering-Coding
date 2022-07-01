# def func(str1):
#     arr1 = []
#     def subsequence(str1,arr,arr1):
#         if len(str1) == 0:
#             arr1.append(arr)
#             return 
#         subsequence(str1[1:],arr+str1[0],arr1)
#         subsequence(str1[1:],arr,arr1)

#     subsequence(str1,"",arr1)
#     return arr1
# print(func("astra"))

def func(arr,i,output,k):
    if i >=len(arr):
        if sum(output) == k:
            print(output)
            return output
        return 
    output.append(arr[i])
    func(arr,i+1,output,k)
    output.remove(arr[i])
    func(arr,i+1,output,k)

func([1,2,3],0,[],3)