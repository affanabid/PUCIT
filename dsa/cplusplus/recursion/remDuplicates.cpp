#include<iostream>
// #include<string>
using namespace std;

string removeDuplicates(string s){
    if (s.length() == 0){
        return "";
    }
    char ch = s[0];
    string new_s;
    new_s = removeDuplicates(s.substr(1));
    if (ch == new_s[0]){
        return new_s;
    }
    return (ch + new_s);
}
int main(){

    cout<<removeDuplicates("aaaabbcccccccdddeeffgh")<<endl;
}