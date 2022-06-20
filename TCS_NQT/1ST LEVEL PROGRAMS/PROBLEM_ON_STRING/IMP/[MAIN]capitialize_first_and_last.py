def func(arr):
    arr2 = ""
    arr1 = []
    for i in arr.split():
        arr1.append(i)
    
    for i in arr1:
        arr2+= " "
        for j in range(len(i)):
            if j == 0:
                arr2+=i[j].upper()
            elif j == len(i)-1:
                arr2+=i[j].upper()
            else:
                arr2+=i[j]
    print(arr2.lstrip())

func("take u forward is awesome")