# 18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1, n-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l<r and nums[l]==nums[l-1]:
                            l +=1
                        while l<r and nums[r]==nums[r+1]:
                            r -=1
                    elif total < target:
                        l +=1
                    else:
                        r -=1
        return res 


