# 694. Number of Distinct Islands

# Medium

# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# 
# Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
# 
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# 
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.
#

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        s = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    self.one=[]
                    self.dfs(grid,i,j)
                    self.one = sorted(self.one,key=lambda x: (x[0],x[1]))
                    res = []
                    for ind in self.one:
                        res.append(ind[0]-self.one[0][0])
                        res.append(ind[1]-self.one[0][1])
                    s.add(tuple(res))
        return len(list(s))

    def dfs(self,grid,i,j):
        n =len(grid)
        m=len(grid[0])
        if i<0 or i>n-1 or j<0 or j>m-1 or grid[i][j]==0:
            return
        grid[i][j]=0
        self.one.append([i,j])
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)

