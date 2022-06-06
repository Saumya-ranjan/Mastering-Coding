def func(x):
    x = x.replace(' ','')
    arr = []
    for i in x:
        arr.append(i)
    print(arr)
    for k in range(len(arr)):
        for j in range(k+1,len(arr)):
            if arr[k] == '{' and arr[j] == '}':
                arr[k] = ""
                arr[j] = ""
            elif arr[k] == '(' and arr[j] == ')':
                arr[k] = ""
                arr[j] = ""
            elif arr[k] == '[' and arr[j] == ']':
                arr[k] = ""
                arr[j] = ""
    print(arr)
    count = 0
    for m in '{]}[()':
        if m in arr:
            count+=1
        else:
            count+=0  
    if count == 0:
        print("valid")
    else:
        print("Not Valid")

func('{ { ( { } ) } }')