/*
Nathan Menezes

Compared output with Emily Di Lauro
 
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double length = -1;
  cout << "Input the side length of a square-based pyramid: ";
  cin  >> length;

  double height = -1;
  cout << "Input the height of a square-based pyramid: ";
  cin  >> height;

  cout << "The volume of the square-based pyramid is "
       << height * pow(length, 2) / 3 << endl;

  return EXIT_SUCCESS;
}

/*
Case 1:
Input the side length of a square-based pyramid: 3.2
Input the height of a square-based pyramid: 4.5678
The volume of the square-based pyramid is 15.5914

Case 2:
Input the side length of a square-based pyramid: 8.9
Input the height of a square-based pyramid: 0.1
The volume of the square-based pyramid is 2.64033

Case 3:
Input the side length of a square-based pyramid: 100
Input the height of a square-based pyramid: 101
The volume of the square-based pyramid is 336667

*/
