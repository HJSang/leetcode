# 986. Interval List Intersections

# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
# 
# Return the intersection of these two interval lists.
# 
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
# 
#  
# 
# Example 1:
# 
# 
# 
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#  
# 
# Note:
# 
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        i,j,res=0,0,[]
        while i<len(a) and j<len(b):
            if a[i][1] < b[j][0]:
                i +=1
            elif a[i][0] > b[j][1]:
                j +=1
            else:
                res.append([max(a[i][0],b[j][0]), min(a[i][1],b[j][1])])
                if a[i][1] < b[j][1]:
                    i +=1
                else:
                    j +=1
        return res  
