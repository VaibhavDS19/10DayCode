#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the sillyGame function below.
 */
string sillyGame(int n) {
    /*
     * Write your code here.
     */
     string players[2] = { "Alice", "Bob" };
     int count = 0;
     bool prime[n+1]; 
     memset(prime, true, sizeof(prime)); 
  
     for (int p=2; p*p<=n; p++) 
     { 
         if (prime[p]) 
           for (int i=p*p; i<=n; i += p)
             prime[i] = false; 
     }
     for(int p=2; p<=n; p++) 
       if (prime[p])
        count++;

     return players[1-count&1];

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int g;
    cin >> g;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int g_itr = 0; g_itr < g; g_itr++) {
        int n;
        cin >> n;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        string result = sillyGame(n);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
