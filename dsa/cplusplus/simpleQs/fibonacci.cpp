#include<iostream>
using namespace std;

void fibonacci(int num){
    int t1 = 0;
    cout<<t1<<endl;
    int t2 = 1;
    cout<<t2<<endl;
    for (int i = 2; i<num; i++){
        int digit = t1 + t2;
        cout<<digit<<endl;
        t1 = t2;
        t2 = digit;
    }
}
int main(){
    int n;
    cin>>n;

    (fibonacci(n));
    
}