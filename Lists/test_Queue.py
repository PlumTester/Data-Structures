import Queue

def test_sizeAndIsEmpty():
    queue = Queue.Queue()

    assert queue.isEmpty() == True
    assert queue.size() == 0
    assert queue.first() == None
    assert queue.toString() == "[]"

    queue.enqueue(1)
    queue.enqueue(2)

    assert queue.isEmpty() == False
    assert queue.size() == 2
    assert queue.first() == 1
    assert queue.toString() == "[1, 2]"

    queue.dequeue()
    queue.dequeue()

    assert queue.isEmpty() == True
    assert queue.size() == 0
    assert queue.first() == None
    assert queue.toString() == "[]"


def test_firstEnqueueDequeue():
    queue = Queue.Queue()
    
    assert queue.first() == None
    assert queue.toString() == "[]"

    queue.enqueue(1)
    queue.dequeue

    assert queue.first() == 1
    assert queue.toString() == "[1]"

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.first() == 1
    assert queue.toString() == "[1, 1, 2, 3]"

    queue.dequeue()
    queue.enqueue(4)
    queue.dequeue()

    assert queue.first() == 2
    assert queue.toString() == "[2, 3, 4]"

    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == None

    assert queue.first() == None 
    assert queue.toString() == "[]"
    



