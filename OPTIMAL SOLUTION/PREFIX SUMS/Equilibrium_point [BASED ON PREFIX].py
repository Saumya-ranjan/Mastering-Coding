# Prefix Sum as well aas suffix sum:

# O(N)) --> T.C
# O(N) --> S.C
def equilibrium(arr):
    prefix = [0]
    suffix = [0]
    prefix_sum = 0
    suffix_sum = 0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        prefix.append(prefix_sum)
    for j in range(len(arr)-1,-1,-1):
        suffix_sum+=arr[j]
        suffix.append(suffix_sum)
    for i in range(len(arr)):
        if prefix[i] == suffix[len(suffix)-2-i]:
            print(i)
    print(prefix,suffix)

equilibrium([1,0])

# Brute Force Method:
# def equilibrium(arr):
#     for i in range(len(arr)):
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return arr[i]
#     return False


# print(equilibrium([8,10,-2,+2,8]))