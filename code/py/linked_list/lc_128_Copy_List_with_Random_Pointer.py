# 138. Copy List with Random Pointer

# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # create a dict: key is origin node and the value is copied node
        d = collections.defaultdict(lambda:Node(0))
        d[None] = None # for null node
        n=head
        while n:
            d[n].val = n.val
            d[n].next = d[n.next]
            d[n].random = d[n.random]
            n=n.next
        return d[head]
