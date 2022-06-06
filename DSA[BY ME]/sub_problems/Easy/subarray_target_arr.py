def func(arr,target):
    for i in arr:
        if i in target:
            target.remove(i)
    if len(target) > 0:
        print("False")
    else:
        print("True")

func( [2,4,1,3],[1,2,3,4])