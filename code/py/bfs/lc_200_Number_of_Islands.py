# 200. Number of Islands
# Given a 2d grid map of '1's (land) and '0's (water)
# count the number of islands
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
# You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    counter +=1
        return counter
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j]='#'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
