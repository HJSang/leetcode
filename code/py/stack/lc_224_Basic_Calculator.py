# 224. Basic Calculator

# Hard

# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
# 
# Example 1:
# 
# Input: "1 + 1"
# Output: 2
# Example 2:
# 
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
# 
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
#

# class Solution:
#     def calculate(self, s: str) -> int:

#         stack = []
#         operand = 0
#         res = 0 # For the on-going result
#         sign = 1 # 1 means positive, -1 means negative

#         for ch in s:
#             if ch.isdigit():

#                 # Forming operand, since it could be more than one digit
#                 operand = (operand * 10) + int(ch)

#             elif ch == '+':

#                 # Evaluate the expression to the left,
#                 # with result, sign, operand
#                 res += sign * operand

#                 # Save the recently encountered '+' sign
#                 sign = 1

#                 # Reset operand
#                 operand = 0

#             elif ch == '-':

#                 res += sign * operand
#                 sign = -1
#                 operand = 0

#             elif ch == '(':

#                 # Push the result and sign on to the stack, for later
#                 # We push the result first, then sign
#                 stack.append(res)
#                 stack.append(sign)

#                 # Reset operand and result, as if new evaluation begins for the new sub-expression
#                 sign = 1
#                 res = 0

#             elif ch == ')':

#                 # Evaluate the expression to the left
#                 # with result, sign and operand
#                 res += sign * operand

#                 # ')' marks end of expression within a set of parenthesis
#                 # Its result is multiplied with sign on top of stack
#                 # as stack.pop() is the sign before the parenthesis
#                 res *= stack.pop() # stack pop 1, sign

#                 # Then add to the next operand on the top.
#                 # as stack.pop() is the result calculated before this parenthesis
#                 # (operand on stack) + (sign on stack * (result from parenthesis))
#                 res += stack.pop() # stack pop 2, operand

#                 # Reset the operand
#                 operand = 0

#         return res + sign * operand
class Solution:
    def calculate(self, s: str) -> int:
        res, num, stack, sign = 0,0,[],1
        for c in s:
            print(c)
            if c.isdigit():
                num = 10*num +int(c)
            elif c=="+":
                res += sign*num
                num=0
                sign=1
            elif c=="-":
                res += sign*num
                num=0
                sign=-1
            elif c=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif c==")":
                prev_sign = stack.pop()
                prev_res = stack.pop()
                res+=sign*num
                res = prev_res + prev_sign*(res)
                num=0
        return res+sign*num

