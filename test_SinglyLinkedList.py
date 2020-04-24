import SinglyLinkedList as ListClass

def test_IsEmptyAndSize():  
    sll = ListClass.SinglyLinkedList()
    assert sll.isEmpty() == True
    assert sll.size() == 0
    assert sll.toString() == "[]"

    sll.addFirst(1)
    assert sll.isEmpty() == False
    assert sll.size() == 1

    sll.addFirst(2)
    assert sll.isEmpty() == False
    assert sll.size() == 2

    sll.removeFirst()
    assert sll.isEmpty() == False
    assert sll.size() == 1

    sll.removeFirst()
    assert sll.isEmpty() == True
    assert sll.size() == 0


def testFirstAndLast():
    sll = ListClass.SinglyLinkedList()
    assert sll.first() == None
    assert sll.last() == None

    sll.addFirst(1)
    assert sll.first() == 1
    assert sll.last() == 1

    sll.addFirst(2)
    assert sll.first() == 2
    assert sll.last() == 1
    
    sll.removeLast()
    assert sll.first() == 2
    assert sll.last() == 2
    
    sll.removeFirst()
    assert sll.first() == None
    assert sll.last() == None
    

def testAddFirst():
    sll = ListClass.SinglyLinkedList()
    sll.addFirst(1)
    assert sll.toString() == "[1]"

    sll.addFirst(2)
    assert sll.toString() == "[2, 1]"

    sll.addFirst(9)
    sll.removeFirst()

    sll.addFirst(8)
    sll.addFirst(7)
    sll.addFirst(6)
    sll.addFirst(5)
    sll.addFirst(4)
    sll.addFirst(3)

    assert sll.toString() == "[3, 4, 5, 6, 7, 8, 2, 1]"
    

def testAddLast():
    sll = ListClass.SinglyLinkedList()
    sll.addLast(1)
    assert sll.toString() == "[1]"

    sll.addLast(2)
    assert sll.toString() == "[1, 2]"

    sll.addLast(9)
    sll.removeFirst()
    assert sll.toString() == "[2, 9]"

    sll.addLast(8)
    sll.addLast(7)
    sll.addLast(6)
    sll.addLast(5)
    sll.addLast(4)
    sll.addLast(3)
    
    assert sll.toString() == "[2, 9, 8, 7, 6, 5, 4, 3]"

def testRemoveFirst():
    sll = ListClass.SinglyLinkedList()

    for i in range(0, 10):
        sll.addLast(i)
    
    assert sll.toString() == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

    sll.removeFirst()
    assert sll.toString() == "[1, 2, 3, 4, 5, 6, 7, 8, 9]"

    for i in range(0, 7):
        sll.removeFirst()

    assert sll.toString() == "[8, 9]"

    sll.removeFirst()
    assert sll.toString() == "[9]"

    sll.removeFirst()
    assert sll.toString() == "[]"
    

def testRemoveLast():
    sll = ListClass.SinglyLinkedList()

    for i in range(0, 10):
        sll.addLast(i)
    
    assert sll.toString() == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
    
    sll.removeLast()
    assert sll.toString() == "[0, 1, 2, 3, 4, 5, 6, 7, 8]"
    
    for i in range(0, 7):
        sll.removeLast()
    
    assert sll.toString() == "[0, 1]"
    
    sll.removeLast()
    assert sll.toString() == "[0]"
    
    sll.removeLast()
    assert sll.toString() == "[]"
    