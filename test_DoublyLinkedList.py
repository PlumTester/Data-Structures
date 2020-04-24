import DoublyLinkedList as ListClass

def test_IsEmptyAndSize():  

    dll = ListClass.DoublyLinkedList()

    assert dll.isEmpty() == True
    assert dll.size() == 0
    assert dll.toString() == "[]"

    dll.addBefore(None, 1)
    assert dll.isEmpty() == False
    assert dll.size() == 1

    dll.addBefore(1, 2)
    assert dll.isEmpty() == False
    assert dll.size() == 2

    dll.remove(2)
    assert dll.isEmpty() == False
    assert dll.size() == 1

    dll.remove(1)
    assert dll.isEmpty() == True
    assert dll.size() == 0


def test_FirstAndLast():

    dll = ListClass.DoublyLinkedList()

    dll.toString()

    assert dll.first() == None
    assert dll.last() == None
    assert dll.before(1) == None 
    assert dll.after(1) == None

    dll.addBefore(None, 1)
    dll.addBefore(1, 6)
    dll.addAfter(6, 7)
    dll.addBefore(1, 9)

    assert dll.first() == 6
    assert dll.last() == 1
    assert dll.toString() == "[6, 7, 9, 1]"
    assert dll.before(6) == None
    assert dll.after(6) == 7
    assert dll.after(1) == None
    assert dll.before(1) == 9
    assert dll.before(7) == 6
    assert dll.after(7) == 9

    dll.addBefore(6, 0)
    dll.addAfter(1, 5)

    assert dll.first() == 0
    assert dll.last() == 5
    assert dll.toString() == "[0, 6, 7, 9, 1, 5]"
    assert dll.before(1) == 9
    assert dll.after(1) == 5
    assert dll.after(9) == 1
    assert dll.before(5) == 1
    assert dll.after(5) == None
    assert dll.before(0) == None
    assert dll.after(0) == 6

def test_setElement():

    dll = ListClass.DoublyLinkedList()
    dll.addBefore(None, 10)
    dll.addBefore(10, 9)
    dll.setElement(9, 8)

    assert dll.toString() == "[8, 10]"

def test_remove():

    dll = ListClass.DoublyLinkedList()

    dll.addBefore(None, 1)
    dll.addBefore(1, 6)
    dll.addAfter(6, 7)
    dll.addBefore(1, 9)

    dll.remove(6)

    assert dll.toString() == "[7, 9, 1]"
    
    dll.remove(9)
    dll.remove(1)

    assert dll.toString() == "[7]"

    dll.remove(7)

    assert dll.toString() == "[]"


def test_multipleOperations():

    dll = ListClass.DoublyLinkedList()
    
    dll.addAfter(None, 1)
    dll.addBefore(1, 10)
    dll.addBefore(1, 11)
    dll.remove(1)
    dll.addAfter(11, 12)
    dll.addBefore(10, 9)

    assert dll.toString() == "[9, 10, 11, 12]"
    assert dll.size() == 4

    dll.remove(9)
    dll.remove(10)
    dll.remove(11)
    dll.remove(12)

    assert dll.toString() == "[]"
    assert dll.size() == 0

    dll.addBefore(None, 1)
    dll.addAfter(1, 2)
    
    assert dll.toString() == "[1, 2]"
    assert dll.size() == 2