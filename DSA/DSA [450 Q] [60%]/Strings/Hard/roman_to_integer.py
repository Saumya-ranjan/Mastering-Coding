def func(S):
    value = 0
    a = "IVXLCDM"
    hash = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    hash1 ={}
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            hash1[str(a[i])+str(a[j])] = int(hash[a[j]]-hash[a[i]])
    for i in hash1.keys():
        if i in S:
            value+=hash1[i]
            S = S.replace(i,"")
    for i in S:
        if i in hash:
            value+=hash[i]
    print(value)



func("IX")