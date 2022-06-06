def func(nums,index):
    arr = []
    for n,i in zip(nums,index): 
        arr.insert(i,n)
    print(arr)
    

func(['a','b','c','d','e'], [0,1,2,2,1])