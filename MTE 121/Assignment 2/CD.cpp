/*
Nathan Menezes & Kabeer Cheema
Outputs what coffee and sweet Mike buys with the amount he has
 
*/

#include <iostream>

using namespace std;

int main()
{

  const double LARGE_COFFEE = 1.75;
  const double SMALL_COFFEE = 1.00;
  const double DONUT = 1.00;
  const double CHOCOLATE = 0.60;
  const double MINI_TART = 0.50;

  double amount = -1.0;
  cout << "Enter an amount: $";
  cin >> amount;
  
  if (amount >= LARGE_COFFEE)
  {
    cout << "You bought a large coffee!" << endl;
    amount -= LARGE_COFFEE;
  }
  else if (amount >= SMALL_COFFEE)
  {
    cout << "You bought a small coffee!" << endl;
    amount -= SMALL_COFFEE;
  }
  else
    cout << "You bought no coffee." << endl;


  if (amount >= DONUT)
    cout << "You bought a donut!" << endl;
  else if (amount >= CHOCOLATE)
    cout << "You bought chocolate!" << endl;
  else if (amount >= MINI_TART)
    cout << "You bought a mini tart!" << endl;
  else
    cout << "You bought no sweet." << endl;

  return EXIT_SUCCESS;
}

/*
Test Cases:

Enter an amount: $0
You bought no coffee.
You bought no sweet.

Enter an amount: $0.6
You bought no coffee.
You bought chocolate!

Enter an amount: $1   
You bought a small coffee!
You bought no sweet.

Enter an amount: $3
You bought a large coffee!
You bought a donut!

*/