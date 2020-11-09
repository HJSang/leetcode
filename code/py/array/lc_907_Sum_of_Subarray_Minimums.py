# 907. Sum of Subarray Minimums

# Medium

# Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
# 
# 
# Note:
# 
# 1 <= A.length <= 30000
# 1 <= A[i] <= 30000

# https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C%2B%2BJavaPython-Stack-Solution


# Intuition:
# I guess this is a general intuition for most solution.
# res = sum(A[i] * f(i))
# where f(i) is the number of subarrays,
# in which A[i] is the minimum.
# 
# To get f(i), we need to find out:
# left[i], the length of strict bigger numbers on the left of A[i],
# right[i], the length of bigger numbers on the right of A[i].
# 
# Then,
# left[i] + 1 equals to
# the number of subarray ending with A[i],
# and A[i] is single minimum.
# 
# right[i] + 1 equals to
# the number of subarray starting with A[i],
# and A[i] is the first minimum.
# 
# Finally f(i) = (left[i] + 1) * (right[i] + 1)
# 
# For [3,1,2,4] as example:
# left + 1 = [1,2,1,1]
# right + 1 = [1,3,2,1]
# f = [1,6,2,1]
# res = 3 * 1 + 1 * 6 + 2 * 2 + 4 * 1 = 17
# 
# 
# Explanation:
# To calculate left[i] and right[i],
# we use two increasing stacks.
# 
# It will be easy if you can refer to this problem and my post:
# 901. Online Stock Span
# I copy some of my codes from this solution.
# 
# 
# Complexity:
# All elements will be pushed twice and popped at most twice
# O(N) time, O(N) space
#

class Solution:
    def sumSubarrayMins(self, A):
        n, mod = len(A), 10**9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod



