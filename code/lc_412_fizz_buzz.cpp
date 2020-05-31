/* 412 Fizz Buzz
Write a program that outputs the string 
representation of numbers from 1 to n.

But for multiples of three it should output "Fizz"
Instead of the number and for the multiplies of five
output "Buzz". For umbers which are multiples of both
three and five output FizzBuzz.
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
*/

class Solution{
public:
	vector<string> fizzBuzz(int n)
	{
		std::vector<std::string> r;
		//reserve memory for vector
		r.reserve(n);
		for(int i=1; i<=n; i++)
		{
			int mod = i%15;
			switch(mod)
			{
				// factor of 15 only
				case 0: {
					r.push_back("FizzBuzz");
					break;
				}
				// factor of 3 only
				case 3:
				case 6:
				case 9:
				case 12:
				{
					r.push_back("Fizz");
				}
				//factor of 5 only
				case 5:
				case 10:
				{
					r.push_back("Buzz");
				}
				//default
				default:
				{
					r.push_back(std::to_string(i));
					break;
				}

			}
		}
		return r;
	}
};
