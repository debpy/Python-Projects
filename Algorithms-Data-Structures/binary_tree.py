from node import Node
class BinaryTree:
    def __init__(self, head: Node):
        self.head = head
    #This method adds a node to the Binary Tree
    def add_node(self, new_node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('Node with that Value already exsist!')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
    #The inorder() function invokes _inorder_recursive() for inorder traversal of Binary Tree 
    def inorder(self):
        self._inorder_recursive(self.head)

    #Inorder Binary Tree traversal using _inorder_recursive recursive function
    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    #The preorder() function invokes _preorder_recursive() for preorder traversal of Binary Tree 
    def preorder(self):
        self._preorder_reverse(self.head)

    #Preorder Binary Tree traversal using _preorder_reverse recursive function
    def _preorder_reverse(self, current_node):
        if not current_node:
            return None
        print(current_node)
        self._preorder_reverse(current_node.left)
        self._preorder_reverse(current_node.right)

    #The postorder() function invokes _postorder_recursive() for preorder traversal of Binary Tree 
    def postorder(self):
        self._postorder_reverse(self.head)

    #Postorder Binary Tree traversal using _postorder_reverse recursive function
    def _postorder_reverse(self, current_node):
        if not current_node:
            return None
        self._postorder_reverse(current_node.left)
        self._postorder_reverse(current_node.right)
        print(current_node)

    #This method returns the Node with the value specified 
    def find(self, value: int):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return LookupError(f"A node with the {value} doesnot exist")

    def find_parent(self, value: int) -> Node:
        if self.head and self.head.value == value:
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):
                return current_node 
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self, value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.right and to_delete.left:
            if to_delete == to_delete_parent.left:
                pass
            elif to_delete == to_delete_parent.right:
                pass
            else:
                pass
        elif to_delete.right or to_delete.left:
            #We have one child
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.left or to_delete.right
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.right or to_delete.left
            else:
                self.head = to_delete.right or to_delete.left     
        else:
            #No children
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete.value == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None


    

        
    