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

	void getInfo()
	{
		cout << "Name: " << name << endl;
	        cout << "Color: " << color << endl;
        	cout << "Price: $" << price << endl;

	}

};

int main()
{
	car myCar("Ford", "Red", 50000);
	car myCar2("Volvo", "Black", 70000);

	myCar.getInfo();
	myCar2.getInfo();

	system(" pause>0 ");
}
