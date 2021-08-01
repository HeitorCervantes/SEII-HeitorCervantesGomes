#include <iostream>

using namespace std;

float sum(float a, float b);
void introduceMe(string name, int age);

int main()
{ 
        cout << sum(2.2, 5) << endl;
        cout << sum(5.2, 75) << endl;
        cout << sum(4, 85) << endl;
	introduceMe("heitor", 22);
	introduceMe("Italo", 52);

        system("pause>0");

}

float sum(float a, float b)
{ 
        return a+b;
}

void introduceMe(string name, int age)
{
	cout << "My name is " << name << endl;
	cout << "I am  " << age << " years old." << endl;
}
