def intelligent(n,r):
    count = 0
    for i in str(n):
        count+=int(i)
    
    counter = str(count*r)

    while len(counter)!=1:
        counting = 0
        for i in counter:
            counting += int(i)
        counter = str(counting)

    return counter

print(intelligent(1234,2))