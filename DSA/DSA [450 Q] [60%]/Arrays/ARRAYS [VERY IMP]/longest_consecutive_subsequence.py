# Brute Force Method 

def func(arr):
    print(arr)
    arr2 = set(arr)
    arr.clear()
    for i in arr2:
        arr.append(i)
    arr.sort()
    arr1 = []
    curr =  arr[0]
    count = 1
    for i in arr[1:]:
        if i-1 == curr:
            curr = i
            count+=1
            arr1.append(count)
            
        else:
            count = 1
            curr = i
    
    arr1.append(count)
    print(arr1)
    print(max(arr1))
    
    
func([21 ,137 ,140, 54 ,30 ,98, 125, 81 ,116, 2 ,31 ,139 ,196, 4 ,138 ,180 ,18 ,170 ,62 ,12 ,179 ,177, 85 ,136 ,104 ,176, 83, 7 ,159, 57 ,144, 99])

