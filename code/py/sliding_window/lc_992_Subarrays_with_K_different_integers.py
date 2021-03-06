# 992. Subarrays with K Different Integers

# Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.
# 
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# 
# Return the number of good subarrays of A.
# 
#  
# 
# Example 1:
# 
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# Example 2:
# 
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
#  
# 
# Note:
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length

# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # The number of subarrays with at most K distinct elements.
        # Just need one more step to reach the folloing equation:
        # exactly(K) = atMost(K) - atMost(K-1)
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            # find another unique and new value
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            # when having more than K distinct values
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1   
            res += j - i + 1
        return res
        
        
