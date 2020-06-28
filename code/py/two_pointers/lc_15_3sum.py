# 15. 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Sort and two-pointer search 
# Note: please skip the repeated the nums
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if nums[i]>0 or nums[i]+nums[i+1]+nums[i+2]>0:
                break
            # if nums[i] + nums[n-2] + nums[n-1]<0:
            #     continue
            if (i>0 and nums[i-1]==nums[i]) or (nums[i] + nums[n-2] + nums[n-1]<0):
                continue
            l,r = i+1, n-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s ==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l +=1
                    while l<r and nums[r]==nums[r-1]:
                        r -=1
                    l +=1
                    r -=1
                elif s <0:
                    l +=1
                else:
                    r -= 1
        return ans
