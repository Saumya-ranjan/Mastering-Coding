def func(arr):
    arr2 = []
    arr1 = []
    for i in arr:
        if i not in arr2:
            arr2.append(i)
    for i in range(len(arr)+1):
        for j in range(i+1,len(arr)+1):
            arr1.append(arr[i:j])
    
    arr1.sort(key = len)
    for i in arr1:
        count = 0
        for j in range(len(arr2)):
            if arr2[j] in i:
                count+=1
            if count>=len(arr2):
                return len(i)


        
print(func("AABBBCBBAC"))