#include <iostream>
using namespace std;

class car
{
  private:
	string name;
	string color;
	double price;
	bool IsBroken;

  public:
	car(string Name, string Color, double Price)
	{
		name = Name;
		color = Color;
		price = Price;
		IsBroken = false;
	}

	void getInfo()
	{
		cout << "Name: " << name << endl;
	        cout << "Color: " << color << endl;
        	cout << "Price: $" << price << endl;

	}

	void crashCar()
	{
		cout << name << " crashed" << endl;
		IsBroken = true;
	}

        void repairCar()
        {
                cout << name << " repaired" << endl;
                IsBroken = false;
        }

	void move()
	{
		if(IsBroken)
			cout << name << " is broken" << endl;
		else
			cout << name << " is driving" << endl;
	}

};

int main()
{
	car ford("Ford", "Red", 50000);
	car volvo("Volvo", "Black", 70000);

	ford.move();
	ford.crashCar();
	ford.move();
	ford.repairCar();
	ford.move();


	system(" pause>0 ");
}
