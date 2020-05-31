# 946. Validate Stack Sequences
# Given two sequences pushed and popped with distinct values
# return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

# Idea:
# Create a stack and append pushed elements.
# for each step, check if the last element = popped[i]
# if so, do while loop to pop out all equal elements 

class Solution:
  def validStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    i, stack = 0, []
    for p in pushed:
      stack.append(p)
      while stack and popped[i]==stack[-]:
        stack.pop()
        i +=1
    return len(stack)==0
