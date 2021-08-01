#include <iostream>

using namespace std;

float sum(float a, float b);

int main()
{
	cout << sum(2.2, 5) << endl;
	cout << sum(5.2, 75) << endl;
	cout << sum(4, 85) << endl;
	system("pause>0");
	
}

float sum(float a, float b)
{
	return a+b;
}
