def func(s):
    arr = []
    arr1= []
    arr2 = []
    for i in range(len(s)+1):
        for j in range(i+1,len(s)+1):
            arr.append(s[i:j])
    for i in arr:
        a = s+i
        if a == a[::-1]:
            arr1.append(i)
    for i in arr1:
        if i ==i [::-1]:
            arr2.append(i)
    arr2.sort(key = len)
    print(arr2[0])

a = int(input())
s = []
for i in range(a):
    n = input()
    s.append(input())
count =1
for i in s:
    print("Case #"+ str(count)+":" ,end ='')
    func(i)
    count+=1

