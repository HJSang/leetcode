# 1197. Minimum Knight Moves
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
# A knight has 8 possible moves it can make, as illustrated below.
# . Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# https://leetcode.com/problems/minimum-knight-moves/
# Return the minimum number of steps needed to move the knight to the square [x, y].
# It is guaranteed the answer exists.



# Example 1:
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]

# Example 2:
# 
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

# Constraints:
# |x| + |y| <= 300


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def dfs(x,y):
            if (x,y) not in memo:
                x,y = abs(x),abs(y)
                if x == y == 0:
                    return 0
                if x + y == 2:
                    return 2
                ans = min(dfs(x-1,y-2),dfs(x-2,y-1))+1
                memo[(x,y)] = ans
            return memo[(x,y)]
        memo = {}
        return dfs(x,y)
