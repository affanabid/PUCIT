#include<iostream>
using namespace std;

int first(int arr[], int n, int key, int i){
    if (i == n){
        return -1;
    }
    if (arr[0] == key){
        return i;
    }
    return first(arr+1, n-1, key, i+1);
}

int last(int arr[], int n, int key, int i){
    if (i == n){
        return -1;
    }
    int restArray = last(arr, n, key, i+1);
    if (restArray != -1){
        return restArray;
    }
    if (arr[i] == key){
        return i;
    }
    return -1;
}
int main(){
    int n = 5, key = 4;
    // cin>>n;
    int arr[n] = {1,4,3,4,2};
    
    cout<<"Array: ";
    for (int i=0; i<n; i++){
        cout<<arr[i]<<",";
    }
    cout<<endl;
    cout<<"First: "<<first(arr, n, key, 0)<<endl;
    cout<<"Last: "<<last(arr, n, key, 0)<<endl;

}