//Stack implementation using cpp
#include <iostream>
using namespace std;
int main() {
    //max size of stack defined
    int maxs=5;
    int s[maxs];
    int top=-1;
    int i=1;int in;int k;
    while (i>0){
        cout<<"\nEnter choice :\n1 to push\n2 to pop\n3 to peek\n0 to exit\n";
        cin>>i;
        switch(i){
            case 1:
                 if (top==(maxs-1)){
                     cout<<"\nStack is full";
                                }
                 else{
                     top++;
                     cout<<"\nEnter Element to be pushed : ";
                     cin>>in;
                     s[top]=in;
                     cout<<"\n"<<in<<" pushed at position "<<(top);
                      }
                 break;
             case 2:
                 if (top==-1){
                     cout<<"\nStack Empty";
                            }
                else{
                    cout<<"\n"<<s[top]<<" POP from position "<<top;
                    top--;
                    }
                    break;
            case 3:
                if (top!=-1){
                cout<<"\nTop element = "<<s[top];}
                else{
                    cout<<"\nStack Enmpty";
                }
                break;
             }
        }
       
}
