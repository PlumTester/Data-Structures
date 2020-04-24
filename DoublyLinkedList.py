
class Node:

    def __init__(self, element):
        print("creating new node with element {0}".format(element))
        self.__element = element
        self.__next = None
        self.__prev = None

    def __del__(self):

        e = self.__element
        n = "None"
        p = "None"

        if self.__next != None:
            n = self.__next.__element
        
        if self.__prev != None:
            p = self.__prev.__element
        
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
        head = Node("head")
        tail = Node("tail")

        self.__head = head
        self.__tail = tail


    def __del__(self):
        print("destroying Doubly Linked List")
        # pass


    def toString(self):

        if self.isEmpty():
            return "[]"
        else:
            
            node = self.__head.getNext()
            output = str(node.getElement()) + "" 

            node = node.getNext()

            while node != self.__tail:
                output += ", " + str(node.getElement())
                node = node.getNext()

            return output


    def size(self):

        count = 0

        if not self.isEmpty():
            
            node = self.__head.getNext()

            while node != self.__tail:
                count += 1
                node = node.getNext()

        return count


    def isEmpty(self):
        if self.__head.getNext() == None and self.__tail.getPrev() == None:
            return True
        elif self.__tail.getPrev() == None:
            print("Prev has reference but head does not!")
            return True
        else:
            return False


    def first(self):
        if not self.isEmpty():
            return self.__head.getNext().getElement()
        else:
            return None


    def last(self):
        if not self.isEmpty():
            return self.__tail.getPrev().getElement()
        else:
            return None

    
    def __findNode(self, element):

        if not self.isEmpty():
            
            node = self.__head.getNext()

            while node != self.__tail:
                if node.getElement() == element:
                    return node

                node = node.getNext()

        return None


    def before(self, element):
        if not self.isEmpty():
            
            nodeRef = self.__findNode(element)

            if nodeRef != None and nodeRef.getPrev() != self.__head:
                return nodeRef.getPrev().getElement()
            
        return None


    def after(self, element):
        if not self.isEmpty():
            
            nodeRef = self.__findNode(element)

            if nodeRef != None and nodeRef.getNext() != self.__tail:
                return nodeRef.getNext().getElement()
            
        return None



    def setElement(self, eRef, element):
        if not self.isEmpty():

            nodeRef = self.__findNode(element)

            if nodeRef != None:
                nodeRef.setElement(element)


    def remove(self, element):
        if not self.isEmpty():

            nodeRef = self.__findNode(element)

            if nodeRef != None:

                if nodeRef.getNext() == self.__tail and nodeRef.getPrev() == self.__head:
                    self.__head.setNext(None)
                    self.__tail.setPrev(None)

                else:
                    nodeRef.getPrev().setNext(nodeRef.getNext())
                    nodeRef.getNext().setPrev(nodeRef.getPrev())
                
                nodeRef.setNext(None)
                nodeRef.setPrev(None)
                del nodeRef


    def addAfter(self, eRef, element):
        if self.isEmpty() and eRef == None:
            node = Node(element)
            
            node.setNext(self.__tail)
            node.setPrev(self.__head)

            self.__head.setNext(node)
            self.__tail.setPrev(node)

        else:
            nodeRef = self.__findNode(eRef)

            if nodeRef != None:
                node = Node(element)

                node.setNext(nodeRef.getNext())
                node.setPrev(nodeRef)

                nodeRef.getNext().setPrev(node)
                nodeRef.setNext(node)


    def addBefore(self, eRef, element):
        if self.isEmpty() and eRef == None:
            node = Node(element)
            
            node.setNext(self.__tail)
            node.setPrev(self.__head)

            self.__head.setNext(node)
            self.__tail.setPrev(node)

        else:
            nodeRef = self.__findNode(eRef)

            if nodeRef != None:
                node = Node(element)

                node.setPrev(nodeRef.getPrev())
                node.setNext(nodeRef)

                nodeRef.getPrev().setNext(node)
                nodeRef.setPrev(node)



