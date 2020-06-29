# 763. Partition Labels

# A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
# 
#  
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#  
# 
# Note:
# 
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # Save the right most index for each char. 
        # The right most is for the segment point
        rightmost = {c:i for i,c in enumerate(S)}
        # two pointers: start and end
        l,r=0,0
        ans = []
        for i,c in enumerate(S):
            # right index
            r=max(rightmost[c],r)
            if i==r:
                # the index is the rightmost index
                ans +=[r-l+1]
                # move left index
                l=i+1
                
        return ans   
