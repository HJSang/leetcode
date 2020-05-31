# LeetCode Daily Track

## Stack
To understand *Stack* data structure, please read [Stack Data Structure](https://www.geeksforgeeks.org/stack-data-structure/) in geeksforgeeks. In short, First-in-Last-out: ![image.png](../files/stack.png). In python, the implementation of stack can be: 
* list
* collections.deque

```python
stack = []
stack.append('a')
stack.append('b')
print('stack is:', stack)
stack.pop()
print('stack is: ', stack)
```
```
stack is: ['a', 'b']
stack is:  ['a']
```
```python
from collections import deque 
stack = deque() 
stack.append('a') 
stack.append('b')
stack.pop()
```
For stack in CPP, please read [Stack in C++ STL](https://www.geeksforgeeks.org/stack-in-cpp-stl/).

For stack problems, the keys are to find:
* when and what are appended into the stack 
* when to pop the stack and how to deal with the poped elements 
* what happens if the stack is empty 

