def func(arr):
    arr1 = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            arr1.append(arr[j] - arr[i])
    print(max(arr1))    # --> Correct [198/211] cases passed
    

func([7,1,5,3,6,4])