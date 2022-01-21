def func(x):
  
    
    target = int(input("enter target: "))
    # print( x[target:]+x[:target])          # right rotation of array
    arr = x[::-1]                           #left rotation of array by given target
    arr1 = arr[:target]                     #totally my way to solve it
    y = arr1[::-1]
    arr2 = arr[target:]
    z= arr2[::-1]
    print(y+z)
    
        
func([1,2,3,4,5,7])