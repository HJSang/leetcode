# 456. 132 Pattern 
# Given a sequence of n intergers a_1, a_2, ..., a_n,
# A 132 pattern is a subsequence a_i, a_j, a_k such that:
# i<j<k and a_i < a_k < a_j.
# Design an algorithm that takes a lits of n numbers as input and 
# checks whether there is a 132 pattern in the list.

# Idea: The number which larger than the **third** and before **third** is stored in the stack.

```python
class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    stack, s3 = [], -float('Inf')
    for n in nums[::-1]:
      if n<s3:
        return True
      while stack and stack[-1] < n:
        s3=stack.pop()
      stack.append(n)
    return False    
```
