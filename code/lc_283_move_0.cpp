/* 283 Move Zeros
Given an array nums, write a function to 
move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
*/

/* i =0, j=0
nums[0]=0
j++ ---> j=1
nums[1] = 1 !=0
then, swap(nums[0], nums[1]).
That is [1,0,0,3,12]
i++ --> i = 1
j++ --> j = 2
nums[2] = 0
j++ --> j = 3
nums[3] =3 !=0
swap(nums[1], nums[3])
That is [1,3,0,0,12]
i++ --> i = 2
j++ -> j = 4
*/

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for(int i = 0, j = 0; j < nums.size(); j++) if(nums[j] != 0) swap(nums[i++], nums[j]);
    }
};
