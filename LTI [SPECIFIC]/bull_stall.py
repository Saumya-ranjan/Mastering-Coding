def isPossible(stalls, k, mid):
    count = 1
    temp = stalls[0]
    dist = 0
    for i in stalls:
        dist = i-temp
        if dist>=mid :
            count += 1
            temp = i
            if( count==k ):
                return True
    return False
           
def aggressiveCows(stalls, k):
    stalls = sorted(stalls)
    ans = -1
    i = 0
    j = stalls[-1]
    mid = i + (j-i)//2
    while( i<=j ):
        if isPossible(stalls, k, mid):
            i = mid+1
            ans = mid
        else:
            j = mid-1
        mid = i + (j-i)//2
        
    return ans
print(aggressiveCows([4,2,1,2,3,6],2))