# 739. Daily Temperatures

# Medium

# Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
#
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        t_max = T[n-1]
        for i in range(n-1,-1,-1):
            if t_max <= T[i]:
                t_max = T[i]
            else:
                days = 1
                while T[i]>=T[i+days]:
                    days += res[i+days]
                res[i]=days
        return res





