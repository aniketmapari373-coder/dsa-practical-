#include <iostream>
#include <string>
#include <algorithm> // for reverse()
using namespace std;
// Node for stack (linked list)
struct Node {
    char data;
    Node* next;
};
Node* topNode = NULL;
// Push operation
void push(char x) {
    Node* newNode = new Node{x, topNode};
    topNode = newNode;
}
// Pop operation
char pop() {
    if (topNode == NULL) return '\0';
    char x = topNode->data;
    Node* temp = topNode;
    topNode = topNode->next;
    delete temp;
    return x;
}
// Peek operation
char peek() {
    return (topNode) ? topNode->data : '\0';
}
// Precedence function
int prec(char c) {
    if (c == '^') return 3;
    if (c == '*' || c == '/') return 2;
    if (c == '+' || c == '-') return 1;
    return -1;
}
// Check if character is operand
bool isOperand(char c) {
    return (isalnum(c)); // letters or digits
}
// Infix to Postfix Conversion
string infixToPostfix(string infix) {
    string result = "";
    topNode = NULL; // reset stack for clean run
    for (char c : infix) {
        if (isOperand(c))
            result += c;
        else if (c == '(')
            push(c);
        else if (c == ')') {
            while (peek() != '(' && topNode != NULL)
                result += pop();
            pop(); // remove '('
        } else {
            while (topNode && prec(peek()) >= prec(c))
                result += pop();
            push(c);
        }
    }
    while (topNode)
        result += pop();
    return result;
}
// Infix to Prefix Conversion
string infixToPrefix(string infix) {
    // Step 1: Reverse infix
    reverse(infix.begin(), infix.end());
    // Step 2: Swap '(' and ')'
    for (char &c : infix) {
        if (c == '(') c = ')';
        else if (c == ')') c = '(';
    }
    // Step 3: Get postfix of modified infix
    string postfix = infixToPostfix(infix);
    // Step 4: Reverse postfix to get prefix
    reverse(postfix.begin(), postfix.end());
    return postfix;
}
int main() {
    string infix;
    cout << "Enter an infix expression: ";
    cin >> infix;
    cout << "\nInfix Expression : " << infix;
    cout << "\nPostfix Expression : " << infixToPostfix(infix);
    cout << "\nPrefix Expression  : " << infixToPrefix(infix);
    return 0;
}
