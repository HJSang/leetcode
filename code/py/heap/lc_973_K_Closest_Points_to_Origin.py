# 973. K Closest Points to Origin

# Medium

# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# 
# (Here, the distance between two points on a plane is the Euclidean distance.)
# 
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
# 
#  
# 
# Example 1:
# 
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:
# 
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
#  
# 
# Note:
# 
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
# 
#


class Solution:
    def kClosest(self, points, K):
        return heapq.nsmallest(K, points, lambda x: x[0]**2 + x[1]**2)


########################################################################
# Heaps are binary trees for which every parent node has a value less than or equal to any of its children. This implementation uses arrays for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero. For the sake of comparison, non-existing elements are considered to be infinite. The interesting property of a heap is that its smallest element is always the root, heap[0].
# 
# The API below differs from textbook heap algorithms in two aspects: (a) We use zero-based indexing. This makes the relationship between the index for a node and the indexes for its children slightly less obvious, but is more suitable since Python uses zero-based indexing. (b) Our pop method returns the smallest item, not the largest (called a “min heap” in textbooks; a “max heap” is more common in texts because of its suitability for in-place sorting).
# 
# These two make it possible to view the heap as a regular Python list without surprises: heap[0] is the smallest item, and heap.sort() maintains the heap invariant!
# 
# To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().
# 
# The following functions are provided:
# 
# heapq.heappush(heap, item)
# Push the value item onto the heap, maintaining the heap invariant.
# 
# heapq.heappop(heap)
# Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
# 
# heapq.heappushpop(heap, item)
# Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().
# 
# New in version 2.6.
# 
# heapq.heapify(x)
# Transform list x into a heap, in-place, in linear time.
# 
# heapq.heapreplace(heap, item)
# Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.
# 
# This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.
# 
# The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.
# 
# The module also offers three general purpose functions based on heaps.
# 
# heapq.merge(*iterables)
# Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values.
# 
# Similar to sorted(itertools.chain(*iterables)) but returns an iterable, does not pull the data into memory all at once, and assumes that each of the input streams is already sorted (smallest to largest).
# 
# New in version 2.6.
# 
# heapq.nlargest(n, iterable[, key])
# Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]
# 
# New in version 2.4.
# 
# Changed in version 2.5: Added the optional key argument.
# 
# heapq.nsmallest(n, iterable[, key])
# Return a list with the n smallest elements from the dataset defined by iterable. key, if provided, specifies a function of one argument that is used to extract a comparison key from each element in the iterable: key=str.lower Equivalent to: sorted(iterable, key=key)[:n]
# 
# New in version 2.4.
# 
# Changed in version 2.5: Added the optional key argument.
# 
# The latter two functions perform best for smaller values of n. For larger values, it is more efficient to use the sorted() function. Also, when n==1, it is more efficient to use the built-in min() and max() functions. If repeated usage of these functions is required, consider turning the iterable into an actual heap.
# 
#                               0
# 
#               1                                 2
# 
#       3               4                5               6
# 
#   7       8       9       10      11      12      13      14
# 
# 15 16   17 18   19 20   21 22   23 24   25 26   27 28   29 30
# 
#

