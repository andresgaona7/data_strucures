import time

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if end_index - start_index < 1:
            return None
        
        before = None
        current = self.head

        for count in range(self.length):
            if count == start_index:
                tail_big = before
                tail_small = current

            if count == end_index:
                head_small = current
                head_big = current.next

            if count >= start_index and count <= end_index:
                after = current.next
                current.next = before
                before = current
                current = after
            else:
                before = current
                current = current.next
        
        if start_index == 0:
            self.head = head_small
            return

        tail_big.next = head_small
        tail_small.next = head_big

    def reverse_between_course(self, start_index, end_index):
        if self.length <= 1:
            return
    
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node
    
        for i in range(start_index):
            previous_node = previous_node.next
    
        current_node = previous_node.next
    
        for i in range(end_index - start_index):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = previous_node.next
            previous_node.next = node_to_move
    
        self.head = dummy_node.next

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
print("Reversed sublist (2, 3): ")
linked_list.reverse_between(2, 3)
linked_list.print_list()

# # Reverse another sublist within the linked list
# print("Reversed entire linked list: ")
# linked_list.reverse_between(0, 4)
# linked_list.print_list()

# # Reverse a sublist of length 1 within the linked list
# print("Reversed sublist of length 1 (3, 3): ")
# linked_list.reverse_between(3, 3)
# linked_list.print_list()

# # Reverse an empty linked list
# print("Reversed empty linked list: ")
# empty_list = LinkedList(0)
# empty_list.make_empty
# empty_list.reverse_between(0, 0)
# empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
