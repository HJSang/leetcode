/* 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal 
to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for 
the purpose of space complexity analysis.)
*/
/* 1) create a acummulative product array
   2) get the reversal acummulative product from the end
   3) multipley
 */
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> C(nums.size(),1);
        if(nums.size() == 0)
            return C;
        
        for(int i = 1; i < nums.size(); i++){
            C[i] = C[i-1]*nums[i-1];
        }
        
        int temp = 1;
        for(int i = nums.size()-2; i >= 0; i--){
            temp = temp * nums[i+1];
            C[i] = C[i] * temp;
        }
        
        return C;
    }
};
