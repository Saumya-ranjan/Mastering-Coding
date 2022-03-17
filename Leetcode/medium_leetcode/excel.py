def func(s):
    arr = []
    arr1 = []
    arr2 = []
    letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = s.split(':')
    for i in s:
        arr.append(i[0])
        arr1.append(i[1])
  
    letter = letter[letter.index(arr[0]):letter.index(arr[1])+1]
    for i in letter:
        for j in range(int(arr1[0]),int(arr1[1])+1):
            arr2.append(i+str(j))
    print(arr2)    
                

func('A1:F2')