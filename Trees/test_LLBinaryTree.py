import LLBinaryTree

def preparePerfectTree():
    
    tree = LLBinaryTree.Tree()
    tree.setRoot(LLBinaryTree.Position(1))
    tree.getRoot().setLeft(LLBinaryTree.Position(2))
    tree.getRoot().setRight(LLBinaryTree.Position(3))

    tree.getRoot().getLeft().setLeft(LLBinaryTree.Position(4))
    tree.getRoot().getLeft().setRight(LLBinaryTree.Position(5))
    tree.getRoot().getRight().setLeft(LLBinaryTree.Position(6))
    tree.getRoot().getRight().setRight(LLBinaryTree.Position(7))

    return tree

def prepareEmptyTree():
    tree = LLBinaryTree.Tree()
    return tree     

def prepareRootTree():
    tree = LLBinaryTree.Tree()
    tree.setRoot(LLBinaryTree.Position("root"))
    return tree

def prepareOnlyLeftTree():
    tree = LLBinaryTree.Tree()

    tree.setRoot(LLBinaryTree.Position(1))
    tree.getRoot().setLeft(LLBinaryTree.Position(2))
    tree.getRoot().getLeft().setLeft(LLBinaryTree.Position(3))
    tree.getRoot().getLeft().getLeft().setLeft(LLBinaryTree.Position(4))
    tree.getRoot().getLeft().getLeft().setRight(LLBinaryTree.Position(5))
    tree.getRoot().getLeft().getLeft().getLeft().setLeft(LLBinaryTree.Position(6))

    return tree

def prepareOnlyRightTree():
    tree = LLBinaryTree.Tree()
    
    tree.setRoot(LLBinaryTree.Position(1))
    tree.getRoot().setRight(LLBinaryTree.Position(2))
    tree.getRoot().getRight().setRight(LLBinaryTree.Position(3))
    tree.getRoot().getRight().getRight().setRight(LLBinaryTree.Position(5))
    tree.getRoot().getRight().getRight().setLeft(LLBinaryTree.Position(4))
    tree.getRoot().getRight().getRight().getLeft().setRight(LLBinaryTree.Position(6))
    tree.getRoot().getRight().getRight().getRight().setRight(LLBinaryTree.Position(7))

    return tree


def prepareMixTree():
    tree = LLBinaryTree.Tree()

    tree.setRoot(LLBinaryTree.Position(1))
    
    # LHS
    tree.getRoot().setLeft(LLBinaryTree.Position(2))
    tree.getRoot().getLeft().setLeft(LLBinaryTree.Position(4))
    tree.getRoot().getLeft().getLeft().setLeft(LLBinaryTree.Position(6))
    tree.getRoot().getLeft().getLeft().setRight(LLBinaryTree.Position(7))
    
    # RHS
    tree.getRoot().setRight(LLBinaryTree.Position(3))
    tree.getRoot().getRight().setLeft(LLBinaryTree.Position(5))
    tree.getRoot().getRight().getLeft().setRight(LLBinaryTree.Position(8))

    return tree


def test_sizeIsEmpty():
    
    treeBase = prepareEmptyTree()

    assert treeBase.isEmpty() == True
    assert treeBase.size() == 0

    treeBase.setRoot(LLBinaryTree.Position(1))
    
    assert treeBase.isEmpty() == False
    assert treeBase.size() == 1

    treeBase.setRoot(None)

    assert treeBase.isEmpty() == True
    assert treeBase.size() == 0

    treeBase = prepareRootTree()

    assert treeBase.isEmpty() == False
    assert treeBase.size() == 1

    treePerf = preparePerfectTree()

    assert treePerf.isEmpty() == False
    assert treePerf.size() == 7

    treeOnlyLeft = prepareOnlyLeftTree()

    assert treeOnlyLeft.isEmpty() == False
    assert treeOnlyLeft.size() == 6

    treeOnlyRight = prepareOnlyRightTree()

    assert treeOnlyRight.isEmpty() == False
    assert treeOnlyRight.size() == 7

    treeMix = prepareMixTree()

    assert treeMix.isEmpty() == False
    assert treeMix.size() == 8

