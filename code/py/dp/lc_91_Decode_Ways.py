# 91. Decode Ways

# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# 
# Example 1:
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# JAVA 1-D DP Solution: https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation
# dp[0] means an empty string will have one way to decode, dp[1] means the way to decode a string of size 1. I then check one digit and two digit combination and save the results along the way. In the end, dp[n] will be the end result.

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0
        for i in range(1,n):
            num1 = int(s[i])
            num2 = int(s[i-1:i+1])
            if num1 !=0:
                dp[i+1] += dp[i]
            if num2>=10 and num2<=26:
                dp[i+1] += dp[i-1]

        return dp[-1]

