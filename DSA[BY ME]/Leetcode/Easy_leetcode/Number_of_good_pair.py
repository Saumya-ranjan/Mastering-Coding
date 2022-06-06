# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# def func(x):          #o(n^2)
#     count=0
#     for i in range(len(x)):
#         for j in range(i,len(x)):
#             if x[i] == x[j] and i<j:
#                 count+=1
#     print(count) 

def func(x):
    result = 0
    hash_map = {}

    for i in x:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1
        result = result+hash_map[i] - 1
    print(result)


func([1,1,1,1])