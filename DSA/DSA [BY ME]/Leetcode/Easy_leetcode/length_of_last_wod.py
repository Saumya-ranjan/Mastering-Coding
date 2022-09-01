def func(s):
    count = -1
    arr = []
    for i in s.split(" "):
        arr.append(i)
    while len(arr[count])==0:
        count =count-1
        
        
    print(len(arr[count]))
       

func("   fly me   to   the moon  ")