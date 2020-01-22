from BinarySearch import BST

bst = BST()

bst.insert(12)
bst.insert(15)
bst.insert(4)
bst.traverseInOrder()

bst.remove(12)
print("after removal of 12")
bst.traverseInOrder()