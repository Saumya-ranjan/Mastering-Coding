def reve(x):
    arr = []
    if x == "":
        print("Nothing in string")
    # elif(x.isalpha()==True):
    #     print("hello")
    else:
        # print(x[::-1])        # 1st option
        for i in x:       
            arr.append(i)
        arr.reverse()
        print(''.join(arr))       # making list as an string




reve(input("Enter a string: "))