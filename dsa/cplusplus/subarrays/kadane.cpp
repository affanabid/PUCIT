#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    // int a[n] = {-1,8,-6,1,-4};
    int a[n];
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    int maxSum = 0;
    int sum = 0;
    for(int i=0; i<n; i++){
        sum += a[i];
        if (sum < 0){
            sum = 0;
        }
        maxSum = max(maxSum, sum );
    }
    cout<<maxSum<<endl;
}