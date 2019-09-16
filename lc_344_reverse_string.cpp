/* 344. Reverse string
Write a function that reverses a string. 
The input string is given as an array of characters char[].

Do not allocate extra space for another array, 
you must do this by modifying the input array in-place 
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

*/

class Solution {
public: 
	void reverseString(vector<char> &s)
	{
		vector<char>* p = &s;
		int len = p->size();
		int aux;
		for(int i=0; i<len/2; i++)
		{
			aux = s[i];
			s[i] = s[len-1-i];
			s[len-1-i]=aux;
		}
	}
};
