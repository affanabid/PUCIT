#include<iostream>
using namespace std;

int main(){
    int r = 3;
    int c = 4;
    int arr[r][c] = {{1,2,3,1},{4,5,6,4}, {7,8,9,7}};
    int row_start = 0, row_end = r-1, column_start = 0, column_end = c-1;

    while (row_start <= row_end && column_start <= column_end){

        //row start
        for (int col=column_start; col <= column_end; col++){
            cout<<arr[row_start][col]<<" ";
        }
        row_start++;
        
        //column end
        for (int row=row_start; row <= row_end; row++){
            cout<<arr[row][column_end]<<" ";
        }
        column_end--;
        
        //row end
        for (int col=column_end; col >= column_start; col--){
            cout<<arr[row_end][col]<<" ";
        }
        row_end--;
        
        //column start
        for (int row=row_end; row >= row_start; row--){
            cout<<arr[row][column_start]<<" ";
        }
        column_start++;
    } 
}
    // for (int i=0; i<r; i++){
    //     for (int j=0; j<c; j++){
    //         cout<<arr[i][j]<<" ";
    //     }
    //     cout<<endl;
    // }