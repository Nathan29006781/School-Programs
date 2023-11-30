/*
Author: Nathan Menezes
Description: A proper fraction class with data validation
Version: 3.0

Assumptions:
- Fraction does not need to be in lowest terms as per assignment
- User will not attempt illegal code such as giving a negative
  value to an unsigned int
*/

#include <iostream>
#include <numeric>

using namespace std;

class Fraction
{
  friend ostream & operator<<(ostream & out,
                              const Fraction & fraction);
  private:
    int numerator = 0;
    unsigned int denominator = 1;

    static bool validate(int numerator, int denominator)
    {
      return abs(numerator) < denominator;
    }

  public:
    Fraction()
    {
      cout << "Created " << *this << endl;
    }

    Fraction(int numerator, unsigned int denominator)
    {
      if(validate(numerator, denominator))
      {
        this->numerator = numerator;
        this->denominator = denominator;
      }
      else
      {
        cout << "Could not create ";
        output(numerator, denominator);
        cout << " Resetting. ";
      }
      cout << "Created " << *this << endl;
    }

    void set(const Fraction & other)
    {
      cout << "Changed " << *this;
      numerator = other.numerator;
      denominator = other.denominator;
      cout << " to " << *this << endl;
    }

    void set(int numerator, int denominator)
    {
      if(validate(numerator, denominator))
      {
        cout << "Changed " << *this;
        this->numerator = numerator;
        this->denominator = denominator;
        cout << " to " << *this << endl;
      }
      else
      {
        cout << "Could not change " << *this << " to ";
        output(numerator, denominator);
        cout << endl;
      }
    }

    bool change_numerator(int numerator)
    {
      if(validate(numerator, denominator))
      {
        cout << "Changed numerator from " 
             << this->numerator
             << " to " << numerator << endl;
        this->numerator = numerator;
        return true;
      }
      cout << "Could not change numerator from " 
           << this->numerator
           << " to " << numerator << endl;
      return false;
    }

    bool change_denominator(unsigned int denominator)
    {
      if(validate(numerator, denominator))
      {
        cout << "Changed denominator from " 
             << this->denominator
             << " to " << denominator << endl;
        this->denominator = denominator;
        return true;
      }
      cout << "Could not change denominator from " 
           << this->denominator
           << " to " << denominator << endl;
      return false;
    }

    void reduce()
    {
      unsigned int divisor = gcd(numerator, denominator);
      if(divisor != 1)
      {
        cout << "Reduced " << *this;
        numerator /= divisor;
        denominator /= divisor;
        cout << " to " << *this << endl;
      }
      else cout << "Could not reduce " << *this << endl;
    }

    int get_numerator() const
    {
      return numerator;
    }

    unsigned int get_denominator() const
    {
      return denominator;
    }

    double round(int decimal_places) const
    {
      return std::round(pow(10, decimal_places) * (*this))
              /   pow(10, decimal_places);
    }

    bool isExactlySame(Fraction const & other) const
    {
      return numerator == other.numerator
          && denominator == other.denominator;
    }

    ostream & output(ostream & out = cout) const
    {
      return out << *this;
    }

    static ostream & output(int numerator, unsigned int denominator,
                            ostream & out = cout)
    {
      return out << numerator << '/' << denominator;
    }

    operator double() const
    {
      return (double)numerator/denominator;
    }

    /*
      Comparison and arithmetic operators get defined from the
      double conversion. They return double, not a Fraction object
    */
};

ostream & operator<<(ostream & out, const Fraction & fraction)
{
  return Fraction::output(fraction.numerator,
                          fraction.denominator, out);
}

int main()
{
  Fraction f1; cout << f1 << " = " << f1.round(2) << endl << endl;
  Fraction f2(3, 7); cout << f2 << " = " << f2.round(3) << endl;
  
  cout << endl;

  f1.set(6, 14); cout << f1 << " = " << f1.round(5) << endl;
  cout << f1 << (f1 == f2 ? " == " : " != ") << f2 << endl; 
  cout << f1 << " does " << (f1.isExactlySame(f2) ? "" : "not ")
       << "exactly equal " << f2 << endl << endl;

  f2.reduce(); cout << f1 << " = " << f1.round(2) << endl;
  f1.reduce(); cout << f1 << " = " << f1.round(2) << endl;
  cout << f1 << (f1 == f2 ? " == " : " != ") << f2 << endl; 
  cout << f1 << " does " << (f1.isExactlySame(f2) ? "" : "not ")
       << "exactly equal " << f2 << endl << endl;

  f2.change_denominator(9);
  cout << f2 << " = " << f2.round(4) << endl;
  cout << f1 << (f1 == f2 ? " == " : " != ") << f2 << endl; 
  cout << f1 << " does " << (f1.isExactlySame(f2) ? "" : "not ")
       << "exactly equal " << f2 << endl << endl;

  f1.set(f2); cout << f1 << " = " << f1.round(1) << endl;
  cout << f1 << (f1 == f2 ? " == " : " != ") << f2 << endl; 
  cout << f1 << " does " << (f1.isExactlySame(f2) ? "" : "not ")
       << "exactly equal " << f2 << endl << endl;

  f1.change_numerator(15); cout << f1 << " = " << f1.round(3) << endl;
  f1.change_numerator(-5); cout << f1 << " = " << f1.round(4) << endl;
  f2.change_denominator(0); cout << f2 << " = " << f2.round(5) << endl;
  f2.change_denominator(2); cout << f2 << " = " << f2.round(6) << endl;

  return EXIT_SUCCESS;
}

/*
Created 0/1
0/1 = 0

Created 3/7
3/7 = 0.429

Changed 0/1 to 6/14
6/14 = 0.42857
6/14 == 3/7
6/14 does not exactly equal 3/7

Could not reduce 3/7
6/14 = 0.43
Reduced 6/14 to 3/7
3/7 = 0.43
3/7 == 3/7
3/7 does exactly equal 3/7

Changed denominator from 7 to 9
3/9 = 0.3333
3/7 != 3/9
3/7 does not exactly equal 3/9

Changed 3/7 to 3/9
3/9 = 0.3
3/9 == 3/9
3/9 does exactly equal 3/9

Could not change numerator from 3 to 15
3/9 = 0.333
Changed numerator from 3 to -5
-5/9 = -0.5556
Could not change denominator from 9 to 0
3/9 = 0.33333
Could not change denominator from 9 to 2
3/9 = 0.333333
*/