/*
Nathan Menezes & Kabeer Cheema
Outputs the polar form of a cartesian coordinate


References:
https://en.cppreference.com/w/cpp/numeric/math/atan2
*/

#include <iostream>
#include <cmath>

using namespace std;

int main()
{

  double x = 0.0;
  cout << "Enter the x-coordinate: ";
  cin >> x;

  double y = 0.0;
  cout << "Enter the y-coordinate: ";
  cin >> y;

  cout << "The radius is " << sqrt(x*x + y*y) << endl;
  cout << "The angle in radians is " << atan2(y, x) << " rad" << endl;
  cout << "The angle in degrees is " << atan2(y, x)*180/M_PI << "°" << endl;


  return EXIT_SUCCESS;
}

/*
Test Cases:

Enter the x-coordinate: -0.5
Enter the y-coordinate: -0.866
The radius is 0.999978
The angle in radians is -2.09441 rad
The angle in degrees is -120.001°

Enter the x-coordinate: 2.5
Enter the y-coordinate: 3.9
The radius is 4.63249
The angle in radians is 1.00076 rad
The angle in degrees is 57.3391°

Enter the x-coordinate: -4
Enter the y-coordinate: 2.9
The radius is 4.94065
The angle in radians is 2.51428 rad
The angle in degrees is 144.058°

Enter the x-coordinate: 0.6
Enter the y-coordinate: -4.8
The radius is 4.83735
The angle in radians is -1.44644 rad
The angle in degrees is -82.875°

Enter the x-coordinate: 0
Enter the y-coordinate: 0
The radius is 0
The angle in radians is 0 rad
The angle in degrees is 0°

*/