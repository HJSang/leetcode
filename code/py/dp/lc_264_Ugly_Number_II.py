# 264. Ugly Number II

# Medium

# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#

class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]

