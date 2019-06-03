class Node:
    def __init__(self, v):
        self.value=v
        self.next=None
        self.previous=None

class LinkedList2:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next=item
            item.prev=self.tail
        self.tail=item
    
    def find(self, val):
        if self.head is None:
            finding=None
        else:
            node=self.head
            while node is not None:
                if val==node.value:
                    finding=node    
                node=node.next
        node=self.head
        return finding
    
    def find_all(self, val):
        return []
    
    def delete(self,val,all=False):
        pass
    
    def clean(self):
        pass

    def len(self):
        return 0

    def insert(self, afterNode, newNone):
        pass

    def add_in_head(self, newNode):
        pass