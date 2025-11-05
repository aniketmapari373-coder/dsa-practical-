/*6.	Implement Singly Linked List perform the following operations: (C++) 
a.	Insert At Begin 
b.	Delete from begin 
c.	Display Linked List 
d.	Count the number of elements in LL  */
#include <iostream>
using namespace std;
// Structure for node
struct Node {
    int data;
    Node* next;
};
Node* head = NULL;  // initially empty list
// Insert at beginning
void insertAtBegin(int x) {
    Node* newNode = new Node;
    newNode->data = x;
    newNode->next = head; // link new node to old head
    head = newNode;       // move head to new node
    cout << "Inserted " << x << " at beginning.\n";
}
// Delete from beginning
void deleteFromBegin() {
    if (head == NULL) {
        cout << "List is empty!\n";
        return;
    }
    Node* temp = head;
    head = head->next; // move head to next node
    cout << "Deleted: " << temp->data << endl;
    delete temp;       // free memory
}
// Display list
void display() {
    if (head == NULL) {
        cout << "List is empty!\n";
        return;
    }
    Node* temp = head;
    cout << "Linked List: ";
    while (temp != NULL) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL\n";
}
// Count number of nodes
void countNodes() {
    int count = 0;
    Node* temp = head;
    while (temp != NULL) {
        count++;
        temp = temp->next;
    }
    cout << "Total nodes: " << count << endl;
}
// Main Menu
int main() {
    int ch, x;
    while (true) {
        cout << "\n1.InsertBegin 2.DeleteBegin 3.Display 4.Count 5.Exit\nEnter choice: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Enter data: "; cin >> x; insertAtBegin(x); break;
            case 2: deleteFromBegin(); break;
            case 3: display(); break;
            case 4: countNodes(); break;
            case 5: exit(0);
        }
    }
}
