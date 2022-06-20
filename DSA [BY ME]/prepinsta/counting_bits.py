
def func(x):
    arr = [0]
    if x > 0:
        while len(arr) < x + 1:
            arr.extend([x+1 for x in arr])
        
    print(arr[0:x+1])
        



func(5)