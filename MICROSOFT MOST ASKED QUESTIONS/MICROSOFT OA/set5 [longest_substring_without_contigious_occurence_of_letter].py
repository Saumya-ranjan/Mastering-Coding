def substring_2_occurence(arr):
    l = 0
    count = 0
    for r in range(2 , len(arr)):
        if r == len(arr) - 1 and arr[r] != arr[r-2]:
            if r+1-l > count:
                str = arr[l:r+1]

        elif arr[r] == arr[r-1] == arr[r-2]:
            if r - l > count:
                str = arr[l:r]
                count+= r-l
            l = r-1
    return str


print(substring_2_occurence("aabbaabbaabbaaa"))