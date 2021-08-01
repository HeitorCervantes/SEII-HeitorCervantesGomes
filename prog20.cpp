#include <iostream>
using namespace std;

int main()
{
	int luckyNumbers[5] = { 1,3,5,7,9 };
	cout << luckyNumbers << endl;
	cout << &luckyNumbers[0] << endl;
	cout << luckyNumbers[0] << endl;

	int* luckyPointer = luckyNumbers;
	cout << "Pointing to " << luckyPointer << ", value: " 
<< *luckyPointer << endl;
	luckyPointer++;
	cout << "Pointing to " << luckyPointer << ", value: " 
<< *luckyPointer << endl;

	system(" pause>0 ");
}
