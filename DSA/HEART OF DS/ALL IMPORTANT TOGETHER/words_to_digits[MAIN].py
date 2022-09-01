def func(n):
    hash ={ 0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    hash1={ 10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",
    15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen",20:"twenty",
    30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred"}
    hash2={ 100:"hundred"}
    a = str(n)
    if len(a) ==1 :
        return hash[int(a)]
    if len(a) == 2:
        if int(a) in hash1:
            return hash1[int(a)]
        else:
            return str(hash1[int(str(a[0]+'0'))]) +' ' + str(hash[int(a[1])])
    if len(a) == 3:
        # if int(a) in hash:
        #     return hash[int(a)]
        # elif int(str(a[1])+str(a[2])) in hash1:
        #     return str(hash[int(a[0])])+" "+str(hash2[100])+ " "+ str(hash1[int(str(a[1])+str(a[2]))])
        # elif int(a[1]) == 0:
        #     return str(hash[int(a[0])])+" "+str(hash2[100])+ " " +str(hash[int(a[2])])
        # else:
        #     return str(hash[int(a[0])])+" "+str(hash2[100])+ " "+str(hash1[int(str(a[1]+'0'))]) +' ' + str(hash[int(a[2])])
        b = str(a[0])
        a = str(a[1:])
        if int(a) in hash1:
            return str(hash[int(b)])+" "+str(hash2[100])+ " "+ hash1[int(a)]
        elif int(a[0]) == 0:
            return str(hash[int(b)])+" "+str(hash2[100])+ " "+ str(hash[int(a[1])])
        else:
            return str(hash[int(b)])+" "+str(hash2[100])+ " "+ str(hash1[int(str(a[0]+'0'))]) +' ' + str(hash[int(a[1])])
        
print(func(506))