/*7.	Implement Singly Linked List perform the following operations:  (C++) 
a.	Insert At Last 
b.	Delete from Last 
c.	Display Linked List 
d.	Search Element in LL 
*/ 
#include <iostream>
using namespace std;
// Structure for node
struct Node {
    int data;
    Node* next;
};
Node* head = NULL; // start with empty list
// Insert at last
void insertAtLast(int x) {
    Node* newNode = new Node;
    newNode->data = x;
    newNode->next = NULL;
    if (head == NULL) {
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next != NULL) // go to last node
            temp = temp->next;
        temp->next = newNode; // link new node at end
    }
    cout << "Inserted " << x << " at last.\n";
}
// Delete from last
void deleteFromLast() {
    if (head == NULL) {
        cout << "List is empty!\n";
        return;
    }
    if (head->next == NULL) {
        cout << "Deleted: " << head->data << endl;
        delete head;
        head = NULL;
        return;
    }
    Node* temp = head;
    while (temp->next->next != NULL) // reach 2nd last node
        temp = temp->next;

    cout << "Deleted: " << temp->next->data << endl;
    delete temp->next;
    temp->next = NULL;
}
// Display
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
// Search element
void search(int key) {
    Node* temp = head;
    int pos = 1;
    while (temp != NULL) {
        if (temp->data == key) {
            cout << "Element " << key << " found at position " << pos << endl;
            return;
        }
        pos++;
        temp = temp->next;
    }
    cout << "Element not found!\n";
}
// Main Menu
int main() {
    int ch, x;
    while (true) {
        cout << "\n1.InsertLast 2.DeleteLast 3.Display 4.Search 5.Exit\nEnter choice: ";
        cin >> ch;
        switch (ch) {
            case 1: cout << "Enter data: "; cin >> x; insertAtLast(x); break;
            case 2: deleteFromLast(); break;
            case 3: display(); break;
            case 4: cout << "Enter element to search: "; cin >> x; search(x); break;
            case 5: exit(0);
        }
    }
}
