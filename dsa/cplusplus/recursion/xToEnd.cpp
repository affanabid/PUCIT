#include<iostream>

using namespace std;

string moveXtoEnd(string s){
    if (s.length() == 0){
        return "";
    }
    char ch = s[0];
    string new_s = moveXtoEnd(s.substr(1));
    if (ch == 'x'){
        return (new_s + 'x');
    }
    return (ch + new_s);
}
int main(){

    cout<<moveXtoEnd("axbxxc")<<endl;
}