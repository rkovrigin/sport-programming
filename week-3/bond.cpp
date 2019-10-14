#include <fstream>
#include <vector>
#include <iostream>

using namespace std;

// ifstream cin("input.txt");
// ofstream cout("output.txt");

const int SMAX = 100000;

int n,x;
vector<int> a;
vector<vector<int> > p;

void readdata()
{
    // cin >> n >> x;
    // a = vector<int>(n);
    // for (int i = 0; i < n; i++)
    //     cin >> a[i];
    a = vector<int>(10);
    n = 10;
    x = -168;
    a[0] = 12;
    a[1] = 27;
    a[2] = 34;
    a[3] = 20;
    a[4] = 29;
    a[5] = 24;
    a[6] = 38;
    a[7] = 38;
    a[8] = 22;
    a[9] = 24;
}

// рекурсивный вывод сертификата
void recout(int i, int s)
{
    if (i > 0)
    {
        recout(i - 1, s - p[i][s] * a[i]);
        if (p[i][s] == 1) cout << '+';
        else cout << '-';
    }
    cout << a[i];
}

int main()
{
    readdata();
    cout << "main" << endl;
    vector<vector<int> > d(n, vector<int>(2 * SMAX, 0));
    // d[i][s] - число способов набрать сумму (s - SMAX) первыми числами a[0], ..., a[i]
    // используется сдвиг SMAX, потому что могут быть отрицательные числа

    p = vector<vector<int> >(n, vector<int>(2 * SMAX, 0));

    d[0][SMAX + a[0]] = 1;

    for (int i = 0; i < n - 1; i++)
    {
        for (int s = 0; s < 2 * SMAX; s++)
        {
            if (d[i][s] == 0) continue;
            cout << s << endl;
            d[i + 1][s + a[i + 1]] += d[i][s];
            // последнее число нужно взять со знаком +
            p[i + 1][s + a[i + 1]] = 1;
            d[i + 1][s - a[i + 1]] += d[i][s];

            // последнее число нужно взять со знаком -
            p[i + 1][s - a[i + 1]] = -1;
        }
    }

    recout(n - 1, SMAX + x);
    cout << endl;
    return 0;
}
