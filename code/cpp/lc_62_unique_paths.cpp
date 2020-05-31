/* 62. Unique paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
*/

/* Solution:
f(m,n) = f(m+1,n) + f(m, n+1)
*/
class Solution {  //num[i][j] means  poissible paths  kinds  from  (i+1cow   j+1col)  
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> num(m,vector<int>(n,1));
        for(int i=m-2;i>=0;i--){
            for(int j=n-2;j>=0;j--){
                 num[i][j]=num[i+1][j]+num[i][j+1];
            }
        }
        return num[0][0];
    }
};