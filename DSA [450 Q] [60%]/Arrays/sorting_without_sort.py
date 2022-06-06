#Without Sorting

def func(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:

                arr[i],arr[j] = arr[j],arr[i]       #Main
          
    print(arr)
            


func([2,6,1,4,8,6,7,10])