#************************************Prints all subsequences***************************************************

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

#**************************************True or False***************************************************************
def subseq(arr):
    k=3 
    arr1 = []
    def func(arr,i,output,k,arr1):
        if i >=len(arr):
            if sum(output) == k:
                arr1.append(tuple(output))
                return 
            return  
        output.append(arr[i])
        func(arr,i+1,output,k,arr1)
        output.remove(arr[i])
        func(arr,i+1,output,k,arr1)
    func(arr,0,[],k,arr1)
    if len(arr1) > 0:
        return True
    return False
    
print(subseq([1,4]))