def test_PreorderTraversal():
    treeEmpty = prepareEmptyTree()
    assert treeEmpty.toString(treeEmpty.preorderTraversal()) == "*---*\n" \
                                                    +   "-^^^-"

    treeRoot = prepareRootTree()
    assert treeRoot.toString(treeRoot.preorderTraversal())  == "*---*\n" \
                                                    +   "e: root, p: None, l: None, r: None\n" \
                                                    +   "-^^^-"

    treePerfect = preparePerfectTree()
    assert treePerfect.toString(treePerfect.preorderTraversal()) == "*---*\n" \
                                                    +   "e: 1, p: None, l: 2, r: 3\n" \
                                                    +   "e: 2, p: 1, l: 4, r: 5\n" \
                                                    +   "e: 4, p: 2, l: None, r: None\n" \
                                                    +   "e: 5, p: 2, l: None, r: None\n" \
                                                    +   "e: 3, p: 1, l: 6, r: 7\n" \
                                                    +   "e: 6, p: 3, l: None, r: None\n" \
                                                    +   "e: 7, p: 3, l: None, r: None\n" \
                                                    +   "-^^^-"

    treeOnlyLeft = prepareOnlyLeftTree()
    assert treeOnlyLeft.toString(treeOnlyLeft.preorderTraversal()) == "*---*\n" \
                                                    +   "e: 1, p: None, l: 2, r: None\n" \
                                                    +   "e: 2, p: 1, l: 3, r: None\n" \
                                                    +   "e: 3, p: 2, l: 4, r: 5\n" \
                                                    +   "e: 4, p: 3, l: 6, r: None\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 5, p: 3, l: None, r: None\n" \
                                                    +   "-^^^-"

    treeOnlyRight = prepareOnlyRightTree()
    assert treeOnlyRight.toString(treeOnlyRight.preorderTraversal()) == "*---*\n" \
                                                    +   "e: 1, p: None, l: None, r: 2\n" \
                                                    +   "e: 2, p: 1, l: None, r: 3\n" \
                                                    +   "e: 3, p: 2, l: 4, r: 5\n" \
                                                    +   "e: 4, p: 3, l: None, r: 6\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 5, p: 3, l: None, r: 7\n" \
                                                    +   "e: 7, p: 5, l: None, r: None\n" \
                                                    +   "-^^^-"

    treeMix = prepareMixTree()
    assert treeMix.toString(treeMix.preorderTraversal()) == "*---*\n" \
                                                    +   "e: 1, p: None, l: 2, r: 3\n" \
                                                    +   "e: 2, p: 1, l: 4, r: None\n" \
                                                    +   "e: 4, p: 2, l: 6, r: 7\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 7, p: 4, l: None, r: None\n" \
                                                    +   "e: 3, p: 1, l: 5, r: None\n" \
                                                    +   "e: 5, p: 3, l: None, r: 8\n" \
                                                    +   "e: 8, p: 5, l: None, r: None\n" \
                                                    +   "-^^^-"

def test_postorderTraversal():
    treeEmpty = prepareEmptyTree()
    assert treeEmpty.toString(treeEmpty.postorderTraversal()) == "*---*\n" \
                                                    +   "-^^^-"

    treeRoot = prepareRootTree()
    assert treeRoot.toString(treeRoot.postorderTraversal())  == "*---*\n" \
                                                    +   "e: root, p: None, l: None, r: None\n" \
                                                    +   "-^^^-"

    treePerfect = preparePerfectTree()
    assert treePerfect.toString(treePerfect.postorderTraversal()) == "*---*\n" \
                                                    +   "e: 4, p: 2, l: None, r: None\n" \
                                                    +   "e: 5, p: 2, l: None, r: None\n" \
                                                    +   "e: 2, p: 1, l: 4, r: 5\n" \
                                                    +   "e: 6, p: 3, l: None, r: None\n" \
                                                    +   "e: 7, p: 3, l: None, r: None\n" \
                                                    +   "e: 3, p: 1, l: 6, r: 7\n" \
                                                    +   "e: 1, p: None, l: 2, r: 3\n" \
                                                    +   "-^^^-"

    treeOnlyLeft = prepareOnlyLeftTree()
    assert treeOnlyLeft.toString(treeOnlyLeft.postorderTraversal()) == "*---*\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 4, p: 3, l: 6, r: None\n" \
                                                    +   "e: 5, p: 3, l: None, r: None\n" \
                                                    +   "e: 3, p: 2, l: 4, r: 5\n" \
                                                    +   "e: 2, p: 1, l: 3, r: None\n" \
                                                    +   "e: 1, p: None, l: 2, r: None\n" \
                                                    +   "-^^^-"

    treeOnlyRight = prepareOnlyRightTree()
    assert treeOnlyRight.toString(treeOnlyRight.postorderTraversal()) == "*---*\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 4, p: 3, l: None, r: 6\n" \
                                                    +   "e: 7, p: 5, l: None, r: None\n" \
                                                    +   "e: 5, p: 3, l: None, r: 7\n" \
                                                    +   "e: 3, p: 2, l: 4, r: 5\n" \
                                                    +   "e: 2, p: 1, l: None, r: 3\n" \
                                                    +   "e: 1, p: None, l: None, r: 2\n" \
                                                    +   "-^^^-"

    treeMix = prepareMixTree()
    assert treeMix.toString(treeMix.postorderTraversal()) == "*---*\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 7, p: 4, l: None, r: None\n" \
                                                    +   "e: 4, p: 2, l: 6, r: 7\n" \
                                                    +   "e: 2, p: 1, l: 4, r: None\n" \
                                                    +   "e: 8, p: 5, l: None, r: None\n" \
                                                    +   "e: 5, p: 3, l: None, r: 8\n" \
                                                    +   "e: 3, p: 1, l: 5, r: None\n" \
                                                    +   "e: 1, p: None, l: 2, r: 3\n" \
                                                    +   "-^^^-"

