# 1351. Count Negative Numbers in a Sorted Matrix
# Easy
# 
# 598
# 
# 39
# 
# Add to List
# 
# Share
# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
# 
# Return the number of negative numbers in grid.
# 
#  
# 
# Example 1:
# 
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:
# 
# Input: grid = [[3,2],[1,0]]
# Output: 0
# Example 3:
# 
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
# Example 4:
# 
# Input: grid = [[-1]]
# Output: 1
#  
# 
# Constraints:
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# -100 <= grid[i][j] <= 100

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # count from left bottom
        i=n-1
        j=0
        cnt=0
        while i>-1 and j<m:
            if grid[i][j]<0:
                cnt += (m-j)
                i -=1
            else:
                j +=1
        return cnt



