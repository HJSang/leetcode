# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle


class Solution:
    def maxSubarray(self, nums):
        maxSum = 0
        res = -float('inf')
        for num in nums:
            maxSum = max(0,maxSum) + num
            res = max(res, maxSum)
        return res

# DP idea:
# https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
# If we think the sub problem as `maxSubArray(int A[], int i, int j)`, which means the maxSubArray for A[i: j]
# In this way, our goal is to figure out what `maxSubArray(A, 0, A.length - 1)` is
# However if we define the format of the sub problem in this way, it's hard to find the connection from the sub problem to the original problem
#
# change the format of the sub problem into something like: `maxSubArray(int A[], int i)`
# which means the maxSubArray for A[0:i ] which must has A[i] as the end element.
# we have to keep track of each solution of the sub problem to update the global optimal value
# However, now the connect between the sub problem & the original one becomes clearer:
# `maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]; `

class Solution:
    def maxSubarray(self, nums):
        maxSum = 0
        n = len(nums)
        res = nums[0]
        dp = [0 for _ in range(n)]
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
            maxSum = max(maxSum, dp[i])
        return maxSum




