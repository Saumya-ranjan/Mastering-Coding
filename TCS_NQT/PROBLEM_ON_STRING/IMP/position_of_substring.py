def func(a,b):
    # count = 0
    # arr = []
    # for i in range(len(a)+1):
    #     for j in range(i+1,len(a)+1):
    #         arr.append(a[i:j])
    # for i in arr:
    #     if len(i) == 1:
    #         count+=1
    #     elif i == b:
    #         count-=1
    #         break
    # print(count)
    c = ""
    if b in a:
        a = a.replace(b," ")
    else:
        print("-1")
    for i in range(len(a)):
        if a[i]!=" ":
            c+=a[i]
        else:
            break
    print(len(c))

func("takeuforward","forward")