# 2357
def minimumOperations(nums):
        dp = [0 for _ in range(len(nums))]
        counter = 0
        def count(num):
            minn = 10000
            for i in range(len(num)):
                if num[i] > 0 and num[i] < minn:
                        minn = num[i]
            for i in range(len(num)):
                if num[i] >0:
                    num[i]-=minn
            return num
        while nums!= dp:
            nums = count(nums)
            counter+=1
        return counter
minimumOperations([1,5,0,3,5])

