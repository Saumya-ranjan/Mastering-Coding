# o(n) -- >
# Dynamic Programming 1d -- >

def numberOfArithmeticSlices(nums):
    dp  =[0 for _ in range(len(nums))]
    for i in range(2 , len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            dp[i] = dp[i-1] + 1
    return sum(dp)
        


# o(n^2) -- >s
def particle(arr):
    count = 0
    arr1 = []
    for i in range(len(arr)+1):
        for j in range(i+1 , len(arr)+1):
            if len(arr[i:j]) >=3:
                arr1.append(arr[i:j])
    for i in range(len(arr1)):
        diff = arr1[i][1] - arr1[i][0]
        for j in range(len(arr1[i])-1):
            if arr1[i][j+1] - arr1[i][j] != diff:
                count+=1
                break

    print(len(arr1) - count)

particle([7, 7, 7, 7])
