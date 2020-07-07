# 322. Coin Change
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# Example 1:
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
# 
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1d- DP
        # dp[i] := the fewest number of coins to change i
        # start from bottom
        # Initialize as infinity
        dp = [0]+ [float('inf')]*amount
        for i in range(1,amount+1):
            for coin in coins:
                # stop whne i-coin<0
                if i-coin>=0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1]<float('inf') else -1