def test_inorderTraversal():
    treeEmpty = prepareEmptyTree()
    assert treeEmpty.toString(treeEmpty.inorderTraversal()) == "*---*\n" \
                                                    +   "-^^^-"

    treeRoot = prepareRootTree()
    assert treeRoot.toString(treeRoot.inorderTraversal())  == "*---*\n" \
                                                    +   "e: root, p: None, l: None, r: None\n" \
                                                    +   "-^^^-"

    treePerfect = preparePerfectTree()
    assert treePerfect.toString(treePerfect.inorderTraversal()) == "*---*\n" \
                                                    +   "e: 4, p: 2, l: None, r: None\n" \
                                                    +   "e: 2, p: 1, l: 4, r: 5\n" \
                                                    +   "e: 5, p: 2, l: None, r: None\n" \
                                                    +   "e: 1, p: None, l: 2, r: 3\n" \
                                                    +   "e: 6, p: 3, l: None, r: None\n" \
                                                    +   "e: 3, p: 1, l: 6, r: 7\n" \
                                                    +   "e: 7, p: 3, l: None, r: None\n" \
                                                    +   "-^^^-"

    treeOnlyLeft = prepareOnlyLeftTree()
    assert treeOnlyLeft.toString(treeOnlyLeft.inorderTraversal()) == "*---*\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 4, p: 3, l: 6, r: None\n" \
                                                    +   "e: 3, p: 2, l: 4, r: 5\n" \
                                                    +   "e: 5, p: 3, l: None, r: None\n" \
                                                    +   "e: 2, p: 1, l: 3, r: None\n" \
                                                    +   "e: 1, p: None, l: 2, r: None\n" \
                                                    +   "-^^^-"

    treeOnlyRight = prepareOnlyRightTree()
    assert treeOnlyRight.toString(treeOnlyRight.inorderTraversal()) == "*---*\n" \
                                                    +   "e: 1, p: None, l: None, r: 2\n" \
                                                    +   "e: 2, p: 1, l: None, r: 3\n" \
                                                    +   "e: 4, p: 3, l: None, r: 6\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 3, p: 2, l: 4, r: 5\n" \
                                                    +   "e: 5, p: 3, l: None, r: 7\n" \
                                                    +   "e: 7, p: 5, l: None, r: None\n" \
                                                    +   "-^^^-"

    treeMix = prepareMixTree()
    assert treeMix.toString(treeMix.inorderTraversal()) == "*---*\n" \
                                                    +   "e: 6, p: 4, l: None, r: None\n" \
                                                    +   "e: 4, p: 2, l: 6, r: 7\n" \
                                                    +   "e: 7, p: 4, l: None, r: None\n" \
                                                    +   "e: 2, p: 1, l: 4, r: None\n" \
                                                    +   "e: 1, p: None, l: 2, r: 3\n" \
                                                    +   "e: 5, p: 3, l: None, r: 8\n" \
                                                    +   "e: 8, p: 5, l: None, r: None\n" \
                                                    +   "e: 3, p: 1, l: 5, r: None\n" \
                                                    +   "-^^^-"



if __name__ == "__main__":

    tree = prepareOnlyRightTree()

    print(tree.toString(tree.preorderTraversal()))
        
