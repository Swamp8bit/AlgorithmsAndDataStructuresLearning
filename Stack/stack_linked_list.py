class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        self.prev=None

class Stack:
    def __init__(self):
        self.start=None
        self.end=None
    
    def size(self):
        node = self.start
        length=0
        while node is not None:
            length+=1
            node = node.next
        return length  
    
    def is_empty(self):
        if self.size()==0:
            return True
        else:
            return False

    
    def pop(self):
        if self.start is None:
            return None #if the stack is empty
        else:
            if self.start.next is None: #case from one item
                item=self.start
                self.start=None
                self.end=None
            else: 
                item=self.end
                self.end=item.prev
                item.prev.next=None #case from two items                              
            return item.value
            
    def print_stack(self):
        node=self.start
        while node is not None:
            print(node.value)
            node=node.next

    def push(self, value):
        item=Node(value)
        if self.start is None:
            self.start = item         
            item.next = None
            item.prev = None
        else:
            self.end.next=item
            item.prev=self.end          
        self.end=item


    def peek(self):
        if self.start is None:
            return None
        else:
            return self.end.value

if "__main__"==__name__:
    test_stack=Stack()
    print (test_stack.size())
    print (test_stack.is_empty())
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(-100)
    assert(test_stack.end.prev.value, 3)
    #print(test_stack.end.value)
    test_stack.print_stack()
    print(test_stack.pop())
    print("########")
    test_stack.print_stack()
    while test_stack.size() > 0:
        print(test_stack.pop())
        print(test_stack.pop())
    test_stack.print_stack()
    