import sys
import os
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '../Stack', '../../AlgorithmsAndDataStructures'))
from stack_linked_list import Stack as StackTail
from stack_linked_list_head import StackHead 
s1=StackHead()
s1.push(1)

if __name__ == "__main__":
    print(s1.pop())

