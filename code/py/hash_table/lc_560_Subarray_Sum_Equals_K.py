# 560. Subarray Sum Equals K

# Medium

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# 
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
# 
# Constraints:
# 
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107

# def subarraySum(self, nums, k):
#         count, cur, res = {0: 1}, 0, 0
#         for v in nums:
#             cur += v
#             res += count.get(cur - k, 0)
#             count[cur] = count.get(cur, 0) + 1
#         return res

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        res = 0
        cur = 0
        for num in nums:
            cur += num
            if cur-k in d:
                # Note that the cum sum is not monotone increasing. The values can be > 1. for example:[1,-1], [1,-1,0].
                res +=d[cur-k]
            if cur in d:
                d[cur] +=1
            else:
                d[cur] = 1
        return res



