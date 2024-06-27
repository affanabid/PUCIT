#include<iostream>
using namespace std;

int main(){
    int n = 5;
    cin>>n;
    int arr[n];
    for (int i = 0; i<n; i++){
        cin>>arr[i];
    }
    int days = 0;
    int mx = arr[0];                                    
    for (int i=1; i<n-1; i++){
        if (arr[i] > mx && arr[i] > arr[i+1]){
            days++;
        }
        mx = max(mx,arr[i]);
    }
    cout<<days<<endl;
}