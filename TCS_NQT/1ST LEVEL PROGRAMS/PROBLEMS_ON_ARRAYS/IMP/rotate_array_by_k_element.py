# no tle form:
def array(arr,rotate):
    while rotate > len(arr):
        rotate -= len(arr)
    return arr[rotate:] + arr[:rotate]



print(array([1,2,3,4,5],11))


# def func(arr,k):
#     for i in range(k):
#         arr.append(arr[0])
#         arr.pop(0)
        

#     print(arr)
#     # for i in range(k):
#     #     arr.insert(0,arr[-1])
#     #     arr.pop(-1)
#     # print(arr)



# func([1,2,3,4,5,6,7],2)