# Brute Force

def without_repeating(str1):
    arr = []
    arr2 = []
    for i in range(len(str1)+1):
        for j in range(i+1,len(str1)+1):
            arr.append(str1[i:j])
    for i in arr:
        if len(i) == len(set(i)):
            arr2.append(i)
    arr2.sort(key = len)
    print(arr2[-1],len(arr2[-1]))

            


without_repeating("pwwdwmerhfkew")