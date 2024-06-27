#include<iostream>
using namespace std;

bool checkSort(int arr[], int n){
    if (n == 1){
        return true;
    }
    if (arr[0] > arr[1]){
        return false;
    }
    return checkSort(arr+1, n-1);
}

bool sorted(int arr[], int n){
    if (n==1){
        return true;
    }

    bool restArray = sorted(arr+1, n-1);
    return (arr[0]<arr[1] && restArray);
}
int main(){
    int n=5;
    int arr[n] = {1,2,1,1,2};

    if (checkSort(arr, n) == true){
        cout<<"Sorted"<<endl;
    }
    else{
        cout<<"Not Sorted"<<endl;
    }
}