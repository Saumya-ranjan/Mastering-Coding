# Brute Force -->  Not By Sliding Window 
# SO here would Mostly Be a case of TLE

def longest_substring(str1,target):
    arr = []
    arr2 = []
    for i in range(len(str1)+1):
        for j in range(i+1,len(str1)+1):
            arr.append(str1[i:j])
    for i in arr:
        arr1 = []
        for j in i:
            if j not in arr1:
                arr1.append(j)
        if len(arr1) == target:
            arr2.append(i)
    arr2.sort(key = len)
    print(len(arr2[-1]),arr2[-1])

longest_substring("aabacbebebe",3)








