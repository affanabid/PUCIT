
#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int n;
    cin>>n;

    double sum = 0;
    int original_n = n;
    while (n>0){
        int digit;
        digit = n%10;
        sum += pow(digit, 3);
        n = n/10;
    }
    if (sum==original_n){
        cout<<"Yes it is an Armstrong number."<<endl;
    }
    else{
        cout<<"No it is not an Armstrong number."<<endl;
    }
}