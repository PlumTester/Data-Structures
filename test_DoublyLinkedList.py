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

    dll.addBefore(None, 1)
    print(dll.toString())

    dll.addBefore(1, 6)
    print(dll.toString())
    
    dll.addAfter(6, 7)
    print(dll.toString())
    
    dll.addBefore(1, 9)
    print(dll.toString())
    
    # assert dll.first() == 1
    # assert dll.last() == 6
    # assert dll.toString() == "[6, 9, 7, 1]"


if __name__ == "__main__":
    test_FirstAndLast()