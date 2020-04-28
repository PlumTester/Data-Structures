import Dequeue

def test_sizeIsEmpty():
    
    dq = Dequeue.Dequeue()

    assert dq.size() == 0
    assert dq.isEmpty() == True
    assert dq.toString() == "[]"

    dq.addLast(1)
    dq.addLast(2)

    assert dq.size() == 2
    assert dq.isEmpty() == False
    assert dq.toString() == "[1, 2]"

    dq.removeFirst()
    dq.removeFirst()

    assert dq.size() == 0
    assert dq.isEmpty() == True
    assert dq.toString() == "[]"

    dq.removeFirst()
    dq.addLast(1)

    assert dq.size() == 1
    assert dq.isEmpty() == False
    assert dq.toString() == "[1]"


def test_getAddRemoveFirst():
    
    dq = Dequeue.Dequeue()

    assert dq.getFirst() == None

    dq.addFirst(3)
    dq.addFirst(2)
    dq.addFirst(1)

    assert dq.getFirst() == 1
    assert dq.toString() == "[1, 2, 3]"
    
    assert dq.removeFirst() == 1
    assert dq.removeFirst() == 2
    
    assert dq.getFirst() == 3
    assert dq.toString() == "[3]"
    assert dq.removeFirst() == 3
    
    assert dq.toString() == "[]"
    assert dq.removeFirst() == None

    dq.addFirst(10)
    assert dq.getFirst() == 10
    assert dq.toString() == "[10]"
    assert dq.removeFirst() == 10


def test_getAddRemoveLast():
    dq = Dequeue.Dequeue()

    assert dq.getLast() == None

    dq.addLast(3)
    dq.addLast(2)
    dq.addLast(1)

    assert dq.getLast() == 1
    assert dq.toString() == "[3, 2, 1]"
    
    assert dq.removeLast() == 1
    assert dq.removeLast() == 2
    
    assert dq.getLast() == 3
    assert dq.toString() == "[3]"
    assert dq.removeLast() == 3
    
    assert dq.toString() == "[]"
    assert dq.removeLast() == None

    dq.addLast(10)
    assert dq.getLast() == 10
    assert dq.toString() == "[10]"
    assert dq.removeLast() == 10 


def test_comboFirstLast():
    dq = Dequeue.Dequeue()
    
    assert dq.getFirst() == None
    assert dq.getLast() == None

    dq.addFirst(1)
    dq.addLast(2)
    dq.addFirst(0)
    dq.addLast(3)
    dq.addLast(4)

    assert dq.toString() == "[0, 1, 2, 3, 4]"
    assert dq.size() == 5
    assert dq.getFirst() == 0
    assert dq.getLast() == 4
    
    assert dq.removeFirst() == 0
    assert dq.removeLast() == 4

    dq.addFirst(9)
    dq.addLast(8)
    assert dq.toString() == "[9, 1, 2, 3, 8]"

    assert dq.removeFirst() == 9
    assert dq.removeLast() == 8
    assert dq.removeLast() == 3
    assert dq.removeLast() == 2
    assert dq.removeFirst() == 1

    assert dq.toString() == "[]"
    assert dq.removeFirst() == None
    assert dq.removeLast() == None
    assert dq.size() == 0

    dq.addLast(12)
    assert dq.toString() == "[12]"
    assert dq.removeFirst() == 12

