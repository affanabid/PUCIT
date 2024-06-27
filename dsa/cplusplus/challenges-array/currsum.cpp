#include<iostream>
using namespace std;
#include <climits>

int main(){
  int n = 7;
  // cin>>n;

  int a[n] = {2,5,3,2,8,7,6};

  int s = 5;
  int start = 0;
  int end = 1;
  int currSum;
  while (currSum != s){
    if (currSum < s){
        end++;
    }
    else{
        start++;
    }
    int currSum = 0;

    for (int i=start; i<end+1; i++){
        currSum += a[i];
    }
    }
    for (int i=start; i<end+1; i++){
        cout<<a[i]<<endl; 
    }
}