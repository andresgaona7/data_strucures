#include "Node.h"
#include <iostream>

class LinkedList
{
private:
    Node* head_;
    Node* tail_;
    int length_;
public:
    LinkedList();
    ~LinkedList();

    void Append(int value);
    void Prepend(int value);
    Node PopFirst();
    Node PopLast();
    void Insert(int index, int value);
    Node Remove(int index);
    void Reverse();
    void Show();
};
