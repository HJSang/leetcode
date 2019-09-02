// Reverse String
/* Write a function that reverses a tring.
The input string is given as an array of characters char[].
Do not allocate extra space for another array.
Must do this by modifying the input array in-place with 
O(1) extra memory.
You may assume all the characters consist of printable ascii characters
*/

/* example 1:
Input: ['h','e','l','l','o']
Output: ['o','l','l','e','h']
*/

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int i=0, j=s.size()-1;
        while(i<j)
        {
            //swap
            int temp = s[j];
            s[j] = s[i];
            s[i] = temp;
            i++;
            j--;
        }
        
    }
};

