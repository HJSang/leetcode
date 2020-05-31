// Letter Combinations of a Phone Number
/* Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number
could represent.
A mapping of digits to letters:
1:['a','b','c']
2:['d','e','f']
...
7:['p','q','r','s']
8:['t','u','v']
9:['w','x','y','z']
*/

/*Example:
Input:'23'
Output:["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
*/
 /*
 start with an empty builder,
  for every digit, 
  use all chars it represents to 
  attach to the builder, 
  when i reaches the end of digits, 
  push builder to result;
  */
class Solution {
public:
	vector<string> letterCombinations(string digits)
	{
		if(digits.empty())
		{
			return {};
		}
		vector<string> combs;
		const vector<string> chars = {"0","1","abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
		string builder;
		build(builder,0,digits,chars,combs);
		return combs;

		void build(string builder, int i, const string& digits, const vector<string>& chars, vector<string>& combs)
		{
			if(i==digits.size())
			{
				combs.push_back(builder);
				return;
			}
			int d = digits[i] - '0';
			for(char ch : chars[d])
			{
				build(builder+ch, i+1, digits, chars, combs);
			}
		}
	}
}
