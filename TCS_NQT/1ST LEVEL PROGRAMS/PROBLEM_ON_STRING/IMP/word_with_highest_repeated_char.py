def func(a):
    arr4 = []
    arr3 = []
    arr1 = []
    hash = {}
    arr = []
    for i in a.split():
        arr.append(i)
    for i in arr:
        count = 0
        for j in i:
            if j not in arr1:
                arr1.append(j)
            else:
                count+=1
        arr1.clear()
        arr3.append(count)

    count1 = 0
    for i in arr3:
        hash[i] = arr[count1]
        count1+=1
    for i in sorted(hash.keys()):
        arr4.append(hash[i])
    print(arr4[-1])
        

    


        
                
            




func("abcdefghij google microsoft")