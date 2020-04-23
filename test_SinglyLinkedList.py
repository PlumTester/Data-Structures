import SinglyLinkedList as ListClass

def test_IsEmptyAndSize():  
    ssl = ListClass.SinglyLinkedList()
    assert ssl.isEmpty() == True
    assert ssl.size() == 0
    assert ssl.toString() == "[]"

    ssl.addFirst(1)
    assert ssl.isEmpty() == False
    assert ssl.size() == 1

    ssl.addFirst(2)
    assert ssl.isEmpty() == False
    assert ssl.size() == 2

    ssl.removeFirst()
    assert ssl.isEmpty() == False
    assert ssl.size() == 1

    ssl.removeFirst()
    assert ssl.isEmpty() == True
    assert ssl.size() == 0


def testFirstAndLast():
    ssl = ListClass.SinglyLinkedList()
    assert ssl.first() == None
    assert ssl.last() == None

    ssl.addFirst(1)
    assert ssl.first() == 1
    assert ssl.last() == 1

    ssl.addFirst(2)
    assert ssl.first() == 2
    assert ssl.last() == 1
    
    ssl.removeLast()
    assert ssl.first() == 2
    assert ssl.last() == 2
    
    ssl.removeFirst()
    assert ssl.first() == None
    assert ssl.last() == None
    

def testAddFirst():
    ssl = ListClass.SinglyLinkedList()
    ssl.addFirst(1)
    assert ssl.toString() == "[1]"

    ssl.addFirst(2)
    assert ssl.toString() == "[2, 1]"

    ssl.addFirst(9)
    ssl.removeFirst()

    ssl.addFirst(8)
    ssl.addFirst(7)
    ssl.addFirst(6)
    ssl.addFirst(5)
    ssl.addFirst(4)
    ssl.addFirst(3)

    assert ssl.toString() == "[3, 4, 5, 6, 7, 8, 2, 1]"
    

def testAddLast():
    ssl = ListClass.SinglyLinkedList()
    ssl.addLast(1)
    assert ssl.toString() == "[1]"

    ssl.addLast(2)
    assert ssl.toString() == "[1, 2]"

    ssl.addLast(9)
    ssl.removeFirst()
    assert ssl.toString() == "[2, 9]"

    ssl.addLast(8)
    ssl.addLast(7)
    ssl.addLast(6)
    ssl.addLast(5)
    ssl.addLast(4)
    ssl.addLast(3)
    
    assert ssl.toString() == "[2, 9, 8, 7, 6, 5, 4, 3]"

def testRemoveFirst():
    ssl = ListClass.SinglyLinkedList()

    for i in range(0, 10):
        ssl.addLast(i)
    
    assert ssl.toString() == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

    ssl.removeFirst()
    assert ssl.toString() == "[1, 2, 3, 4, 5, 6, 7, 8, 9]"

    for i in range(0, 7):
        ssl.removeFirst()

    assert ssl.toString() == "[8, 9]"

    ssl.removeFirst()
    assert ssl.toString() == "[9]"

    ssl.removeFirst()
    assert ssl.toString() == "[]"
    

def testRemoveLast():
    ssl = ListClass.SinglyLinkedList()

    for i in range(0, 10):
        ssl.addLast(i)
    
    assert ssl.toString() == "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
    
    ssl.removeLast()
    assert ssl.toString() == "[0, 1, 2, 3, 4, 5, 6, 7, 8]"
    
    for i in range(0, 7):
        ssl.removeLast()
    
    assert ssl.toString() == "[0, 1]"
    
    ssl.removeLast()
    assert ssl.toString() == "[0]"
    
    ssl.removeLast()
    assert ssl.toString() == "[]"
    