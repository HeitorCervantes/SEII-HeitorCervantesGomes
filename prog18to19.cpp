#include <iostream>

using namespace std;

void celebrateBirthday(int* age);

int main()
{
	int myAge = 33;
	cout<< "before function, age  " << myAge << endl;
	celebrateBirthday(&myAge);
	cout<< "after function, age  " << myAge << endl;

        system("pause>0");

}

void celebrateBirthday(int* age)
{
	(*age)++;
	cout << "Yeeey, celebrated " << *age << ". birthday" << endl;
}
