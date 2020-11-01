# 718. Maximum Length of Repeated Subarray

# Medium
# 
# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
# 
# Example 1:
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
#  
# 
# Note:
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        DP = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, n+1):
            for j in range(1,m+1):
                if A[i-1] == B[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                    ans = max(ans, DP[i][j])
        return ans
