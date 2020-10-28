# 53. Maximum Subarray

# Easy

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# 
#

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1-d DP solution
        # dp[i] is the maxmimum sum endding with i-th entry
        # res = max(dp)
        # dp[i] = max(0,dp[i-1]) + nums[i]
        maxsum = 0
        res = -float('inf')
        for num in nums:
            maxsum = max(0,maxsum) + num
            res = max(res,maxsum)
        return res



class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # divide and conquer solution
        # maxsum = max(maxsum of left half, maxsum of right hald, middle)
        # middle = middle + maxsum of left seen + maxsum of right seen
        if len(nums)==1:
            return nums[0]
        l,r=0, len(nums)-1
        m = l + (r-l)//2
        lmax = self.maxSubArray(nums[:m+1])
        rmax = self.maxSubArray(nums[m+1:])
        lseen = 0
        s=0
        for i in range(m-1,-1,-1):
            s+=nums[i]
            lseen = max(lseen,s)
        rseen = 0
        s=0
        for i in range(m+1,len(nums)):
            s += nums[i]
            rseen=max(rseen,s)


        return max(lmax,rmax, nums[m]+lseen+rseen)
