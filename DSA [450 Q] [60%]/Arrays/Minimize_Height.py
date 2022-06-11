def getMinDiff( arr, k):
        arr.sort()
        #[3  9  12 16 20]
        res = arr[-1]-arr[0]
        # 17
        for i in range(1,len(arr)):
            if arr[i]-k<0:
                continue
            minn = min(arr[0]+k,arr[i]-k)
            maxx = max(arr[-1]-k,arr[i-1]+k)
            res= min(res, maxx-minn)
        return res
print(getMinDiff([3, 9, 12, 16, 20],3))