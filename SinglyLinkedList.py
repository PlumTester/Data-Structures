class Node:

    def __init__(self, element):
        # print("creating new node with element {0}".format(element))
        self.__element = element
        self.__next = None
    
    def __del__(self):
        if self.__next != None:
            pass
            # print("deleting node with element {0} and next Node {1}".format(str(self.__element), str(self.__next.__element)))
        else:
            pass
            # print("deleting node with element {0} and next Node {1}".format(str(self.__element), str(self.__next)))

    def __str__(self):
        print(self.__element)

    def getElement(self):
        return self.__element

    def setElement(self, e):
        self.__element = e

    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next


class SinglyLinkedList:

    def __init__(self):
        # print("creating new SinglyLinkedList!")
        self.__head = None

    def __del__(self):
        # print("deleting Linked List with contents " + self.toString())
        pass

    def toString(self):
        if self.isEmpty():
            return "[]"
        else:
            node = self.__head
            output = "[" + str(node.getElement())
            while node.getNext() != None:
                node = node.getNext()
                output += ", " + str(node.getElement())

            output += "]"
            return output


    def size(self):
        
        count = 0
        node = self.__head

        while node != None:
            count += 1
            node = node.getNext()
        
        return count


    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False


    def first(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.getElement()


    def last(self):
        
        if self.isEmpty():
            return None
        else:  
            node = self.__head
            
            while node.getNext() != None:
                node = node.getNext()
            
            return node.getElement()


    def addFirst(self, e):
        if self.isEmpty():
            self.__head = Node(e)
        else:
            newNode = Node(e)
            newNode.setNext(self.__head)
            self.__head = newNode            

        pass

    def addLast(self, e):
        if self.isEmpty():
            self.__head = Node(e)
        else:
            lastNode = self.__head

            while lastNode.getNext() != None:
                lastNode = lastNode.getNext()

            newNode = Node(e)
            lastNode.setNext(newNode)

    def removeFirst(self):
        if self.isEmpty():
            return
        else:
            oldHead= self.__head
            self.__head = self.__head.getNext()
            del oldHead
    
    
    def removeLast(self):
        if self.isEmpty():
            return
        else:
            
            lastNode = self.__head
            
            if lastNode.getNext() == None:
                del self.__head
                self.__head = None
                return

            while lastNode.getNext().getNext() != None:
                lastNode = lastNode.getNext()

            secondLast= lastNode
            lastNode = lastNode.getNext()

            secondLast.setNext(None)
            del lastNode


