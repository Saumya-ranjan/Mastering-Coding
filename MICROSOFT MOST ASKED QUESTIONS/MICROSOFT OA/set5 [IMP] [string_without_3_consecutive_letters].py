def without_consecutive(arr):
    res = arr[0:2]
    for i in range(2 , len(arr)):
        if arr[i] != arr[i-1] or arr[i] != arr[i-2]:
            res+= arr[i]
    return res

print(without_consecutive("uuuuxaaaaxum"))