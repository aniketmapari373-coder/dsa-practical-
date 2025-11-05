#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
// Structure to store student details
struct student {
    int ID;
    char name[40];
    float cgpa;
};
// Function to input student data
void accept(student *s, int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nEnter ID: ";
        cin >> s[i].ID;
        cout << "Enter Name: ";
        cin >> s[i].name;
        cout << "Enter CGPA: ";
        cin >> s[i].cgpa;
    }
}
// Display all student data
void display(student *s, int n) {
    cout << "\nID\tName\tCGPA\n";
    for (int i = 0; i < n; i++)
        cout << s[i].ID << "\t" << s[i].name << "\t" << s[i].cgpa << endl;
}
// Linear Search by ID
int linearsearch(student *s, int x, int n) {
    for (int i = 0; i < n; i++)
        if (s[i].ID == x)
            return i;
    return -1;
}
// Binary Search by ID (Array must be sorted by ID)
int binarysearch(student *s, int x, int n) {
    int low = 0, high = n - 1, mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (s[mid].ID == x)
            return mid;
        else if (x < s[mid].ID)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}
// Bubble Sort by Name (Ascending)
void bubblesort(student *s, int n) {
    student temp;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (strcmp(s[j].name, s[j + 1].name) > 0) {
                temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
}
// Selection Sort by CGPA (Ascending)
void selectionsort(student *s, int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++)
            if (s[j].cgpa < s[minIndex].cgpa)
                minIndex = j;
        swap(s[i], s[minIndex]);
    }
}
// Insertion Sort by CGPA (Descending)
void insertionsort(student *s, int n) {
    for (int i = 1; i < n; i++) {
        student key = s[i];
        int j = i - 1;
        while (j >= 0 && s[j].cgpa < key.cgpa) {
            s[j + 1] = s[j];
            j--;
        }
        s[j + 1] = key;
    }
}
int main() {
    int ch, n = 0, x;
    char choice;
    student *s = NULL;
    while (true) {
        cout << "\n1.Create 2.Add 3.Linear 4.Binary 5.Bubble 6.Selection 7.Insertion 8.Exit\n";
        cout << "Enter choice: ";
        cin >> ch;
        switch (ch) {
            case 1:
                cout << "Enter number of students: ";
                cin >> n;
                s = (student*) malloc(n * sizeof(student));
                accept(s, n);
                display(s, n);
                break;
            case 2:
                cout << "Add more student (y/n): ";
                cin >> choice;
                if (choice == 'y') {
                    s = (student*) realloc(s, (n + 1) * sizeof(student));
                    cout << "Enter ID Name CGPA: ";
                    cin >> s[n].ID >> s[n].name >> s[n].cgpa;
                    n++;
                }
                display(s, n);
                break;
            case 3:
                cout << "Enter ID to search: ";
                cin >> x;
                int pos;
                pos = linearsearch(s, x, n);
                if (pos != -1)
                    cout << "Found: " << s[pos].name << " " << s[pos].cgpa << endl;
                else
                    cout << "Not found\n";
                break;
            case 4:
                cout << "Enter ID to search: ";
                cin >> x;
                pos = binarysearch(s, x, n);
                if (pos != -1)
                    cout << "Found: " << s[pos].name << " " << s[pos].cgpa << endl;
                else
                    cout << "Not found\n";
                break;
            case 5:
                bubblesort(s, n);
                display(s, n);
                break;
            case 6:
                selectionsort(s, n);
                display(s, n);
                break;
            case 7:
                insertionsort(s, n);
                display(s, n);
                break;
            case 8:
                free(s);
                exit(0);
        }
    }
}
