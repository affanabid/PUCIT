#include<iostream>
using namespace std;

int reverse(string s){
    if (s.length() == 0){
        return 0;
    }
    string new_s = s.substr(1); //complete list copied except first character
    reverse(new_s);
    cout<<s[0]<<endl;
}
int main(){
    string s = "Affan";
    cout<<reverse(s)<<endl;
}