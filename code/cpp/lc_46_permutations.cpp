/* 46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
*/

class Solution {
public:
	vector<vector<int>> permute(vector<int> & nums)
	{
		vector<vector<int>> res;
		DFS(res, nums,0);
		return res;
	}
	void DFS(vector<vector<int>>& res, vector<int>& nums, int pos)
	{
		if(pos==nums.size()-1)
		{
			res.push_back(nums);
			return;
		}
		for(int i = pos; i<nums.size(); i++)
		{
			swap(nums[pos], nums[i]);
			DFS(res,nums, pos+1);
			swap(nums[pos], nums[i]);
		}
	}
};