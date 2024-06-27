#include<iostream>
using namespace std;

void increment(int *a){
    (*a)++;
}

int main(){
    int a = 4;

    int *ptr = &a;
    
    increment(ptr);
    cout<<a<<endl;

    // cout<<a<<" and "<<b<<endl;
}