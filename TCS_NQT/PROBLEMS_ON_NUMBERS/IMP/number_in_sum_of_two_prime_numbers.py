def func(a):
    if a ==1:
        return False
    if a ==2:
        return False
    arr = [2]
    for i in range(3,a):
        count = 0
        for j in range(2,i):
            if i%j ==0:
                count+=1
        if count == 0:
            arr.append(i)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == a:
                return True
    return False

            




print(func(11))