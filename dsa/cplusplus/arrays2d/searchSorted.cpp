#include<iostream>
using namespace std;

int main(){
    int r = 3;
    int c = 4;
    int arr[r][c] = {{1,4,7,11},{2,5,8,12}, {3,6,9,16}, {10,13,14,17}};
    int row = 0, column = c-1, element=8;
    while (row >= 0 && column >= 0){
        if (arr[row][column] == element){
            cout<<"Position: "<<row<<","<<column<<endl;
            break;
        }
        else if (arr[row][column] > element){
            column--;
        }
        else{
            row++;
        }
    }
}