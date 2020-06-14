# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Test case format:
# For simplicity sake, each node's value is the same as the node's
# index (1-indexed). For example, the first node with val = 1,
# the second node with val = 2, and so on. The graph is
# represented in the test case using an adjacency list.
# Adjacency list is a collection of unordered lists used to
# represent a finite graph. Each list describes the set of neighbors
# of a node in the graph.

# The given node will always be the first node with val = 1. You
# must return the copy of the given node as a reference to the
# cloned graph.

# Example 1:

# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        copynode = Node(node.val)
        copies = {copynode.val:copynode}
        self.dfs(node, copies)
        return copynode
    def dfs(self,node, copies):
        for nb in node.neighbors:
            if nb.val in copies:
                copies[node.val].neighbors.append(copies[nb.val])
            else:
                n = Node(nb.val)
                copies[n.val] = n
                copies[node.val].neighbors.append(n)
                self.dfs(nb,copies)


# Iterative way
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
                
        
        
