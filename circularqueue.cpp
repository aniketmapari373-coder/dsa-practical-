#include<iostream>
using namespace std;
class CircularQueue{
public:
	int arr[4], front, rear, size ;
	CircularQueue(){
		front = rear = -1;
		size = 4;
	}	
	bool isEmpty(){
		if(front==rear) return true;
		return false;
	}	
	bool isFull(){
		if( (rear+1)%size==front ) return true;
		return false;
	}	
	void dequeue(){
		if(isEmpty()) cout << " Queue is empty " << endl;
		else front = (front+1)%size;
	}
	void enqueue(int val){
		if(isFull()) cout << " Queue is Full " << endl;
		else {
			rear = (rear+1)%size;
			arr[rear] = val;
		}
	}
	void display(){
		if(isEmpty()) cout << " Empty queue " << endl;
		else {
			for (int i = (front + 1) % size; i < rear;i = (i + 1) % size) {
				cout << arr[i] << " ";
			}
        		cout << arr[rear] << endl;
		}	}
};
int main () {	
	CircularQueue cq ;	
	while(true){	
		cout << "1. Enqueue " << endl << "2. Dequeue " << endl << "3. Display " << endl << "4. Exit "<<endl;		
		int ch ;
		cout << "Enter your choice : ";
		cin >> ch;		
		switch(ch){
			case 1 :
				int val ;
				cout << "Enter a number to insert : ";
				cin >> val;
				cq.enqueue(val);
				break;
			case 2 :
				cq.dequeue();
				break;
			case 3 :
				cq.display();
				break;
			case 4 :
				return 0;
			default :
				cout << "Enter a valid choice";
        }}}
