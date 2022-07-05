def substring(arr,target):
    count1=0
    for i in arr:
        if i ==target:
            count1+=1
    if count1 ==1:
        return -1
    elif count1 == 0:
        return 0
    else:
        count = 0
        arr1= []
        arr2 = []
        for i in range(len(arr)+1):
            for j in range(i+1,len(arr)+1):
                arr1.append(arr[i:j])
        for i in arr1:
            if i[0] == i[-1] == target:
                arr2.append(i)
        arr2.sort(key = len)
        for i in arr2[-1]:
            if i!=target and i.isalnum():
                count+=1
        return count

print(substring( "my name is granar", "a" ))