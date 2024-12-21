#include <istream>

class Node
{
public:
    int value_;
    Node* next;
    Node();
    Node(int value);
    ~Node();
};