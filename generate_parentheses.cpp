//Generate Parentheses
/* Given n pairs of parentheses, write a function
to generate all combinations of well-formed parentheses.
*/

/* For example, n=3
[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]
*/
/* When the number of '(' less than n, append '('
WHen the number of '(' is more than the number of ')'
append ')'
*/
#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<string> result;
    vector<string> generateParenthesis(int n) {
        helper("",n,0);
        return result;
    }
    void helper(string s, int leftpare_need, int moreleft)
    {
        if(leftpare_need==0 && moreleft==0)
        {
            result.push_back(s);
            return;
        }
        if(leftpare_need>0)
        {
            helper(s+"(",leftpare_need-1, moreleft+1);
        }
        if(moreleft)
        {
            helper(s+")",leftpare_need,moreleft-1);
        }
        
    }
};

int main()
{
	int n = 4;
	Solution s;
	vector<string> str= s.generateParenthesis(n);
	for(int i=0; i< str.size(); i++)
	{
		cout<<str[i]<<endl;
	}
}

