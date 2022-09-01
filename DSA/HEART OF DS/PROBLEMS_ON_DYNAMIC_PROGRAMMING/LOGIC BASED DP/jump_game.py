 # Greedy Algorithm

def canJump(nums):
    a = len(nums)-1
    for i in range(a-1,-1,-1):
        if i+nums[i] >= a:
            a = i
    if a == 0 :
        return True
    return False

print(canJump([2,3,1,1,4]))