#include<iostream>
using namespace std;

int replacePI(string s){
    string new_s;
    if (s.length() == 1){
        return 0;
    }
    if (s[0] == 'p' && s[1] == 'i'){
        cout<<"3.14";
        new_s = s.erase(0, 2);
    }
    else {
        cout<<s[0];
        new_s = s.erase(0, 1);
    }
    
    replacePI(new_s);
}
int main(){

    cout<<replacePI("pippxxppiixipi")<<endl;
}