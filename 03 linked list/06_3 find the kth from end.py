class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
  
        
def find_kth_from_end_mine(list, index):
    slow = list.head
    fast = list.head

    count = 0
    for _ in range(index):
        fast = fast.next
        count += 1

        if fast is None:
            break

    if fast is None:
        if  count == index:
            return list.head
        else: 
            return None

    
    while True:
        slow = slow.next
        fast = fast.next

        if fast is None:
            break
    
    return slow


def find_kth_from_end(list, index):
    slow = list.head
    fast = list.head

    for _ in range(index):
        if fast is None:
            return None
        
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)  # Output: 4

print("-----")
k = 10
result = find_kth_from_end(my_linked_list, k)
if result is None:
    print(None)  # Output: 4
else:
    print(result.value)

print("-----")
k = 5
result = find_kth_from_end(my_linked_list, k)
if result is None:
    print(None)  # Output: 4
else:
    print(result.value)



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

