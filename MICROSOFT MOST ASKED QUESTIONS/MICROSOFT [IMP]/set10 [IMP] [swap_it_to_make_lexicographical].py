def minimizeWithKSwaps(arr, n, k):
    a = ""
    for i in range(n-1):
        pos = i
        for j in range(i+1, n):
            if (j-i > k):
                break
            if (arr[j] < arr[pos]):
                pos = j
        for j in range(pos, i, -1):
            arr[j],arr[j-1] = arr[j-1], arr[j]
        k -= pos - i
    for i in range(len(arr)):
        a+=str(arr[i]) + " "
    print(a)
        

# Driver Code
for i in range(int(input())):
    a,b = input().split()
    n,k = int(a) , int(b)
    arr = [int(j) for j in input().split()]
    minimizeWithKSwaps(arr, n, k)
