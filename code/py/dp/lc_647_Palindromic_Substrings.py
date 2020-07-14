# 647. Palindromic Substrings

# Medium
# 
# Given a string, your task is to count how many palindromic substrings in this string.
# 
# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
# 
# Example 1:
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# Example 2:
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# Note:
# 
# The input string length won't exceed 1000.

class Solution:
    def countSubstrings(self, s: str) -> int:
        # center searching: (i), (i,i+1)
        ans, n = 0, len(s)
        for i in range(n):
            # i is the center
            j=k=i
            while j>=0 and k<n and s[j]==s[k]:
                ans +=1
                j -=1
                k +=1
            # i, i+1 are the center
            j=i
            k=i+1
            while j>=0 and k<n and s[j]==s[k]:
                ans +=1
                j -=1
                k +=1
        return ans
