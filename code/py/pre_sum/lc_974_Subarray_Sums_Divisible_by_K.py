# 974. Subarray Sums Divisible by K

# Medium

# 
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
# 
# 
# 
# Example 1:
# 
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# 
# 
# Note:
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#

# class Solution:
#     def subarraysDivByK(self, A: List[int], K: int) -> int:
#         res = 0
#         prefix = 0
#         count = [1] + [0] * (K-1)
#         for a in A:
#             prefix = (prefix + a) % K
#             res += count[prefix]
#             count[prefix] += 1
#         return res

class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)

        count = collections.Counter(P)
        return int(sum(v*(v-1)/2 for v in count.values()))
