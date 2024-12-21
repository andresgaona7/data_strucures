#include "LinkedList.h"

LinkedList::LinkedList()
{
    head_ = nullptr;
    tail_ = nullptr;
    length_ = 0;
}

LinkedList::~LinkedList()
{
}

void LinkedList::Show()
{
    Node* temp = head_;
    for (int i = 0; i < length_; i++)
    {
        std::cout << (*temp).value_ << " ";
        temp = (*temp).next;
    }
    
    std::cout << std::endl;
}

void LinkedList::Append(int value)
{
    if(length_ == 0)
    {
        head_ = new Node(value);
        tail_ = head_;
        length_++;
        return;
    }

    (*tail_).next = new Node(value);
    tail_ = (*tail_).next;
    length_++;
}

void LinkedList::Prepend(int value)
{
    if (length_ == 0)
    {
        head_ = new Node(value);
        tail_ = head_;
        length_++;
        return;
    }
    
    Node* temp = new Node(value);
    (*temp).next = head_;
    head_ = temp;
    length_++;
}

Node LinkedList::PopFirst()
{
    if (length_ == 0)
    {
        std::cout << "Nothing to pop" << std::endl;
        return Node();
    }
    
    Node* temp = head_; 
    head_ = (*head_).next;
    length_--;
    return *temp;
}

Node LinkedList::PopLast()
{
    if (length_ == 0)
    {
        std::cout << "Nothing to pop" << std::endl;
        return Node();
    }

    Node* temp = head_;
    for (int i = 0; i < length_ - 2; i++)
    {
        temp = (*temp).next;
    }
    
    Node* next_node = (*temp).next;
    (*temp).next = nullptr;
    tail_ = temp;
    length_--;
    return *next_node;
}

void LinkedList::Insert(int index, int value)
{
    if (index < 0 || index > length_)
    {
        std::cout << "Index out of limits" << std::endl;
        return;
    }

    if (index == 0)
    {
        Prepend(value);
        return;
    }

    if (index == length_)
    {
        Append(value);
        return;
    }
    
    Node* temp = head_;
    for (int i = 0; i < index - 1; i++)
    {
        temp = (*temp).next;
    }
    
    Node* new_node = new Node(value);
    (*new_node).next = (*temp).next;
    (*temp).next = new_node;
    length_++;
}

Node LinkedList::Remove(int index)
{
    if (index < 0 || index > length_)
    {
        std::cout << "Index out of limits" << std::endl;
        return Node();
    }

    if (index == 0)
    {
        return PopFirst();
    }

    if (index == length_)
    {
        return PopLast();
    }
    
    Node* temp = head_;
    for (int i = 0; i < index - 1; i++)
    {
        temp = (*temp).next;
    }

    Node* next_node = (*temp).next;
    (*temp).next = (*next_node).next;
    length_--;
    return *next_node;
}

void LinkedList::Reverse()
{
    Node* before = nullptr;
    Node* temp = head_;
    Node* after;

    head_ = tail_;
    tail_ = temp;

    for (int i = 0; i < length_; i++)
    {
        after = (*temp).next;
        (*temp).next = before;
        before = temp;
        temp = after;
    }
}

