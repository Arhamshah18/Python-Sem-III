#include <iostream>
using namespace std;
class Queue {
public:
    void que(int a) {
        const int ms = 100;
        int capacity = (a > ms)?ms:a;
        int qu[ms];
        int k = 6;
        int ind = 0;
        int t = 0;
        while(k != 0){
            cout << "\nQueue menu :\n1 to Enqueue\n2 to dequeue\n3 to peek\n4 to display queue\n5 to check is Queue is Empty\n0 to exit\n";
            cin >> k;
            if(k == 1){
                if(ind < capacity){
                    cout << "Enter element to enqueue : ";
                    cin >> t;
                    qu[ind] = t;
                    ind++;
                } else {
                    cout << "Queue is full\n";
                }
            }
            else if(k == 2){
                if(ind == 0){
                    cout << "Queue is empty\n";
                }else{
                    for(int i = 0; i < ind - 1; i++){
                        qu[i] = qu[i + 1];
                    }
                    ind--;
                    cout << "Dequeue successful\n";
                }
            }
            else if(k==3){
                if(ind == 0){
                    cout << "Queue is empty\n";
                }else{
                    cout << "--->" << qu[0] << "\n";
                }
            }
            else if(k==4){
                for(int i=0;i<=ind;i++){
                    cout<<"--->"<<qu[i]<<" ";
                }
            }
            else if(k==5){
                if(ind==0){
                    cout<<"Queue Empty";
                }
                else
                    cout<<"Queue is not empty , has "<<ind+1<<" elements ";
            }
            else if(k != 0){
                cout << "Invalid option\n";
                           }
        }
    }
    
};

int main() {
    int y; 
    cout << "Enter required length for queue : ";
    cin >> y;
    Queue q;
    q.que(y);
    return 0;
}
