# 856. Score of Parentheses
# Given a balanced parentheses string S
# compute the score of the string based on the following rule:
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.

# Idea:
# if '(': push the cur number to the stack 
# if ')': cur number add stack pop + max(cur, 1)

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur
