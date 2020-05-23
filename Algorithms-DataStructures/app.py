from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add_node(Node(5))
tree.add_node(Node(11))

print("Inorder Traversal: ")
print("--------------")
tree.inorder()
print("\n")
print("Preorder Traversal: ")
print("--------------")
tree.preorder()
print("\n")
print("Postorder Traversal: ")
print("--------------")
tree.postorder()

print(tree.find(11))
print(tree.find(55))
