#include<iostream>
using namespace std;

int dec(int n){
    if (n == 0){
        return 0;
    }
    cout<<n<<endl;
    dec(n-1);
}

int inc(int n){
    if (n==0){
        return 0;
    }
    inc(n-1);
    cout<<n<<endl;
}
int main(){
    int n;
    cin>>n;

    cout<<inc(n)<<endl;
    cout<<dec(n)<<endl;

}