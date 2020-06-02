# 402. Remove K Digits
# Given a non-negative integer num represented as a string
# remove k digits from the number so that the new number is the smallest possible.
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

# Idea:
# Use stack 
# if the new element > the last one in stack, pop out 
# at most pop out k and until the stack is empty 
# Otherwise, push to the stack 
# Tricky part: get the last k from the stack if the length > k
# ignore the left 0s.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:  
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                k -= 1
                stack.pop()  
            stack.append(digit)
            print(stack)
        if k > 0:
            stack = stack[:-k]     
        return "".join(stack).lstrip("0") or "0" 


