#include "LinkedList.h"

int main()
{
    std::cout << "Running linked list" << std::endl;
    LinkedList myList;

    // Append
    myList.Append(1);
    myList.Append(2);
    myList.Append(3);
    myList.Append(4);
    myList.Append(5);
    myList.Show();
    
    // Prepend
    myList.Prepend(-1);
    myList.Prepend(-2);
    myList.Prepend(-3);
    myList.Prepend(-4);
    myList.Prepend(-5);
    myList.Show();

    // Insert
    myList.Insert(0, 0);
    myList.Show();
    myList.Insert(5, 0);
    myList.Show();
    myList.Insert(12, 0);
    myList.Show();

    // Pop Firt
    myList.PopFirst();
    myList.Show();

    // Pop Last
    myList.PopLast();
    myList.Show();

    // Remove
    myList.Remove(0);
    myList.Show();

    myList.Remove(10);
    myList.Show();

    myList.Remove(3);
    myList.Show();

    std::cout << "TESTING" << std::endl;
    // Reverse
    myList.Reverse();
    myList.Show();
    
    return 0;
}