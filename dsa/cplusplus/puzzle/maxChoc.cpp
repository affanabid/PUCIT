#include<iostream>

using namespace std;

int main(){
    int chocolates = 0;
    int wrappers = 0;
    int rupee = 15;

    while (rupee > 0 || wrappers > 0){
        if (rupee != 0){
            chocolates += 1;
            wrappers += 1;
            rupee -= 1;
        }
        else{
            chocolates += 1;
            wrappers -= 3;
        }
    }
    cout<<chocolates;
}