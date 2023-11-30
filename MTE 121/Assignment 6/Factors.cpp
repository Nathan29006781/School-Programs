/*
Authors: Nathan Menezes, Chaela Chan, Rachel Olsen (Done during Section 103)
Description: outputs the numeric factors of a positive user-inputed integer
Version: 1.0
*/

#include <iostream>

using namespace std;

int main()
{
	int num = 0;
	do
	{
		cout << "Enter a positive number: ";
		cin >> num;
	}
	while (num <= 0);

	int count = 0;
	for (int factor = num; factor > 0; factor--)
	{
		if (num % factor == 0)
		{
			cout << factor << ' ';
			count++;
			if (count % 5 == 0)
				cout << endl;
		}
	}
	return EXIT_SUCCESS;
}

/*
Enter a positive number: -5
Enter a positive number: 0
Enter a positive number: 999999
999999 333333 142857 111111 90909 
76923 47619 37037 30303 27027 
25641 15873 12987 10989 10101 
9009 8547 6993 5291 4329 
3861 3663 3367 3003 2849 
2457 2331 2079 1443 1287 
1221 1001 999 819 777 
693 481 429 407 351 
333 297 273 259 231 
189 143 117 111 99 
91 77 63 39 37 
33 27 21 13 11 
9 7 3 1
*/