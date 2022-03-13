# def func(s):   #brute force method
    
#     count = 0
#     arr1 = []
#     arr = []
#     arr2 = []
#     for i in range(len(s)+1):
#         for j in range(i+1,len(s)+1):
#             a = s[i:j]
#             arr.append(a)
#     for i in arr:
#         if len(i) %2 ==0:
#             if i.count('1') == i.count('0'):
#                 arr1.append(i)
#     for i in arr1:
#         if '0' * int(len(i)/2) in i and '1' * int(len(i)/2) in i:
#             arr2.append(i)
        
#     for i in arr2:
#         count+=1
#     print(count)
            
            
# #time exceeded
            

                       

# func("11001111010000011101111001101")

