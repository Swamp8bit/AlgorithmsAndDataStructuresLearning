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
            item.previous = None
            item.next = None
        else:
            self.tail.next=item
            item.previous=self.tail
        self.tail=item
    
    def find(self, val):  
       
        node=self.head
        while node is not None:
            if val==node.value:
                return node
                
            node=node.next
        return None
        
    
    def find_all(self, val):
        finding=[]
        node=self.head
        while node is not None:
            if node.value == val:
                finding.append(node)
            node=node.next        
        return finding
    
    def len(self):
        node = self.head
        length=0
        while node is not None:
            length+=1
            node = node.next
        return length
    
    def delete(self,val, all=False):
        node=self.head
                 
        while node is not None:
            node_previous=node.previous
            node_next=node.next
            if node.value == val:
                if node_previous is not None:
                    node_previous.next=node_next
                    if node_next is not None:
                        node_next.previous=node_previous
                    else:
                        self.tail=node_previous
                else:
                    self.head=node_next
                    if node_next is not None:
                        node_next.previous=None
                    else:
                        self.tail=node_previous
                if all==False:
                    break               
            
            node=node_next
 
    
    def print_all_nodes(self):
        node=self.head
        while node is not None:
            print(node.value)
            node = node.next

    def clean(self):
        self.head=None
        self.tail=None    

    def insert(self, afterNode, newNode):
        #case in the middle
        if newNode is None:
            return
        if afterNode is not None:
            node = self.head
            while node is not None:

                if afterNode is node:
                    newNode.next=node.next
                    newNode.previous=node
                    node.next=newNode
                    return
            node=node.next
        else:
            if self.head is None and self.tail is None: #case of empty list
                self.head=newNode
                self.tail=newNode
                
            else: # case of add last
                last_tail=self.tail
                self.tail=newNode
                self.tail.previous=last_tail
                last_tail.next=newNode
                newNode.next=None               
                newNode.previous=last_tail                    

    def add_in_head(self, newNode):
        if self.head is None and self.tail is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.head.previous=newNode
            newNode.next=self.head
            self.head=newNode
            newNode.previous=None