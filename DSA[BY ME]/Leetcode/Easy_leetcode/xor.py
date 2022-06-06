# def func(encoded , first):
#     print(2 ^ 3)

#     # [1,0 <- first, 2<-first]

# func([77083],28218)

def func(encoded, first):
    arr = [first]
    for i in encoded:
        arr.append(i ^ first)
        first = i^first

    print(arr)


func([6,2,7,3],  4)