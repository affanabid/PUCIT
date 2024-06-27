#include<iostream>
#include<cmath>
using namespace std;

// int main() {
//   int a,b;
//   cin>>a>>b;

//   for (int i=a; i<=b; i++)
//     {
//       int j;
//       for (j=2; j<i; j++)
//         {
//           if (i%j==0)
//           {
//             break;
//           }
//         }
//       if (j==i)
//       {
//         cout << i << endl;
//       }
//     }
// }

int main() {
  int n;
  cin>>n;

  bool flag = 0;
//sqrt of n is used because if any number greater than sqrt of that value is a factor of that value, then that value has factor within the range before sqrt of that value.
  for (int i=2; i<sqrt(n); i++){
    if (n%i==0){
      cout<<"Not-prime";
    }
  }
  if (flag==0){
    cout<<"Prime";
  }
}