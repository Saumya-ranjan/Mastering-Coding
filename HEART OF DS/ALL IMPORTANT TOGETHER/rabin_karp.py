def func(str1,str2):
    arr = []
    for i in range(len(str1)+1):
        for j in range(i+1,len(str1)+1):
            if str1[i:j] == str2:
                arr.append(i)
    return arr
                



    



func("AABAACAADAABAABA","AABA")