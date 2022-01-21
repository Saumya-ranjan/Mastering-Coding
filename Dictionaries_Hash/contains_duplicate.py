# def func(x):                 #big O(n^2)
#     value = 0
#     for i in range(0,len(x)):              
#         for j in range(i+1,len(x)):
#             if x[i]==x[j]:
#                 value = value+1
#             else:
#                 value = value + 0
#     if value>=1:
#         print('true')
#     else:
#         print('false')



# func([1,2,3,4])

def hashtable(x):              #Big O(n)
    
    hash = {}
    value = 0
    for i in range(0,len(x)):
        if x[i] in hash:
            value = value+1
        else:
            hash[x[i]]=i
            value = value+0

    if value>=1:
        print("true")
    else:
        print("false")


hashtable([1,2,3,4,5,4])