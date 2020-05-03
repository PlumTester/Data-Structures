import LLBinaryTree

class Node:
    def __init__(self, k, v):
        self.__key = k
        self.__value = v

        self.__parent = None
        self.__left = None
        self.__right = None

    def __del__(self):
        pass

    def getKey(self):
        return self.__key

    def setKey(self, key):
        pass

    def getValue(self):
        return self.__value

    # allows for LLBinaryTree toString function to work
    def getElement(self):
        self.getValue()

    def setValue(self, value):
        self.__value = value

    def getParent(self):
        return self.__parent

    def setParent(self, p):
        self.__parent = p 

    def getLeft(self):
        return self.__left
        
    def setLeft(self, p):
        self.__left = p
        if p != None:
            p.parent = self

    def getRight(self):
        return self.__right

    def setRight(self, p):
        self.__right = p
        if p != None:
            p.parent = self

    # < 0 if self < compNode
    # = 0 if self = compNode
    # > 0 if self > compNode
    def compare(self, compNode):
        if compNode == None:
            print("cannot compare to NoneType")
            return 1
        
        if self.__value > compNode.getValue():
            return 1
        elif self.__value == compNode.getValue():
            return 0
        elif self.__value < compNode.getValue():
            return -1
        else:
            print("invalid comparison")
            return None 


class PriorityQueue:

    def __init__(self):
        self.__heap = LLBinaryTree.Tree()

    def __del__(self):
        pass

    def size(self):
        self.__heap.size()

    def isEmpty(self):
        self.__heap.isEmpty()

    def toString(self):
        return self.__heap.toString(self.__heap.positions())

    def insert(self, key, value):
        pass

    def removeMin(self):
        pass

    def min(self):
        pass
