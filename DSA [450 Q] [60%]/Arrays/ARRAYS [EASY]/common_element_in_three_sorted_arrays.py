def func(arr1,arr2,arr3):
    hash = []
   
    for i in set(arr1):
        if i in set(arr2) and i in set(arr3):
            hash.append(i)
    return sorted(hash)
            
    


print(func([1, 5, 10, 20, 40, 80],[6, 7, 20, 80, 100],[3, 4, 15, 20, 30, 70, 80, 120]))