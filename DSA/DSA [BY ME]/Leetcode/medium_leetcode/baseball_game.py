def func(ops):
    k = 0
    count = 1
    sum = 0
    arr = []
    for i in range(len(ops)):
        if ops[i] == "C":
            arr.pop(-1)
        elif ops[i]=="D":
            count = 2 * int(arr[-1])
            arr.append(count)
        elif ops[i]=="+":
            sum = int(arr[-2]) + int(arr[-1])
            arr.append(sum)
        elif int(ops[i])<0 or int(ops[i])>0:
            arr.append(ops[i])
    for j in arr:
        k+=int(j)
    print(k)
func(["5","-2","4","C","D","9","+","+"])