# 96. Unique Binary Search Trees
# Medium

# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
# 
# Example:
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    def numTrees(self, n: int) -> int:
        # define dp[n] is # of unique BST's (binary search trees)
        # define f(n,i) is # of BST using i as root
        # hence dp[n] = f(n,1) + ... + f(n,n)
        # f(n,i) = dp[i-1] *dp[n-i]
        # therefore, dp[n] = dp[0]*dp[n-1] + ... + dp[n-1]*dp[0]
        if n==0 or n==1:
            return 1
        dp = [0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
