def max_of_subarray(arr,target):
    # arr1 = []
    # for i in range(len(arr)):
    #     if i+target <= len(arr):
    #         arr1.append(max(arr[i:i+target]))
    # print(arr1)
    arr1 = []
    for i in range(len(arr)):
        j = i+target
        if j <=len(arr):
            arr1.append(max(arr[i:j]))
    print(arr1)





max_of_subarray([12,-1,-7,8,-15,30,16,28,45,34,24,24],3)