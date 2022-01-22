# def func(x):
# #   This code is big O(n) time complex

#     target = int(input("enter target: "))    
#     # print( x[target:]+x[:target])          # right rotation of array
#     arr = x[::-1]                           #left rotation of array by given target
#     arr1 = arr[:target]                     #totally my way to solve it
#     y = arr1[::-1]
#     arr2 = arr[target:]
#     z= arr2[::-1]
#     print( y+z)      #list 
    
        
# func([1,2,3,4,5,7,5,6,6])

def func(x):
    arr = []
    target = int(input("Enter the Number: "))
    for i in range(target):
        x.insert(0,x[-1])
        x.pop(-1)
    
    print(x)
        


func([1,2,3,4,5,6,7])





