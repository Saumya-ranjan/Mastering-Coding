#******************************** Print the subsequence of string *******************************************************
def func(s):
    def subseq(s,output):
        if len(s) == 0:
            print(output)
            return 
        subseq(s[1:],output+s[0])
        subseq(s[1:],output)

    res = subseq(s,"")
    return res
func("abc")


#********************************** Counting all subsequences *******************************************************
def func(s):
    arr = []
    def subseq(s,output):
        if len(s) == 0:
            arr.append(output)
            return 
        subseq(s[1:],output+s[0])
        subseq(s[1:],output)
    res = subseq(s,"")
    return len(arr)
print(func("abc"))

