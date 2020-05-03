import LLBinaryTree

def prepareBasicTree():
    
    tree = LLBinaryTree.Tree()
    tree.setRoot(LLBinaryTree.Position(1))
    tree.getRoot().setLeft(LLBinaryTree.Position(2))
    tree.getRoot().setRight(LLBinaryTree.Position(3))

    tree.getRoot().getLeft().setLeft(LLBinaryTree.Position(4))
    tree.getRoot().getLeft().setRight(LLBinaryTree.Position(5))
    tree.getRoot().getRight().setLeft(LLBinaryTree.Position(6))
    tree.getRoot().getRight().setRight(LLBinaryTree.Position(7))

    return tree


def test_sizeIsEmpty():
    
    tree1 = LLBinaryTree.Tree()

    assert tree1.isEmpty() == True
    assert tree1.size() == 0

    tree1.setRoot(LLBinaryTree.Position(1))
    
    assert tree1.isEmpty() == False
    assert tree1.size() == 1

    tree1.setRoot(None)

    assert tree1.isEmpty() == True
    assert tree1.size() == 0

    tree2 = prepareBasicTree()

    assert tree2.isEmpty() == False
    assert tree2.size() == 7



if __name__ == "__main__":

    tree = prepareBasicTree()

    print(tree.toString(tree.inorderTraversal()))
        
