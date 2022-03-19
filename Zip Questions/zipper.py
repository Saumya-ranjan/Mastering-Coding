def func(nums,index):
    arr = []
    for n,i in zip(nums,index): 
        arr.insert(i,n)
    print(arr)
    

func([0,1,2,3,4], [0,1,2,2,1])