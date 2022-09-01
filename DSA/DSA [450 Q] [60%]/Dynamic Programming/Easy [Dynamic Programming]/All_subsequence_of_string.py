arr = []
def func(str1,output):   
    if len(str1) == 0:
        arr.append(output)
        return 
    func(str1[1:],output+str1[0])
    func(str1[1:],output)
func("abcd","" )
print(arr)