# 4, [7,8,9,3], 2
#     | | | |
    
#    [8,9,3,5]
def func(N,arr,D):
    m=0
    mxPos=0
    
   
    for i in range(N):
        arr[i]=(arr[i]-1)//D
    for i in range(N):
        if arr[i]>=m:
            m=arr[i]
            mxPos=i
    print(mxPos+1)

func(4,[7,8,9,3],2)