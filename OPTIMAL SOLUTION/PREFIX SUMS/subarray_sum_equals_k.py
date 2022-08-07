# Prefix Sum

def subarray_sum_k(nums,k):
    ans = 0
    hash = {0:1}
    arr = []
    count = 0
    for i in range(len(nums)):
        count+=nums[i]
        arr.append(count)
    for i in arr:
        if i - k in hash:
            ans+=hash[i-k]
        if i not in hash:
            hash[i] = 1
        else:
            hash[i]+= 1
    return ans
print(subarray_sum_k([1,1,1],  2))