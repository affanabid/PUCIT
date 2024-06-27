#include<iostream>
using namespace std;

int main(){
    int n=7;
    int a[n] = {4, -4, 6, -6, 10, -11, 12};

    int totalSum = 0;
    int b[n];
    for (int i=0; i<n; i++){
        totalSum += a[i];
        b[i] = -(a[i]);
    }
    
    //kadane: 
    int sumnc = 0; //Sum of non contributing
    int sum = 0;
    for (int i=0; i<n; i++){
        sum += b[i];
        if (sum < 0){
            sum = 0;
        }
        sumnc = max(sumnc, sum);
    }
    sumnc *= -1;
    int mx = totalSum - sumnc;
    cout<<mx<<endl;
    
}