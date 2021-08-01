#include <iostream>
using namespace std;

class car
{
  public:
	string name;
	string color;
	double price;

};

int main()
{
	car myCar;
	myCar.name = "Car's name";
	myCar.color = "red";
	myCar.price = 50000;

	cout << "Name: " << myCar.name << endl;
        cout << "Color: " << myCar.color << endl;
        cout << "Price: $" << myCar.price << endl;

        car myCar2;
        myCar2.name = "Volvo";
        myCar2.color = "black";
        myCar2.price = 70000;

        cout << "Name: " << myCar2.name << endl;
        cout << "Color: " << myCar2.color << endl; 
        cout << "Price: $" << myCar2.price << endl;

	system(" pause>0 ");
}
