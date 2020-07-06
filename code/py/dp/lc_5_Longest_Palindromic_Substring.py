# 5. Longest Palindromic Substring
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# 
# Example 1:
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
# 
# Input: "cbbd"
# Output: "bb"


# Non-DP Solution:
# for each index, you can either search it to two direction `xax` or `xaax`.
# Find the longest one

class Solution:
    def longestPalindrome(self,s:str) -> str:
        res = ''
        for i in range(len(s)):
            temp1=self.helper(s,i,i)
            temp2=self.helper(s,i,i+1)
            res=temp1 if len(temp1)>len(temp2) else temp2
        return res
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            u+=1
        return s[l+1:u]

# DP-solution:
# create a 2-d boolean array to indicate if [i,j] is palindromic or not
# state function:
#  if d[i,i]=True; then d[i,i+1]=True if str[i]==str[i+1]
#  d[i, i+2]=True if str[i]==str[i+2] and str[i+1:i+2] is palindromic
#  d[i,i+3]=True if str[i]==str[i+3] and str[i+1:i+3] is palindromic
# Hence, d[i,i+s] = True if str[i]==str[i+s] and str[i+1:i+s] is palindromic

class Solution:
    def longestPalindrome(self,s):
        if not s:
            return ''
        n = len(s)
        dpTable = [[False for _ in range(n)] for _ in range(n)]
        maxLen, amxString = 1, s[0]
        # Initialize
        for i in range(n):
            dpTable[i][i]=True
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                dpTable[i][j] = (s[i]==s[j])
                if j!=i+1:
                    dpTable[i][j] &= dpTable[i+1][j-1]
                if dpTable[i][j] and j-i+1>maxLen:
                    maxLen = j-i+1
                    maxString = s[i:j+1]
        return maxString


