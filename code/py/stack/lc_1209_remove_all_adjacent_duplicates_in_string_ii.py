# 1209. Remove All Adjacent Duplicates in String II
# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters
# from s and removing then causing the left and the right side of the deleted substring to 
# concatenate together.
# we repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after such duplicate removals have been made.
# it is guranteed that the answer is unique.

# Idea:
# use stack to save # of char.
# if cnt == k: pop out 
# if cnt < k: cnt +1
# else: append char and cnt

class Solution:
  def removeDuplicates(self, s:str, k:int) -> str:
    stack = []
    for c in s:
      if stack:
        char, cnt = stack[-1]
        if char==c and cnt+1==k:
          stack.pop()
        elif char==c:
          stack[-1][1] +=1
        else:
          stack.append([c,1])
      else:
        stack.append([c,1])
    ans=''
    for i in stack:
      ans += i[0]*i[1]
    return ans
      
