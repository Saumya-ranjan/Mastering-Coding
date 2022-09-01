def missing_repeating(arr):
    arr1= []
    missing = 0
    repeating = 0
    for i in range(1,len(arr)+1):
        if i not in arr:
            missing = i
        if arr[i-1] not in arr1:
            arr1.append(arr[i-1])
        elif arr[i-1] in arr1:
            repeating = arr[i-1]
    print(repeating, missing)
        


missing_repeating([1,2, 3,4,5,6,7,8,9,10,10,12])