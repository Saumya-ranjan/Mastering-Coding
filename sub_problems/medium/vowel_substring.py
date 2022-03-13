def func(word):
    arr = []
    count = 0
    for i in range(len(word)+1):
        for j in range(i+1, len(word)+1):
            arr.append(set(word[i:j]) == set('aeiou'))
    for i in arr:
        if i == True:
            count+=1
    print(count)


func("aeiouu")