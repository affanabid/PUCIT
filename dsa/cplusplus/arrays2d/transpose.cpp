#include<iostream>
using namespace std;

int main(){
    int r = 3;
    int c = 3;
    int arr[r][c] = {{1,2,3},{4,5,6}, {7,8,9}};
    int result[r][c];
    for (int i=0; i<r; i++){
        for (int j=0; j<c; j++){
            cout<<arr[j][i]<<" ";
            // result[i][j] = arr[j][i];
        }
        cout<<endl;
    }
}