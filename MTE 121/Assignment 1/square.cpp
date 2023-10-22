/*
Nathan Menezes

Compared output with Emily Di Lauro
 
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double side_length = -1;

  cout << "Input a side length: ";
  cin >> side_length;

  cout << "The square of " << side_length
       << " is " << pow(side_length, 2) << endl;

  cout << "& the cube of " << side_length
       << " is " << pow(side_length, 3) << endl;
  
  return EXIT_SUCCESS;
}

/*
Input a side length: 8
The square of 8 is 64
& the cube of 8 is 512

*/
