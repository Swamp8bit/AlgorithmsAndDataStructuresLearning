import ctypes

class DynArray:
    _MIN_CAPACITY=16
    def __init__(self):
        self.count = 0
        self.capacity = self._MIN_CAPACITY
        self.array=self.make_capacity(self.capacity)
    
    def __len__(self):
        return self.count
    
    def make_capacity(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 and i >= self.count:
            raise IndexError("Index is out of bounds")
        return self.array[i]
    
    def resize(self, new_capacity):
        print("It is time for resizing")
        new_array=self.make_capacity(new_capacity)
        for i in range(self.count):
            new_array[i]=self.array[i]
        self.array=new_array
        self.capacity=new_capacity
    
    def append(self,itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count]=itm
        self.count+=1
    
    def insert(self,i, itm):
        if i < 0 and i >= self.count:
            raise IndexError("Index is out of bounds")
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        
        for j in range(self.count,i,-1):
            self.array[j]=self.array[j-1]            
        self.array[i]=itm
        self.count+=1
    
    def shrink(self):
        threshold=self.capacity/2
        shrink_to=int(self.capacity/1.5)
        if self.count < threshold:            
            if shrink_to <= self._MIN_CAPACITY:
                self.resize(self._MIN_CAPACITY)
            else:
                self.resize(shrink_to)
    
    def delete(self,i):
        if i < 0 and i >= self.count:
            raise IndexError("Index is out of bounds")
        self.count-=1
        for j in range(i,self.count):
            print(f"j={j} is going to be j+1={j+1}")
            self.array[j]=self.array[j+1]        
        self.shrink()
            

if __name__=="__main__":
    da = DynArray()
    for i in range(20):
        da.append(i)
        print(f"Printing position i={i} da[i]={da[i]} ")
   
    print("=================")
    da.insert(2,-6)
    for i in range(da.count):
         print(f"Printing position i={i} da[i]={da[i]} ")
    print(f"The capacity is {da.capacity}")
    print("=================")
    for i in range(3,10):
        da.delete(i)
    for i in range(da.count):
         print(f"Printing position i={i} da[i]={da[i]} ")
    print(f"The capacity is {da.capacity}")
    
        
        

