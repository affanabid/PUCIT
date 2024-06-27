#include<iostream>
using namespace std;

int main(){
  char c;
  cout<<"Enter a character: ";
  cin>>c;

  switch(c) 
  {
    case 'a':
    cout<<"A"<<endl;
    break;
    case 'b':
    cout<<"B"<<endl;
    break;
    case 'c':
    cout<<"C"<<endl;
    break;
    case 'd':
    cout<<"D"<<endl;
    break;
    default:
    cout<<"No"<<endl;
    break;
  }
}