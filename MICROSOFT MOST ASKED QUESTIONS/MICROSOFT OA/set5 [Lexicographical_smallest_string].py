def lexicographical(arr):
    # If decreasing then just remove that character
    for i in range(1,len(arr)):
        if ord(arr[i]) < ord(arr[i-1]):
            arr = arr.replace(arr[i-1] ,"")
            return arr
        
print(lexicographical("abcda"))