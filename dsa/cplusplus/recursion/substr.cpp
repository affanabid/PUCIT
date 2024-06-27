#include<iostream>
using namespace std;

void substrings(string s, string ans){
    if (s.length() == 0){
        cout<<ans<<endl;
        return ;
    }
    char ch = s[0];
    string new_s = s.substr(1);
    substrings(new_s, ans);
    substrings(new_s, ans+ch);
}
int main(){
    string s = "abc";
    substrings(s, "");
}
