class Node:
    def __init__(self,v):
        self.next=None
        self.value=v
class Queue:
    def __init__(self):
        self.start=None
        self.end=None
    
    def enqueue(self, item): #need to add element to the end of the list
        new_end=Node(item)
        if self.end is not None:
            old_end=self.end        
            self.end=new_end
            old_end.next=new_end
        else:
            self.start=new_end
            self.end=new_end
    
    def dequeue(self): #need to remove element from the beginning of the list
        if self.start is not None:
            item=self.start.value
            self.start=self.start.next
            return item       
        else:            
            return None
            

    def size(self):
        sum=0
        if self.start is not None:        
            node=self.start        
            while node is not None:
                sum+=1
                node=node.next
        return sum

    def is_empty(self):
        if self.size() ==0:
            return True
        else:
            return False
