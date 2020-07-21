# 120. Triangle

# Medium

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# 
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 2d-DP
        # dp[i][j] is the min path sum to triangle[i][j]
        n,m=len(triangle), len(triangle[-1])
        dp = [[0]*m for _ in range(n)]
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            dp[i][0] = triangle[i][0] + dp[i-1][0]
            dp[i][i] = triangle[i][i] + dp[i-1][i-1]
        for i in range(1,n):
            for j in range(1,i):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])

        return min(dp[n-1])

# O(1)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        if n==1:
            return triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                temp = min(triangle[i-1][max(j-1,0)],triangle[i-1][min(j,i-1)])
                triangle[i][j] = triangle[i][j] + temp
        return min(triangle[n-1])
