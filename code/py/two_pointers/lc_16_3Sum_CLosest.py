# 16. 3Sum Closest

# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
#  
# 
# Example 1:
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
# Constraints:
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Three pointers and array sorting
        # Sort the array.
        # Initialize ans = nums[0]+nums[1]+nums[2]
        # Loop the array: i=0 to n-1.
        #   L=i+1,R=n-1
        #   ans_candidate = nums[i]+nums[L]+nums[R]
        #   if ans_candidate==target: return ans_candidate
        #   elif: abs(ans_candidate-target)<abs(ans-target): ans= ans_candidate
        #   if ans_candidate > target: R = R-1
        #   else: L = L + 1
        nums.sort()
        n=len(nums)
        ans = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            L=i+1
            R=n-1
            while L<R:
                ans_candidate = nums[i]+nums[L]+nums[R]
                if ans_candidate==target: 
                    return ans_candidate
                if abs(ans_candidate-target)<abs(ans-target):
                    ans= ans_candidate
                if ans_candidate > target: R = R-1
                else:
                     L = L+1
        return ans
