#include<iostream>
using namespace std;

int main(){
    int element = 9;
    int n = 3;
    int m = 3;
    int arr[n][m] = {{1,2,3},{4,5,6}, {7,8,9}};
    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++){
            if (arr[i][j] == element){
                cout<<"Element found at: "<<i<<" and "<<j<<endl;
            }
        }
    }
}