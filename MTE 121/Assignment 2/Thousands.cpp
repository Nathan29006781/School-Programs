/*
Nathan Menezes & Kabeer Cheema
Formats an integer in the thousands with commas

Assumptions: -999999 <= number <= 999999
 
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{

  int number = 0;
  cout << "Enter a number: ";
  cin >> number;

  int second_part = abs(number % 1000);
  number /= 1000;

  cout << "The number is " << number << ',';
  if (second_part < 100)
    cout << 0;
  if (second_part < 10)
    cout << 0;
  cout << second_part << endl;

  return EXIT_SUCCESS;
}

/*
Test Cases:

Enter a number: 425081
The number is 425,081

Enter a number: 1000
The number is 1,000

Enter a number: -11004
The number is -11,004

Enter a number: -987654
The number is -987,654

*/