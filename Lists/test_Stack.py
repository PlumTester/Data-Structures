import Stack

def test_isEmptyAndSize():
    
    stack = Stack.Stack()

    assert stack.size() == 0
    assert stack.toString() == "[]"

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.size() == 3
    assert stack.toString() == "[3, 2, 1]"

    stack.pop()
    stack.pop()

    assert stack.size() == 1
    assert stack.toString() == "[1]"

    stack.pop()
    
    assert stack.size() == 0
    assert stack.toString() == "[]"


def test_pushPopCombos():

    stack = Stack.Stack()

    stack.push(5)
    stack.push(4)

    assert stack.top() == 4

    stack.pop()
    stack.push(3)

    assert stack.toString() == "[3, 5]"

    stack.push(1)
    stack.pop()
    
    assert stack.top() == 3
    stack.pop()

    stack.pop()
    stack.pop()

    assert stack.top() == None
