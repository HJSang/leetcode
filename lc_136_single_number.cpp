/* 136 Single Number 
Given a non-empty array of integers, every element appears tiwce
except for one.
Find that single one.

Note: Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int r =0;
        for(int i=0; i<nums.size(); i++)
        {
            r ^= nums[i];
        }
        return r;
    }
};

/* Summary
XOR operation:
n^n = 0
0^n = n
It's commutative, so a^b^c = a^c^b = b^a^c = b^c^a = c^a^b = c^b^a.
*/
