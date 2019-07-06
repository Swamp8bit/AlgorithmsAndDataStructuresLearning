class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class OrderedList:
    def __init__(self, asc):
        self.head=None
        self.tail=None
        self.__ascending=asc

    def compare(selv,v1,v2):
        return 0
        # -1 if v1 < v2
        # 0 if v1 == v2
        # +1 if v1 > v2

    def add(self,value):
        pass
    
    def find(self, val):
        return None #if no such element

    def delete(self, val):
        pass

    def clean(self,asc):
        self.__ascending=asc
        pass
    
    def len(self):
        return 0
    
    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r
