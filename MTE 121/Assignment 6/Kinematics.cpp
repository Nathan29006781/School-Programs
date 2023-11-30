/*
Authors: Nathan Menezes, Chaela Chan, Rachel Olsen (Done during Section 103)
Description: Outputs final distance from acceleration data of a car
Assumptions: Initial position and velocity are zero
Version: 1.0
*/
#include <iostream>
#include <fstream>

using namespace std;

void update(double & pos, double & vel, double & accel, double & time)
{
  pos += vel*time + accel*time*time/2;
  vel += accel*time;
}
	
double displacement(ifstream & FileIn, double time_interval)
{
  double pos = 0;
  double vel = 0;
  double accel = 0;
  while (FileIn >> accel)
    update (pos, vel, accel, time_interval);

  return pos;
}

int main()
{
	const double TIME_INTERVAL = 0.25;

	ifstream FileIn ("accel_data.txt");
	if(!FileIn)
	{
		cout << "Could not open accel_data.txt";
		return EXIT_FAILURE;
	}

	cout << "The displacement is "
        << displacement(FileIn, TIME_INTERVAL) << 'm' << endl;
	FileIn.close();
	
	return EXIT_SUCCESS;
}

/*
The displacement is 38.7649m
*/

