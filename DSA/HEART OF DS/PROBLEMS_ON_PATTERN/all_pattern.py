# 1) Pattern 1

# *
# **
# ***
# ****

# a = int(input())
# for i in range(a+1):
#     for j in range(i):
#         print("*" , end = " ")
#     print()


# **********************************************************************************

# 2) Pattern 2

# ****
# ***
# **
# *

# a = int(input())
# count = a
# for i in range(a):
#     for j in range(count):
#         print('*' , end = '')
#     count-=1
#     print()

# **********************************************************************************************

# 3) Pattern 3

# *****
# *****
# *****
# *****
# *****

# a = int(input())
# for i in range(a):
#     for j in range(a):
#         print('*' ,end = '')
#     print()

# ****************************************************************************************

# 4) Pattern 4

# 1
# 12
# 123
# 1234
# 12345

# a = int(input())
# for i in range(a+1):
#     count = 1
#     for j in range(i):
#         print(count , end ='')
#         count+=1
#     print()

# **********************************************************************************

# 5) Pattern 5

# *
# **
# ***
# ****
# ***
# **
# *

# a = int(input())
# if a %2 != 0:
#     # Upper
#     upper = int(a/2)+1
#     for i in range(upper+1):
#         for j in range(i):
#             print('*' , end = '')
#         print()
#     # Lower
#     lower = a - upper
#     counter = lower
#     for i in range(lower):
#         for j in range(counter):
#             print('*' , end = '')
#         counter-=1
#         print()


# **************************************************************************************************

# 6) Pattern 6

#     *
#    **
#   ***
#  ****

# 1st Method:

# a = int(input())
# spaces = a
# for i in range(a+1):
#     for k in range(spaces):
#         print(end = ' ')
#     spaces-=1
#     # print('*')
#     for j in range(i):
#         print('*', end = '')
#     print()

# 2nd Method:

# a = int(input())
# count = 1
# counter=a-1
# for i in range(a):
#     for j in range(1):
#         print(str(' '*counter)+ str(count * '*'),end='')
#     count+=1
#     counter-=1
#     print()

# ***************************************************************************************************************

# 7) pattern 7

#     *
#    * *
#   * * *
#  * * * *
#   * * *
#    * *
#     * 

# a = int(input())
# # UPPER
# upper = int(a/2)+1
# spaces = upper-1
# for i in range(1 ,  upper+1):
#     for k in range(spaces):
#         print(end= ' ')
#     spaces-=1
#     for j in range(i):
#         print('*' , end = ' ')
#     print()
# #LOWER
# lower = upper-1
# spaces = lower-1
# b = lower
# spaces_lower = 1
# for i in range(lower):
#     for k in range(spaces_lower):
#         print(end=' ')
#     spaces_lower+=1
#     for j in range(b):
#         print('*' , end=' ')
#     b-=1
#     print()

# ******************************************************************************************************

# 8) pattern 8

# * * * * *
# *       *
# * * * * *
#     *
#     *


# a= int(input())

# # For Rectangle
# rec =  (int(a/2) + 1)
# spaces = a

# for i in range(1,rec+1):
#     if i == 1:
#         for j in range(a):
#             print('*' , end =' ')
#         print()
#     elif i == rec:
#         for j in range(a):
#             print('*' , end =' ')
#         print()
#     else:
#         print('*' , end=' ')
#         for k in range(spaces-2):
#             print(end='  ')
#         print('*')
        
# # linear line:
# space_line = a-1
# for i in range(a-rec):
#     for j in range(space_line):  
#         print(end=' ')
#     print('*')


# *****************************************************************************


# 9) pattern 9

#     *
#     *
# * * * * *
# *       *
# * * * * *


# a= int(input())
# rec =  (int(a/2) + 1)
# spaces = a 
# # linear line:
# space_line = a-1
# for i in range(a-rec):
#     for j in range(space_line):  
#         print(end=' ')
#     print('*')

# # Rectangle: 

# for i in range(1,rec+1):
#     if i == 1:
#         for j in range(a):
#             print('*' , end =' ')
#         print()
#     elif i == rec:
#         for j in range(a):
#             print('*' , end =' ')
#         print()
#     else:
#         print('*' , end=' ')
#         for k in range(spaces-2):
#             print(end='  ')
#         print('*')
        
# *******************************************************************************************************

# 10) pattern 10:

# 12345677654321
# 123456**654321
# 12345****54321
# 1234******4321
# 123********321
# 12**********21
# 1************1
# > 

# n = int(input('hello give ur input:'))
# count = 1
# counter = 0
# terminate = n
# for i in range(1,n+1):
#     print(i, end='' )
# for j in range(n, 0,-1):
#     print(j , end='')
# print()
# for i in range(n-1):
#     arr = []
#     arr1 =[]
#     for j in range(n):
#         if count == terminate:
#             terminate-=1
#             count = 1
#             arr.append(str('*'))
#             print('*' , end = '')
#             arr.append(str(counter*'*'))
#             print(counter * '*', end='')
#             counter+=1
#             print(''.join(arr) ,end='')
#             break
#         arr1.append(str(count))
#         print(count , end = "")
#         count+=1
#     print(''.join(arr1)[::-1], end='')
#     print()
