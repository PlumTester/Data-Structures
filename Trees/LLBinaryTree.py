import Dequeue 

class Position:
    
    def __init__(self, element):
        self.__element = element
        self.__parent = None
        self.__left = None
        self.__right = None

    def __del__(self):
        pass

    def getElement(self):
        return self.__element
    
    def setElement(self, element):
        self.__element = element

    def getParent(self):
        return self.__parent

    def setParent(self, p):
        self.__parent = p

    def numChildren(self):
        num = 0

        if self.__left != None:
            num += 1
        
        if self.__right != None:
            num += 1

        return num


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

    def getSibling(self):
        if self.__parent.__right == self:
            return self.__parent.__left
        elif self.__parent.__left == self:
            return self.__parent.__right
        else:
            print("Sibling logic incorrect")


    def isExternal(self):
        if self.__left == None and self.__right == None:
            return True

    def isInternal(self):
        return not self.isExternal()

    def isRoot(self):
        if self.__parent == None:
            return True
        else:
            return False


class Tree:

    def __init__(self):
        self.__root = None

    def __del(self):
        pass

    def toString(self, positions):
        
        positionStr = self.positionStr(positions)
        output = ""

        output += "*---*\n"
        for node in positionStr:
            output += node + "\n"
        
        output += "-^^^-"

        return output
        

    def size(self):
        return len(self.positions())


    def isEmpty(self):
        if self.__root == None:
            return True
        else:
            return False


    def getRoot(self):
        if not self.isEmpty():
            return self.__root


    def setRoot(self, root):
        if root == None:
            self.__root = root

        elif self.__root == None:
            root.setLeft(None)
            root.setRight(None)
            self.__root = root
            
        else:
            root.setRight(self.__root.getRight())
            root.setLeft(self.__root.getLeft())
            self.__root = root


    def positionStr(self, positions):

        output = []
        
        for node in positions:

            if node == None:
                continue

            nodeRepr = ""
            nodeRepr += "e: " + str(node.getElement())

            if node.getParent() != None:
                nodeRepr += ", p: " + str(node.getParent().getElement())
            else:
                nodeRepr += ", p: None"

            if node.getLeft() != None:
                nodeRepr += ", l: " + str(node.getLeft().getElement())
            else:
                nodeRepr += ", l: None"

            if node.getRight() != None:
                nodeRepr += ", r: " + str(node.getRight().getElement())
            else:
                nodeRepr += ", r: None"

            output.append(nodeRepr)

        return output


    def positions(self):
        
        positions = []
        stack = Dequeue.Dequeue()
        stack.addLast(self.getRoot()) 

        while not stack.isEmpty():
            node = stack.removeFirst()

            if node == None:
                continue

            positions.append(node)

            stack.addLast(node.getLeft())
            stack.addLast(node.getRight())

        return positions



    def preorderTraversal(self):

        if self.isEmpty():
            return []

        positions = [] 
        stack = Dequeue.Dequeue()
        stack.addLast(self.getRoot())

        while not stack.isEmpty():
            node = stack.removeFirst()

            if node == None:
                continue

            positions.append(node)

            stack.addFirst(node.getRight())
            stack.addFirst(node.getLeft())

        return positions


    def postorderTraversal(self):

        if self.isEmpty():
            return []

        positions = [] 
        stack = Dequeue.Dequeue()
        node = self.getRoot()

        while(1):

            while node != None:
                if node.getRight() != None:
                    stack.addFirst(node.getRight())
                
                stack.addFirst(node)
                node = node.getLeft()

            node = stack.removeFirst()

            if node.getRight() != None and stack.getFirst() == node.getRight():
                child = stack.removeFirst()
                stack.addFirst(node)
                node = child
            else:
                positions.append(node)
                node = None

            if stack.isEmpty():
                break

        return positions


    def inorderTraversal(self):
        
        if self.isEmpty():
            return []

        positions = [] 
        stack = Dequeue.Dequeue()
        node = self.getRoot()

        while(1):

            while node != None:
                stack.addFirst(node)
                node = node.getLeft()

            # node = stack.removeFirst()

            if node == None and not stack.isEmpty():
                node = stack.removeFirst()
                positions.append(node)
                node = node.getRight()

            elif node == None and stack.isEmpty():
                break

        return positions