# 456. 132 Pattern 
# Given a sequence of n intergers a_1, a_2, ..., a_n,
# A 132 pattern is a subsequence a_i, a_j, a_k such that:
# i<j<k and a_i < a_k < a_j.
# Design an algorithm that takes a lits of n numbers as input and 
# checks whether there is a 132 pattern in the list.

# Idea: The number which larger than the **third** and before **third** is stored in the stack.
# loop nums from end to begin 
class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    stack, s3 = [], -float('Inf')
    for n in nums[::-1]:
      if n<s3:
        # return True because n < s3 < stack[-1] (132 pattern)
        return True
      while stack and stack[-1] < n:
        # if stack is not empty, pop the last element if <n
        s3=stack.pop()
      # while loop stops when stack is empty or stack[-1]>=n  
      stack.append(n)
    return False    
