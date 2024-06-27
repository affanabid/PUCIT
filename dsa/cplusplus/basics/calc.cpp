#include<iostream>
using namespace std;

int main(){
  int a,b;
  cout<<"Enter two numbers: "<<endl;
  cin>>a>>b;

  char op;
  cout<<"Enter operation: "<<endl;
  cin>>op;
  switch(op){
    case '+': cout<<"a+b: "<<a+b<<endl;
              break;
    case '-': cout<<"a-b: "<<a-b<<endl;
              break;
    case '*': cout<<"a*b: "<<a*b<<endl;
              break;
    case '/': cout<<"a/b: "<<a/b<<endl;  
              break;
    default: cout<<"Enter Valid operator!"<<endl;
  }
}