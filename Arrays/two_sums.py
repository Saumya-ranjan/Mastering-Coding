# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def sums(x):
    target = int(input("enter a target: "))
    for i in range(len(x)):
        for j in range(len(x)):
            if (x[i] + x[j]) == target:
                print( i, j)
    


sums([2,0,11,11,9,15])