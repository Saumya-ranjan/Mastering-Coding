# Reverse

def func(arr,l,r):
    if l >= len(arr)/2:
        return arr
    arr[l],arr[r] = arr[r],arr[l]
    return func(arr,l+1,r-1)

print(func([4,5,6,5,7,1,2],0,-1))

# Palindrome  

def func(arr,l,r):
    if arr[l]!=arr[r]:
        return False
    if l >= len(arr)/2:
        return True 
    return func(arr,l+1,r-1)
    

print(func([4,1,2,4],0,-1))