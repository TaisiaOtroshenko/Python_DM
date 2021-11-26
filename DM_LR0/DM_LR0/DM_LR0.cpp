#include <iostream>
#include <limits.h>
using namespace std;

const int COUNT = 4;

void Full(int* arr, int COUNT)
{

	cout << "Введите " << COUNT << " чисел для тестирования" << endl;
	for (int i = 0; i < COUNT; i++)
	{
		cin >> arr[i];
	}
}

int main()
{
	setlocale(0, "");
	/*
#pragma region Task1
	int arr1[COUNT]{};
	Full(arr1, COUNT);
	int min = LONG_MAX, max = LONG_MIN;

	for (int i = 0; i < COUNT; i++)
	{
		if (arr1[i] >= max)
			max = arr1[i];
		if (arr1[i] <= min)
			min = arr1[i];
	}
	cout << "Минимальное число: " << min << endl;
	cout << "Максимальное число: " << max << endl;
#pragma endregion

#pragma region Task2
	
int arr2[COUNT]{};
	Full(arr2, COUNT);
	int max2 = LONG_MIN, max1 = LONG_MIN, i_max{};

	for (int i = 0; i < COUNT; i++)
	{
		if (arr2[i] >= max1)
		{
			max1 = arr2[i];
			i_max = i;
		}
	}
	for (int i = 0; i < COUNT; i++)
	{
		if (arr2[i] >= max2 && i != i_max)
			max2 = arr2[i];
	}
	cout << "Максимальные числа: " << max1 << ", " << max2 << endl;

#pragma endregion
	*/
#pragma region Task3
	while (true)
	{
		int arr3[COUNT]{};
		Full(arr3, COUNT);
		float m{};

		for (int i = 0; i < COUNT - 1; i++)
		{
			for (int i = 0; i < COUNT - 1; i++)
			{
				if (arr3[i] < arr3[i + 1])
				{
					arr3[i + 1] += arr3[i];
					arr3[i] = arr3[i + 1] - arr3[i];
					arr3[i + 1] = arr3[i + 1] - arr3[i];
				}
			}
		}
		if (COUNT % 2 == 0)
		{
			m = (arr3[COUNT / 2] + arr3[COUNT / 2 - 1]) / (float)2;
		}
		else
		{
			m = arr3[COUNT / 2];
		};

		cout << "Медиана монжества: " << m << endl;
	}
#pragma endregion

#pragma region Task4
	int arr4[COUNT]{};
	Full(arr4, COUNT);
	int t_count{}, m_count{}, n{};

	for (int i = 0; i < COUNT - 1; i++)
	{
		for (int i = 0; i < COUNT - 1; i++)
		{
			if (arr4[i] > arr4[i + 1])
			{
				arr4[i + 1] += arr4[i];
				arr4[i] = arr4[i + 1] - arr4[i];
				arr4[i + 1] = arr4[i + 1] - arr4[i];
			}
		}
	}
	for (int i = 0; i < COUNT - 1; i++)
	{
		if (arr4[i] == arr4[i + 1])
		{
			t_count ++;
		}
		else if (t_count >= m_count)
		{
			m_count = t_count;
		}
		else if (t_count == m_count)
		{
			m_count = 0;
		}

	}
	if (m_count == 0)
	{
		cout << "Нет моды" << endl;
	}
	else
	{
		cout << "Мода монжества: " << m_count+1 << endl;
	}
#pragma endregion

#pragma region Task5

#pragma endregion

#pragma region Task6

#pragma endregion

#pragma region Task7

#pragma endregion

#pragma region Task8

#pragma endregion

#pragma region Task9

#pragma endregion

#pragma region Task10

#pragma endregion
	system("pause");
}