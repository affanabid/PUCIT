#include<iostream>
using namespace std;

int main(){
    int n = 6;
    int a[n] = {0, -9, 4, 2, 3, 5};
    int check[10];
    for (int i=0; i<10; i++){
        check[i] = false;
    }
    for (int i=0; i<n; i++){
        if (a[i] >= 0){
            check[a[i]] = true;
        }
    }
    for (int i=0; i<10; i++){
        if (check[i] == false){
            cout<<i<<endl;
            break;
        }
    }
}