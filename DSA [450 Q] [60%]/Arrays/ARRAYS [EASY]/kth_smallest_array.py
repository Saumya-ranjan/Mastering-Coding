def func(arr,target):
    arr.sort()
    if (target> len(arr)):
        print("Invalid")
    else:
        print(arr[target-1])
    


func([7,10, 4, 20, 15],int(input("what is the element: ")))