#include<iostream>
using namespace std;
#include <climits>

int main(){
  // int n;
  // cin>>n;

  int a[7] = {2,5,3,8,8,7,6};

  const int N = 1e6+2;
  int b[N];
  for (int i=0; i<N; i++){
    b[i] = -1;
  }

  int mn = INT_MAX;
  for (int i=0; i<7; i++){
    int digit = a[i];
    if (b[digit] != -1){
      mn = min(mn, b[digit]);
    }
    else{
      b[digit] = i;
      }
    }
  // cout<<mn<<endl;
  if (mn == INT_MAX) {
        cout << "No duplicate found" << endl;
    } else {
        cout << mn << endl;
    }

}