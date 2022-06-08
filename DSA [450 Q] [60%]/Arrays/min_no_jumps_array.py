def func(arr):
    count = 0
    x = 0
    for i in range(0,len(arr)):
        x+= arr[x]
        count+=1
        if x>=len(arr)-1:
            return count

   
        




print(func([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]))