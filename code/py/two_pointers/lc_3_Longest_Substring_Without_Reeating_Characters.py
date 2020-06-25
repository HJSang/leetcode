# 3. Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.
# 
# Example 1:
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Two pointers: one is the start and another is the end
# if not repeated, end ++
# if repeated, start ++
# save the visted chars to check repeated or not: key is the value and the value is the index
# start <= seen index makes sure that the repeated happens. 

class Solution:
  def lengthOfLongestSubstring(self, s:str) -> int:
    ans = 0
    visited = {}
    start, end = 0,0
    for i, c in enumerate(s):
      # if repeated
      if c in visited and start <= visited[c]:
        start = visited[c]+1
      else:
        ans = max(ans, i-start+1)
      seen[c] = i
    return ans
