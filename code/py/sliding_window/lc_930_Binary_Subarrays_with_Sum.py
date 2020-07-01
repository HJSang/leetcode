# 930. Binary Subarrays With Sum
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
#  
# 
# Example 1:
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#  
# 
# Note:
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        return self.atMost(A,S) - self.atMost(A,S-1)
    def atMost(self, A, S):
        if S<0:
            return 0
        i,res,n=0,0,len(A)
        for j in range(n):
            S -= A[j]
            while S<0:
                S += A[i]
                i +=1
            res += j-i+1
        return res 

