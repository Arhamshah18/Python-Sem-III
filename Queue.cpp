#include <iostream>
using namespace std;
public void que(a){
    int qu[a];int k=4;int ind=0;int t=0;int i;
    while(k!=0){
    cout<<"queue menu :\n1 to Enqueue\n2 to dequeue\n3 to peek\n";
    cin>>k;
    if(k==1){
        if(ind<a-1){
        cout<<"Enter element to enqueue : ";
        cin>>t;
        qu[ind]=t;
        ind++;}
    else{
        cout<<"Queue is full";
    }
    }
    else if(k==2){
        for(i=0,i<a,i++){
            qu[i]=qu[i+1];
        }
        cout<<"Dequeue successfull";
    }
    else if(k==3){
        cout<<"--->"<<qu[0];
    }
    else if(k!=0){
        cout<<"Invalid option";
    }
    }
}
int main() {
   int y; 
   cout<<"Enter required length for queue : ";
   cin>>y;
   q=qu(y);
   
}
