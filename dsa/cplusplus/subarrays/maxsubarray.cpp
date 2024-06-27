#include<iostream>
using namespace std;

//Time complexity: O(n)
int main(){
    int n=5;

    int a[n] = {-1,4,-6,7,-4};
    // for (int i=0; i<n; i++){
    //     cin>>a[i];
    // }
    int currSum = 0;
    int mx = 0;
    for (int i=0; i<n; i++){
        currSum += a[i];
        if (currSum < 0){
            currSum = 0;
        }
        mx = max(mx, currSum);
    }
    cout<<mx<<endl;
}

//Time complexity: O(n2)
// int main(){
//         int n=5;

//     int a[n] = {1, -4, 3, 2, 1};
//     // for (int i=0; i<n; i++){
//     //     cin>>a[i];
//     // }
//     int currSum[n+1];
//     currSum[0] = 0;

//     for (int i=1; i<=n; i++){
//         currSum[i] = currSum[i-1] + a[i-1]; //cumulative array made
//     }
//     // for (int i=0; i<=n; i++){
//     //     cout<<currSum[i]<<" ";
//     // }
//     int mx = 0;
//     for (int i=1; i<=n; i++){
//         int sum = 0;
//         for (int j = 0; j<i; j++){
//             sum = currSum[i] - currSum[j];
//             mx = max(sum, mx);
//         }
//     }
//     cout<<mx<<endl;
// }

//Time compleity: O(n3)
// int main(){
    // int n=4;

    // int a[n] = {-1, 4, 7, 2};
    // // for (int i=0; i<n; i++){
    // //     cin>>a[i];
    // // }
    // int mx = 0;
    
//     for (int i=0; i<n; i++){
//         for (int j = i; j<n; j++){
//             int sum = 0;
//             for (int k=i; k<=j; k++){
//                 // cout<<a[k]<<" ";
//                 sum += a[k];
//             }
//             // cout<<endl;
//             mx = max(sum, mx);
//         }
        
//     }
//     cout<<mx<<endl;
// }