# psedeo Code
"""
class Node:
    __init__:
    data
    next
    prev

class Deque:
    head
    tail
    next

    add_front(item)
        adding node in front
    add_rear(item)
        adding node in rear or last
    remove_rear(item):
        remove node from starting
    remove_front(item):
        remove node from last
    is_empty(node):
        check list is empty or not
        return :True or Flase
    display():
        for displaying list


"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_front(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def add_rear(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove_front(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
            self.length -= 1
            return temp

    def remove_rear(self):
        if self.tail is None:
            return None
        else:
            temp = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            self.length -= 1
            return temp

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self.length
    
    def display(self):
        current=self.head
        if self.head==None:
            print('list Empty')
            return
        while current!=None:
            print(current.data)
            current=current.next




if __name__== '__main__':
    obj=Deque()
    obj.add_front(45)
    obj.add_rear(56)
    # print(obj.display())
    obj.add_front(67)
    obj.remove_front()
    print(obj.display())
    obj.remove_rear()
    print( obj.is_empty())