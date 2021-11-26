#include <iostream>
using namespace std;

const int SIZE = 26;
int control{};

void Charter(bool* arr);
bool* Not(bool* arr);
bool* Сonjunction(bool* arr, bool* arr2);
bool* Disjunction(bool* arr, bool* arr2);
bool* Difference(bool* arr, bool* arr2);
bool* Xor(bool* arr, bool* arr2);


void Charter(bool* arr)
{
	size_t power{};
	for (size_t i{}; i < SIZE; ++i)
	{
		if (arr[i] == 1)
		{
			power++;
		}
	}

	char* arr_char = new char[power+1];
	for (size_t i{}, p{}; i < SIZE; ++i)
	{
		if (arr[i] == 1)
		{
			arr_char[p] = (int )(65 + i);
			++p;
		}
	}
	control += power;
	//Вывод
	for (size_t i{}; i < SIZE; ++i)
	{
		cout << arr[i];
	}
	cout << "\tCardinality - " << power << "  \t";
	for (size_t p{}; p < power; ++p)
	{
		cout << arr_char[p];
	}
	cout << endl;
}

bool* Not(bool* arr)
{
	for (size_t i{}; i < SIZE; ++i)
	{
		arr[i] = !arr[i];
	}
	return arr;
}

bool* Сonjunction(bool* arr, bool* arr2)
{
	bool arr_r[SIZE]{};
	for (size_t i{}; i < SIZE; ++i)
	{
		arr_r[i] = arr[i] && arr2[i];
	}	
	Charter(arr_r);
	return arr_r;
}

bool* Disjunction(bool* arr, bool* arr2)
{
	bool arr_r[SIZE]{};
	for (size_t i{}; i < SIZE; ++i)
	{
		arr_r[i] = arr[i] || arr2[i];
	}
	Charter(arr_r);
	return arr_r;
}

bool* Difference(bool* arr, bool* arr2)
{
	bool arr_r[SIZE]{};
	for (size_t i{}; i < SIZE; ++i)
	{
		arr_r[i] = arr[i] && !arr2[i];
	}
	Charter(arr_r);
	return arr_r;
}

bool* Xor(bool* arr, bool* arr2)
{
	bool arr_r[SIZE]{};
	for (size_t i{}; i < SIZE; ++i)
	{
		arr_r[i] = (arr[i] && !arr2[i]) || (arr2[i] && !arr[i]);
	}
	Charter(arr_r);
	return arr_r;
}

void main()
{
	bool arr_A[SIZE] = { 1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
	bool arr_B[SIZE] = { 1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };

	cout << "Array A\t\t";
	Charter(arr_A);
	cout << "Array B\t\t";
	Charter(arr_B);

	cout << "Intersection\t";
	Сonjunction(arr_A, arr_B);
	
	cout << "Union\t\t";
	Disjunction(arr_A, arr_B);

	cout << "Difference A-B\t";
	Difference(arr_A, arr_B);

	cout << "Difference B-A\t";
	Difference(arr_B, arr_A);

	cout << "A xor B\t\t";
	Xor(arr_A, arr_B);

	cout << "Not A\t\t";
	Charter(Not(arr_A));
	cout << "Not B\t\t";
	Charter(Not(arr_B));

	cout << "Coltrol number = " << control << endl;
	system("pause");
}

