def func(n):
    arr =[]
    for i in str(n):
        arr.append(int(i)**len(str(n)))
    total_sum = sum(arr)
    if total_sum == n:
        print("armstrong Number")
    else:
        print("Not Armstrong")
        


func(1)