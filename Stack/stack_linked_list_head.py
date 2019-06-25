class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        

class StackHead:
    def __init__(self):
        self.start=None
        
    
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
            item=self.start
            if self.start.next is not None:                
                self.start=self.start.next            
            else:
                self.start=None
            return item.value            

    def push(self, value):
        item=Node(value)
        if self.start is None:
            self.start=item
        else:
            prev_start=self.start
            self.start=item
            item.next=prev_start

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.start.value

    def print_stack(self):
        node=self.start
        while node is not None:
            print(node.value)
            node=node.next

if "__main__"==__name__:
    test_stack=StackHead()
    print (test_stack.size())
    print (test_stack.is_empty())
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push(-100)
    test_stack.print_stack()
    test_stack.pop()
    print("##############")
    test_stack.print_stack()
    while test_stack.size() > 0:
        print(f"I've popped the value of {test_stack.pop()}")
        print(f"I've popped the value of {test_stack.pop()}")
    test_stack.print_stack()
    