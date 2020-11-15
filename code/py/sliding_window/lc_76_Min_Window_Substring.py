# 76. Minimum Window Substring

# Hard

# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
# 
# Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
# 
#  
# 
# Example 1:
# 
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# 
# Input: s = "a", t = "a"
# Output: "a"
#  
# 
# Constraints:
# 
# 1 <= s.length, t.length <= 105
# s and t consist of English letters.
#  
# 
# Follow up: Could you find an algorithm that runs in O(n) time?
# 
#

class Solution(object):
    def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    if not t or not s:
        return ""

    dict_t = Counter(t)

    required = len(dict_t)

    # Filter all the characters from s into a new list along with their index.
    # The filtering criteria is that the character should be present in t.
    filtered_s = []
    for i, char in enumerate(s):
        if char in dict_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    formed = 0
    window_counts = {}

    ans = float("inf"), None, None

    # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
    # Hence, we follow the sliding window approach on as small list.
    while r < len(filtered_s):
        character = filtered_s[r][1]
        window_counts[character] = window_counts.get(character, 0) + 1

        if window_counts[character] == dict_t[character]:
            formed += 1

        # If the current window has all the characters in desired frequencies i.e. t is present in the window
        while l <= r and formed == required:
            character = filtered_s[l][1]

            # Save the smallest window until now.
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            window_counts[character] -= 1
            if window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1

        r += 1
    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
#     def minWindow(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: str
#         """
#         t_counts = collections.Counter(t)
#         n = len(s)
#         l,r=0,0
#         d = {}
#         res=[[0,0,n+1]]
#         for r in range(n):
#             d[s[r]] = d.get(s[r],0)+1
#             while self.valid(t_counts,d):
#                 if res[-1][2]>r-l+1:
#                     res.pop()
#                     res.append([l,r,r-l+1])
#                 d[s[l]] -=1
#                 l+=1
#         a,b,c = res[0]
#         return s[a:(b+1)] if c<n+1 else ""
#     def valid(self,target,cur):
#         for i in target:
#             if target[i]>cur.get(i,0):
#                 return False
#         return True

