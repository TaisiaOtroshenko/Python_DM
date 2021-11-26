#include <iostream>
#include <vector>
using namespace std;

const int SIZE = 6;
size_t power{};
vector<vector<bool>> Multi(vector<vector<bool>> arr1, vector<vector<bool>> arr2) //умножение матриц
{
    vector<vector<bool>> arr_r(SIZE,vector<bool>(SIZE,0));
    for (size_t i{}; i < SIZE; ++i)
    {
        for (size_t j{}; j < SIZE; ++j)
        {
            for (size_t k{}; k < SIZE; ++k)
            {
                    arr_r[i][j] = arr_r[i][j]||(arr1[i][k] && arr2[k][j]);
            }
        }
    }
    return arr_r;
}
inline void Output(vector<vector<bool>> &arr, string type)
{
    //output
    cout << type << endl;
    for (size_t i{}; i < SIZE; ++i)
    {
        for (size_t j{}; j < SIZE; ++j)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    //control
    for (size_t i{}; i < SIZE; ++i)
    {
        for (size_t j{}; j < SIZE; ++j)
        {
            if (arr[i][j] == 1)
            {
                ++power;
            }
        }
    }
}
void Ref(vector<vector<bool>> arr)
{
    for (size_t i{}; i < SIZE; ++i)
    {
        arr[i][i] = 1;
    }
    Output(arr, "Reflexive closure:");
}
void Symm(vector<vector<bool>> arr)
{
    for (size_t i{}; i < SIZE; ++i)
    {
        for (size_t j{}; j < SIZE; ++j)
        {
            if (arr[i][j] == 1)
            {
                arr[j][i] = 1;
            }
        }
    }
    Output(arr, "Symmetrical closure:");
}
void Tran1(vector<vector<bool>> arr) //объединение степеней матрицы
{
    vector<vector<bool>> arr_prew = arr;
    vector<vector<bool>> arr_new = arr;
    vector<vector<bool>> arr_r = arr;
    for (size_t i{}; i < SIZE; ++i)
    {
        arr_new = Multi(arr_new, arr);
        for (size_t i{}; i < SIZE; ++i)
        {
            for (size_t j{}; j < SIZE; ++j)
            {
                arr_r[i][j] = arr_r[i][j] || arr_new[i][j];
            }
        }
    }
    Output(arr_r, "Transitive closure (1st way):");
}
void Tran2(vector<vector<bool>> arr) //алгоритм Уоршелла
{ 
    for (size_t k{}; k < SIZE; ++k)
    {
        for (size_t i{}; i < SIZE; ++i)
        {
            for (size_t j{}; j < SIZE; ++j)
            {
                if (arr[i][k] && arr[k][j])
                {
                    arr[i][j] = 1;
                }
            }
        }
    }
    Output(arr, "Transitive closure (2nd way):");
}

int main()
{
    vector<vector<bool>> arr = { {0, 1, 1, 1, 0, 1}, {0, 0, 0, 0, 1, 0}, {0, 1, 1, 1, 1, 0}, {0, 1, 0, 0, 1, 0}, {0, 1, 0, 1, 1, 0}, {0, 1, 1, 1, 1, 0} };
    //vector<vector<bool>> arr = { {0, 1, 0, 0, 0, 0}, {0, 0, 1, 0, 0, 0}, {0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0}, {0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0} }; //test
    Output(arr, "Initial ratio R:");
    Ref(arr);
    Symm(arr);
    Tran1(arr);
    Tran2(arr);
    cout << "Control number - " << power << endl;

    system("pause");
}
