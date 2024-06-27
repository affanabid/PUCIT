#include<iostream>
using namespace std;

int linearSearch(int arr[], int x, int n){
    for (int i=0; i<n; i++){
        if (arr[i]==x){
            return i;
        }
    }
    return -1;
}

int main(){
    int n;
    cin>>n;

    int arr[n];
    for (int i=0; i<n; i++){
        cin>>arr[i];
    }
    cout<<linearSearch(arr, 10, n);
}