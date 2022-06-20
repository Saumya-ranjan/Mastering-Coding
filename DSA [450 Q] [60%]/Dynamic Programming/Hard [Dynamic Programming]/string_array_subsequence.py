# A contigious and non contigious sequence that follows the order

#                                  [ARRAYS]

def func(arr,index,output):
    if index >= len(arr):
        print(output)
        return
    # 1st this executes giving value of 312,31,32,3
    output.append(arr[index])
    func(arr,index+1,output)      
    # Now this executes with 12,1,2,[]
    output.remove(arr[index])    # [3,1,2] then it removes 2 going in deep iterative.
    func(arr, index + 1, output)
    
func([3,1,2],0,[])


#                                  [STRINGS]

def func(arr,output):
    if len(arr) == 0:
        print(output)
        return
    func(arr[1:],output+arr[0]) 
    func(arr[1:],output)
    
func('abc','')