# 659. Split Array into Consecutive Subsequences

# Medium
# Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences such that each subsequence consists of consecutive integers and has length at least 3.
# 
# 
# 
# Example 1:
# 
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# 
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# 
# Input: [1,2,3,4,4,5]
# Output: False
# 
# 
# Constraints:
# 
# 1 <= nums.length <= 10000

# Explanation
# I used a greedy algorithm.
# leftis a hashmap, left[i] counts the number of i that I haven't placed yet.
# endis a hashmap, end[i] counts the number of consecutive subsequences that ends at number i
# Then I tried to split the nums one by one.
# If I could neither add a number to the end of a existing consecutive subsequence nor find two following number in the left, I returned False
# 
# 
# Complexity
# Time O(N)
# Space O(N)

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True
