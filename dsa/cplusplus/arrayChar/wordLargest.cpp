#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    cin.ignore();

    char sentence[n+1];

    cin.getline(sentence, n+1);
    // cin.ignore();
    // for (int i=0; i<n; i++){
    //     cout<<sentence[i]<<endl;
    // }
    int i = 0, maxLength = 0, currLength = 0;
    int start=0, s=0, end=0, e=0;

    while (1){

        if (sentence[i] == ' ' || sentence[i] == '\0'){
            // maxLength = max(maxLength, currLength);

            if (currLength > maxLength){
                maxLength = currLength;
                start = s;
                end = i-1;
            }
            currLength = 0;
            s = i + 1;
        }
        else{
            currLength++;
        }
        if (sentence[i] == '\0'){
            break;
        }
        i++; 
    }
    // cout<<maxLength<<endl;
    cout<<"Longest word: ";
    for (int i=start; i<=end; i++){
        cout<<sentence[i];
    }
    // cout<<start<<" "<<end<<endl;

}
