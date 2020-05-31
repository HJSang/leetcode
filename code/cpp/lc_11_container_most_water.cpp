/* 11. Container With Most Water

Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of 
line i is at (i, ai) and (i, 0). Find two lines, which 
together with x-axis forms a container, such that the 
container contains the most water.

Note: You may not slant the container and n is at least 2.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
*/

/* Solution:
1) To maximize (j-i)*min(a_i, a_j)
2) i=0, j=n-1
3) if a_i< a_j, i++
   if a_i>a_j, j--
 */

class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size(),i=0,j;
        j = n-1;
        int max_area =0, area;
        while(i<j)
        {
            area = (j-i)*min(height[i],height[j]);
            if(area>max_area) max_area=area;
            if(height[i]>height[j])
            {
                j--;
            }
            else
            {
                i++;
            }
        }
        return max_area;
    }
};