# 10. Regular Expression Matching

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

# JAVA DP Solution: https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

# The solution uses 2D DP: Boolean 2d array with dim: len(s)+1 x len(p)+1
# initialize [0,0] as True

# 1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
# 2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
# 3, If p.charAt(j) == '*':
#    here are two sub conditions:
#                1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
#                2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
#                               dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a
#                            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
#                            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty


class Solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]y
