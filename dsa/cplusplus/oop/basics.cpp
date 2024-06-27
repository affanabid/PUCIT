#include<iostream>
using namespace std;


class student{
    string name;

    public:
    int age;
    bool gender;

// Default Constructor
    student(){
        cout<<"Default Constructor"<<endl;
    }

// Parameterized Constructor 
    student(string s, int a){
        cout<<"Parameterized Constructor"<<endl;
        name = s;
        age = a;
    }

// Copy Constructor
    student (student &a){
        cout<<"Copy Constructor"<<endl;
        name = a.name;
        age = a.age;
        gender = a.gender;
    }
// We prefer not using default copy constructor as it performs shallow copy whereas the copy constructor made by us performs deep
// copy i.e. the pointers are copied as well as the locations to which pointers are pointing to.

    void setName(string s){
        name = s;
    }

    void getName(){
        cout<<name<<endl;
    }

    void info(){
        cout<<"Name: "<<name<<endl;
        cout<<"Age: "<<age<<endl;
        cout<<"Gender: "<<gender<<endl;
    }

// Operator Overloading
    bool operator == (student &a){
        if (name == a.name && age == a.age && gender == a.gender){
            return true;
        }
        return false;
    }

    ~student(){
        cout<<"Destructor called"<<endl;
    }
};

int main(){
    student a;
    string s;
    s = "ali";
    a.setName(s);
    a.age = 10;
    a.gender = 0;
    a.info();

    cout<<"\nNew object"<<endl;
    student b("amir", 10);
    b.getName();
    cout<<b.age<<endl;

    student c = a;
    c.info();

    if (c == a){
        cout<<"Same"<<endl;
    }
    else{
        cout<<"Not Same"<<endl;
    }
}