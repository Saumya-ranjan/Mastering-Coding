# Recursive  -> TLE(TIME LIMIT EXECUTION)
# def palindromic_substring(a):
#     arr = []
#     arr1 =[]
#     for i in range(len(a)+1):
#         for j in range(i+1,len(a)+1):
#             arr.append(a[i:j])
#     for i in arr:
#         if i ==i [::-1]:
#             arr1.append(i)
#     arr1.sort(key = len)
#     print(len(arr1[-1]))

# palindromic_substring("babad")

# Tabulation  --> EFFICIENT ( more efficient than memoization )

def palindromic_substring(a):
    arr1= [ ]
    b = a[::-1]
    dp = [ [0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    for i in range(1,len(dp)):
        for j in range(1,len(a)+1):
            if b[i-1] == a[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = 0
    for i in range(len(dp)):
        for j in dp[i]:
            arr1.append(j)
    print(max(arr1))

palindromic_substring("babad")