#include<iostream>
using namespace std;

int main(){
    // int n = 5;
    // cin>>n;
    // int arr[n];
    // for (int i = 0; i<n; i++){
    //     cin>>arr[i];
    // }
    int n = 5;
    int arr[n] = {5, 3,9,1,0};

    for (int i=0; i<n; i++){
        int current = arr[i];
        int j = i-1;
        while (arr[j]>current && j >=0){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = current;
    }
    for (int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
}