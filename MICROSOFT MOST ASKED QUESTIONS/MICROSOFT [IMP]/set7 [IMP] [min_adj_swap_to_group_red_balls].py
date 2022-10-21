# My observation -- >

def swap_group_red(arr):
    res = 0
    reds = []
    # If Found 2 red then count there mid whites and add it to result
    for i in range(len(arr)):
        if arr[i] == 'R':
            reds.append(i)
    if len(reds) ==1:
        return 0
    
    if len(reds) % 2 == 0:
        for i in range(int(len(reds)/2)):
            slet = -1
            for j in range(reds[i],reds[slet]):
                if arr[j] == 'W':
                    res+=1
            slet-=1
    else:
        reds.pop(int(len(reds)/2))
        for i in range(int(len(reds)/2)):
            slet = -1
            for j in range(reds[i],reds[slet]):
                if arr[j] == 'W':
                    res+=1
            slet-=1
    
    print(res)

            




swap_group_red("WWRWWWRWR")