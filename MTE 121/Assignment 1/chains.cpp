/*
Nathan Menezes

Compared output with Emily Di Lauro
 
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  double chain_length = -1;

  cout << "Enter a length in chains: ";
  cin >> chain_length;

  cout << "The length of " << chain_length << " chains is " << endl;

  const int CHAIN_TO_FEET = 66;
  const int CHAIN_TO_YARDS = 22;
  const int CHAIN_TO_LINKS = 100;
  const int CHAIN_TO_RODS = 4;
  const double CHAIN_TO_FURLONGS = 0.1;

  cout << chain_length * CHAIN_TO_FEET     << " feet "     << endl;
  cout << chain_length * CHAIN_TO_YARDS    << " yards "    << endl;
  cout << chain_length * CHAIN_TO_LINKS    << " links "    << endl;
  cout << chain_length * CHAIN_TO_RODS     << " rods "     << endl;
  cout << chain_length * CHAIN_TO_FURLONGS << " furlongs " << endl;
  
  return EXIT_SUCCESS;
}

/*
Enter a length in chains: 25
The length of 25 chains is 
1650 feet 
550 yards 
2500 links 
100 rods 
2.5 furlongs 

*/
