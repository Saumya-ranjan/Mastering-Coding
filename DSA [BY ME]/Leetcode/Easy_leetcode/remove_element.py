# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


def func(x):
    val=int(input("Enter a NUmber: "))
    count = 0
    for i in range(len(x)):
        if x[i]!=val:
            x[count]=x[i]
            count+=1
    print(count)
    return count

print(func([1,3,3,3,4,5,6,2]))




# def func(x):          #o(n)  My Code 
#     arr =[]
#     count = 0
#     val = int(input("Enter a Number: "))
#     for i in x:
#         if i == val:
#             continue
        
#         else:
#             count+=1
#             arr.append(i)
#     print(count)
#     print(arr)
    
# func([1,2,3,3,3,4,5])

