#include<iostream>
using namespace std;

int factorial(int n){
    int f = 1;
    for (int i=n; i>0; i--){
        f *= i;
    }
    cout<<f<<endl;
}
int main(){
    int n;
    cin>>n;

    factorial(n);
}