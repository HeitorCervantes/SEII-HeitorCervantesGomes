#include <iostream>
using namespace std;

class car
{
  public:
	string name;
	string color;
	double price;

	car(string Name, string Color, double Price)
	{
		name = Name;
		color = Color;
		price = Price;
	}

};

int main()
{
	car myCar("Ford", "Red", 50000);

	cout << "Name: " << myCar.name << endl;
        cout << "Color: " << myCar.color << endl;
        cout << "Price: $" << myCar.price << endl;

	car myCar2("Volvo", "Black", 70000);

        cout << "Name: " << myCar2.name << endl;
        cout << "Color: " << myCar2.color << endl; 
        cout << "Price: $" << myCar2.price << endl;

	system(" pause>0 ");
}
