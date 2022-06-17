arr = []
def func(input,output):
    if len(input) ==0:
        arr.append(output)
        return 
    func(input[1:],output+input[0])
    func(input[1:],output)



func("xaayc","")
print(arr)






# def func(str, index = -1, curr = ""):
   
#   # base case
#      if (index == len(str)):
#        return
#      if (len(curr) > 0):
#        print(curr)
 
#      i = index + 1
 
#      while(i < len(str)):
#         curr = curr + str[i]
#         func(str, len(str), i, curr)
#         curr = curr[0:-1]
#         i = i + 1
# func("xxay",)