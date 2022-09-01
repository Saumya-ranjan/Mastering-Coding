#Substring
# Brute Force Method

def count_occurences_anagram(str1,str2):
    arr2 = []
    arr = []
    hash = {}
    count= 0
    for i in range(len(str2)+1):
        for j in range(i+1,len(str2)+1):
            arr.append(str2[i:j])
    for i in str1:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] += 1
    for i in arr:
        if len(i) == len(str1):
            arr2.append(i)
    for i in arr2:
        hash1 = {}
        for j in i:
            if j not in hash1:
                hash1[j] = 1
            else:
                hash1[j]+=1
        if hash1 == hash:
            count+=1
    print(count)
    
count_occurences_anagram('aaba','aabaabaa')



   

        
    
count_occurences_anagram('FOR','FORROFFROGWGRFORFO')
