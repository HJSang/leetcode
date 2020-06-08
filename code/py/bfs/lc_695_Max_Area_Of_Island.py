# 695. Max Area of Island
# Given a non-empty 2D array grid of 0's and 1's
# an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array
# If there is no island, the maximum area is 0.

# Example 1:
#[[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt = [0]
                    self.moveIsland(grid,i,j,n,m,cnt)
                    ans = max(ans, cnt[0])
        return ans
    def moveIsland(self,grid,i,j,n,m,cnt):
        if i<0 or i>=n or j<0 or j>=m or grid[i][j] == 0:
            return 
        cnt[0] +=1
        grid[i][j] = 0
        self.moveIsland(grid,i+1,j,n,m,cnt)
        self.moveIsland(grid,i-1,j,n,m,cnt)
        self.moveIsland(grid,i,j+1,n,m,cnt)
        self.moveIsland(grid,i,j-1,n,m,cnt)
        
        
