# Using Array   

# def func(A):
#     num = 0
#     upper = 0
#     lower = 0
#     special = 0
#     if len(A)>=8 and len(A)<=15:
#         for i in range(len(A)):
#             if A[i].isnumeric() :
#                 num+=1               
#             elif A[i].isupper():
#                 upper+=1
#             elif A[i].islower():
#                 lower+=1
#             elif A[i] in '@,#,%,&,!,$':
#                 special+=1
#     else:
#         print('0')
#     if upper>0 and lower>0 and special>0 and num>0:
#         print('1')
#     else:
#         print('0')
    
# func('V87*FFrbGj6')



# Using Hash

def func(x):
    hash = {}
    for i in x:
        if i.isupper():
            hash['upper'] =  i
        elif i.islower():
            hash['lower'] = i
        elif i.isnumeric():
            hash['num'] = i
        elif i in '@#$%^&*_':
            hash['special'] = i
    count = 0
    for v in hash.keys():
        if v=='upper' or v == 'lower' or v == 'num' or v=='special':
            count+=1
    if count == 4:
        print('1')
    else:
        print('0')



        

func('dowhf123A')

