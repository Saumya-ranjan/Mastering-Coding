def min_swap(arr):
    arr = list(arr)
    hash=  {}
    for i in range(len(arr)):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            hash[arr[i]]+=1
    odd = 0
    odd_val = '%'  # Any value just for reference
    for i in hash.keys():
        if hash[i]%2 !=0:
            odd+=1
            odd_val = i

    if odd> 1:
        return "Palindrome cannot be Made"
    else:
        count = 0
        def check_first_last(arr, odd_val):
            if len(arr) <2:
                return []
            nonlocal count
            if arr[0] != odd_val:
                elem = arr[0]
            else:
                elem = arr[-1]
                arr = arr[::-1]
            for i in range(len(arr)-1, -1 , -1):
                if arr[i] == elem:
                    count+= len(arr) - 1 - i
                    arr.pop(i)
                    arr.pop(0)
            return arr

        while len(arr)>1:
            if arr[0] == arr[-1]:
                arr.pop(0)
                arr.pop(-1)
            elif arr[0]!= arr[-1]:
                arr = check_first_last(arr , odd_val)
        return count

print(min_swap("xxyy"))