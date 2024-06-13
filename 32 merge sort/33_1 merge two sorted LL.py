class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def _merge(self, list1, list2):
        combined = LinkedList(0)
        i, j = 0, 0

        head1 = list1
        head2 = list2.head
        while i < self.length and j < list2.length:
            if head1.value < head2.value:
                combined.append(head1.value)
                head1 = head1.next
                i += 1
            else:
                combined.append(head2.value)
                head2 = head2.next
                j += 1

        while i < self.length:
            combined.append(head1.value)
            head1 = head1.next
            i += 1

        while j < list2.length:
            combined.append(head2.value)
            head2 = head2.next
            j += 1

        self.head = combined.head.next
        return combined
    
    def merge(self, list2):
        self._merge(self.head, list2)

l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

# aux = merge(l1, l2)
# aux.print_list()

l1.merge(l2)
l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""