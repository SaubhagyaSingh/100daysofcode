#include <iostream>
using namespace std;
/*
1 dan coder: +1 / -1
3 dan coder: +4 / -4
5 dan coder: +6 / -6
7 dan coder: +9 / -9
*/
int main()
{
    int t;
    string u;
    string d;
    cin >> t;
    while (t--)
    {
        cin >> u;
        cin >> d;
        int sum = 0;
        for (int i = 0; i < 5; i++)
        {
            if (u[i] == 1)
            {
                sum = sum + 1;
            }
            else if (u[i] == 3)
            {
                sum = sum + 4;
            }
            else if (u[i] == 5)
            {
                sum = sum + 6;
            }
            else if (u[i] == 7)
            {
                sum = sum + 9;
            }
        }
        for (int i = 0; i < 5; i++)
        {
            if (d[i] == 1)
            {
                sum = sum - 1;
            }
            else if (u[i] == 3)
            {
                sum = sum - 4;
            }
            else if (u[i] == 5)
            {
                sum = sum - 6;
            }
            else if (u[i] == 7)
            {
                sum = sum - 9;
            }
        }
        cout << sum << endl;
    }
}