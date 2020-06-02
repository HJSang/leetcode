# 901. Online Stock Span 
# Write a class StockSpanner which collects daily price quotes for some stock, 
# and returns the span of that stock's price for the current day.
# The span of the stock's price today is defined as the maximum number of consecutive days 
# (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
# For example, if the price of a stock over the next 7 days were
#  [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

# Idea:
# Use stack to save the element and the span 
# so that we don't need to go back and only go back through stack 

class StockSpanner:
    def __init__(self):
        # initial stack 
        self.stack = []

    def next(self, price):
        # count the current element itself
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        # the while loop stops when the stack is empty or the last element in stack>price    
        self.stack.append([price, res])
        return res    
