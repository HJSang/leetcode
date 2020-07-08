# 221. Maximal Square

# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
# 
# Example:
# 
# Input:
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4

# C++ 2d-DP Solution: https://leetcode.com/problems/maximal-square/discuss/61803/C%2B%2B-space-optimized-DP

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP[i][j] is the max side length to formualte the sqaure
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        ans=0
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j] !='1':
                    dp[i+1][j+1]=0
                else:
                    dp[i+1][j+1]=min(dp[i+1][j],dp[i][j+1],dp[i][j])+1
                ans = max(ans, dp[i+1][j+1])

        return ans*ans
