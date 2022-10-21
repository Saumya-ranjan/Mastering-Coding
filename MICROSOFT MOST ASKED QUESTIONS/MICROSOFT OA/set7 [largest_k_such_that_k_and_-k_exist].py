def largest(arr):
    arr.sort()
    arr = arr[::-1]
    for i in range(len(arr)):
        if arr[i] > 0:
            if -arr[i] in arr:
                return arr[i]
    return 0


print(largest([1, 2, 3, -4]))