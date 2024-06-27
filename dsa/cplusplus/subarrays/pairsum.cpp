#include<iostream>
using namespace std;

bool pairsum(int arr[], int n, int k){
    for (int i=0; i<n-1; i++){
        for (int j=i+1; j<n; j++){
            if (arr[i] + arr[j] == k){
                cout<<i<<"'th index and "<<j<<"'th index"<<endl;
                return true;
            }
        }
    }
    return false;
}
int main(){
    int n = 5;
    int arr[n] = {2,4,6,8,0};
    int k = 14;
    pairsum(arr, n, k);
}   