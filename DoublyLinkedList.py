
class Node:

    def __init__(self, element):
        print("creating new node with element {0}".format(element))
        self.__element = element
        self.__next = None
        self.__prev = None

    def __del__(self):

        e = self.__element
        n = None
        p = None

        if self.__next != None:
            n = self.__next
        
        if self.__prev != None:
            p = self.__prev
        
        print("deleting node with element {0}, next {1}, and prev {2}".format(e, n, p))

    def __str__(self):
        pass

    def getElement(self):
        return self.__element

    def setElement(self, element):
        self.__element = element

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

    def getPrev(self):
        return self.__prev

    def setPrev(self, prev):
        self.__prev = prev

class DoublyLinkedList:

    def __init__(self):
        print("creating Doubly Linked List")
        pass

    def __del__(self):
        pass
        
    def toString(self):
        return "ah ha!"

    def size(self):
        return 2

    def isEmpty(self):
        pass

    def first(self):
        pass

    def last(self):
        pass




