#BruteForce

def func(arr):
    hash = {}
    arr1= []
    for i in arr:
        if i not in hash:
             hash[i] =1
        else:
            hash[i]+=1
    for i in hash.values():
        arr1.append(i)
    arr1.sort()
    for i in hash.keys():
        if hash[i] == arr1[-2]:
            print(i)



func(['aaa','bbb', 'ccc', 'bbb', 'aaa', 'aaa'])