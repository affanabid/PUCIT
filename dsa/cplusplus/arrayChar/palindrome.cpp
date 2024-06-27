#include<iostream>
using namespace std;

bool palindrome(char name[], int n){
    for (int i=0; i<n; i++){
        if (name[i] != name[n-1-i]){
            return false;
        }
    }
    return true;
}

int main(){
    int n;
    cin>>n;
    char name[n] = "racecar";

    if (palindrome(name, n)){
        cout<<"Palindrome";
    }   
    else{
        cout<<"Not a palindrome";
    }
}