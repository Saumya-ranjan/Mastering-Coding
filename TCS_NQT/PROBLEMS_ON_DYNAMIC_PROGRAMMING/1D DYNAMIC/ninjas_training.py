# Tabulation with Not space Optimization Technique:
# it uses o(n) space because of dp:

def ninjaTraining(points):
    dp = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
    dp[0][0], dp[0][1] , dp[0][2] = points[0][0] , points[0][1] , points[0][2]
    for i in range(1,len(dp)):
        dp[i][0] = max(dp[i-1][1]+ points[i][0], dp[i-1][2]+points[i][0])
        dp[i][1] = max(dp[i-1][0]+ points[i][1], dp[i-1][2]+points[i][1])
        dp[i][2] = max(dp[i-1][0]+ points[i][2], dp[i-1][1]+points[i][2])
    print(dp)

ninjaTraining([[1,2,5],[3,1,1],[3,3,3]])


#  Space Optimization  as we taking single space not an dp so it's o(1)

# def ninjaTraining(points):
#     prev0 = points[0][0]
#     prev1 = points[0][1]
#     prev2 = points[0][2]
#     for i in range(1,len(points)):
#         cur0 = max(points[i][0] + prev1 , points[i][0]  +prev2)
#         cur1 = max(points[i][1] + prev0 , points[i][1]  +prev2)
#         cur2 = max(points[i][2] + prev0 , points[i][2]  +prev1)
#         fullmax = max(cur0,cur1,cur2)
#         prev0 = cur0
#         prev1  = cur1
#         prev2 = cur2
#     return fullmax
# ninjaTraining([[1,2,5],[3,1,1],[3,3,3]])