# 300. Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing subsequence.
# 
# Example:
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:
# 
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP problem
        # DP[i] is the length of subsequence eading with nums[i]
        # Initialize Dp=1
        if not nums:
            return 0
        n=len(nums)
        dp_table=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp_table[i]=max(dp_table[i], dp_table[j]+1)
        return max(dp_table)

