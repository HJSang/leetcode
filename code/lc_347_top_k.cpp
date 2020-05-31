/* 347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
*/

// Solution 1. MaxHeap, O(nlogn)
class Solution {
public:
	vector<int> topKFrequent(vector<int>& nums, int k)
	{
		unordered_map<int, int> m;
		for(auto x: nums) m[x]++;
		priority_queue<pair<int,int>> pq;
	    for(auto p:m) pq.push({p.second, p.first});
	    vector<int>res;
	    while(k--)
	    {
	    	res.push_back(pq.top().second);
	    	pq.pop();
	    }
	    return res;
	}
};

//Summary
/* unordered_map: https://www.geeksforgeeks.org/unordered_map-in-cpp-stl/
priority_queue:
1. https://www.geeksforgeeks.org/priority_queuetop-c-stl/
2. Priority queues are a type of container adaptors, 
specifically designed such that the first element of the queue 
is the greatest of all elements in the queue.
3. #include <queue> 
4. priority_queue<int> pqueue;
*/





