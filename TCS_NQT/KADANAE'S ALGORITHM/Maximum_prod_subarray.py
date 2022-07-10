def max_prod(arr):
    ma=arr[0]
    mn=arr[0]  
    ans=arr[0]
    for i in range(1,len(arr)):
        if arr[i]<0:
            ma,mn=mn,ma
        ma=max(arr[i],arr[i]*ma)
        mn=min(arr[i],arr[i]*mn)
        ans=max(ma,ans)
    return ans

max_prod([2,3,-2,4])