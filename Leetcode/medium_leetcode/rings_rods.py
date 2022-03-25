def func(rings):
    hash = {}
    arr = []
    num = []
    for i in range(len(rings)):
        if i%2 == 0:
            arr.append(rings[i])
        else:
            num.append(rings[i])
    for i,j in zip(arr,num):
        if j not in hash:
            hash[j] = str(i)
        else:
            hash[j] += str(i)
    count = 0
    for i in hash.values():
        if 'G' in i and 'R' in i and 'B' in i:
            count+=1
    print(count)
func("B0R0G0R9R0B0G0")