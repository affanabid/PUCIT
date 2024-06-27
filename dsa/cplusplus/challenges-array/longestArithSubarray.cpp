#include<iostream>
using namespace std;

int main(){
    int n = 5;
    cin>>n;
    int arr[n];
    for (int i = 0; i<n; i++){
        cin>>arr[i];
    }
    int pd = arr[1] - arr[0];
    int curr = 2;
    int j = 2;
    int ans = 2;
    while (j<n){
        int current_pd = arr[j]-arr[j-1];
        if (current_pd == pd){
            curr++;
        }
        else{
            pd = current_pd;
            curr = 2;
        }
        ans = max(curr, ans);
        j++;
    }
    cout<<ans<<endl;
}