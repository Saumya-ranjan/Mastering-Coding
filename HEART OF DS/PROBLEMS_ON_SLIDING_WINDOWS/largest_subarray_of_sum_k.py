# For all Numbers -ve and +ve
def largest_subarray(arr,target):
    arr1 = []
    arr2 = []
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    for i in arr1:
        if sum(i) == target:
            arr2.append(i)
    arr2.sort(key = len)
    print(len(arr2[-1]))




largest_subarray([4,1,1,-2,1,5],5)