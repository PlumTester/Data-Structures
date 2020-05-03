class Node:

    def __init__(self, element):
        # print("creating {0} Node".format(element))
        self.__element = element
        self.__next = None
        self.__prev = None

    def __del__(self):
        # print("destroying {0} Node".format(self.__element))
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


class Dequeue():

    def __init__(self):
        # print("creating Queue")

        self.__head = Node("head")
        self.__tail = Node("tail")
        
        self.__head.setNext(self.__tail)
        self.__tail.setPrev(self.__head)


    def __del__(self):
        # print("destroying Queue")
        pass

    def isEmpty(self):
        if self.__head.getNext() == self.__tail:
            return True
        else:
            return False 


    def size(self):
        node = self.__head.getNext()
        count = 0

        while node != self.__tail:
            count += 1
            node = node.getNext()

        return count

    def toString(self):

        output = "["

        node = self.__head.getNext()

        while node != self.__tail:
            output += str(node.getElement())

            if node.getNext() != self.__tail:
                output += ", "

            node = node.getNext()
        
        output += "]"

        return output


    def toList(self):
        output = []

        node = self.__head.getNext()

        while node != self.__tail:
            output.append(node.getElement())
            node = node.getNext()
        
        return output


    def getFirst(self):
        if not self.isEmpty():
            return self.__head.getNext().getElement()
        else:
            return None
        
    def getLast(self):
        if not self.isEmpty():
            return self.__tail.getPrev().getElement()
        else:
            return None

    def addFirst(self, element):
        node = Node(element)
        node.setPrev(self.__head)
        node.setNext(self.__head.getNext())

        self.__head.getNext().setPrev(node)
        self.__head.setNext(node)


    def addLast(self, element):
        node = Node(element)
        node.setNext(self.__tail)
        node.setPrev(self.__tail.getPrev())

        self.__tail.getPrev().setNext(node)
        self.__tail.setPrev(node)

    def removeFirst(self):
        if self.__head.getNext() != self.__tail:
            node = self.__head.getNext()

            self.__head.getNext().getNext().setPrev(self.__head)
            self.__head.setNext(self.__head.getNext().getNext())

            result = node.getElement()
            del node

            return result

        else:
            return None

    def removeLast(self):
        if self.__tail.getPrev() != self.__head:
            node = self.__tail.getPrev()

            self.__tail.getPrev().getPrev().setNext(self.__tail)
            self.__tail.setPrev(self.__tail.getPrev().getPrev())

            result = node.getElement()
            del node

            return result
        


