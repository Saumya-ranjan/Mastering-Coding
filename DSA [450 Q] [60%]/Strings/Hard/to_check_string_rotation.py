# BY SUBSTRING
# When there is rotation question do it by substring

def func(str1,str2):
    arr = []
    arr1 = []
    str3 = str1+str1
    for i in range(len(str3)+1):
        for j in range(i+1,len(str3)+1):
            arr.append(str3[i:j])
    # if str2 in arr:
    #     return True 
    # return False
    for i in arr:
        if len(i) == len(str1):
            arr1.append(i)
    return (arr1)

print(func("ABACD","CDABA"))



#GENERAL (BRUTEFORCE)

# def func(str1,str2):
#     arr = []
  
#     for i in str1:
#         arr.append(i)
#     for i in str1[::-1]:
#         arr.insert(0,i)
#         arr.pop(-1)
#         a = ""
#         for i in arr:
#             a += str(i)
#         if a == str2:
#             return True
#     return False

# print(func("ABACD","CDABA"))