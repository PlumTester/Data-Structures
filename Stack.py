import SinglyLinkedList as sll

class Stack():

    def __init__(self):
        self.__sll = sll.SinglyLinkedList()
    
    def __del__(self):
        pass

    def isEmpty(self):
        return self.__sll.isEmpty()

    def toString(self):
        return self.__sll.toString()

    def size(self):
        return self.__sll.size()

    def push(self, element):
        return self.__sll.addFirst(element)

    def pop(self):
        return self.__sll.removeFirst()

    def top(self):
        return self.__sll.first()