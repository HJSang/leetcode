/* 78. Subsets.
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
*/

// A template to those combination problems
// https://leetcode.com/problems/combinations/discuss/27006/a-template-to-those-combination-problems

class Solution {
public:
	vector<vector<int>> subsets(vector<int> & nums)
	{
		vector<vector<int>> res;
		backtrack(nums,0,vector<int>(), res);
		return res;
	}
	void backtrack(vector<int>&nums, int k, vector<int> subset, vector<vector<int>>& res)
	{
		if(k==nums.size())
		{
			res.push_back(subset);
			return;
		}
		backtrack(nums, k+1, subset, res);
		subset.push_back(nums[k]);
		backtrack(nums,k+1,subset, res);
	}
};