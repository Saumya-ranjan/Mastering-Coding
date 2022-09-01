#Bruteforce time complexity : o(n^3)

def func(arr,target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i!=j:
                c = target - (arr[i]+arr[j])
                if c in arr[j+1:]: 
                    count+=1
    print(count)
        

func([1, 4, 45, 6 ,10, 8],13)

