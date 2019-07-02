class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        self.prev=None

class Stack:
    def __init__(self):
        self.start=None
        self.end=None
    
    def get_head(self):
        return self.start
    
    def get_tail(self):
        return self.end
    
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

    