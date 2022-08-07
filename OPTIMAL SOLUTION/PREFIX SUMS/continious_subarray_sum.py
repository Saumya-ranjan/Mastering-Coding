# To solve in o(n) -->

def checkSubarraySum(nums,k):
    #o(n)
    arr = []
    hash = {0:-1}
    count = 0
    for i in range(len(nums)):
        count+=nums[i]
        arr.append(count)
    counter = 0
    for i in range(len(arr)):
        if arr[i]%k not in hash:
            hash[arr[i]%k] = counter
            counter+=1
        elif arr[i]%k in hash:
            if abs(hash[arr[i]%k] - counter) >= 2:
                counter+=1
                return True
            else:
                counter+=1
    return False
checkSubarraySum([23,2,4,6,7], 6)