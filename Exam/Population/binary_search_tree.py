"""
Exam tsk 3 Population Binary Search Tree
"""


class NodeBST:
    """
    Binary search tree node for population module
    """

    def __init__(self, data, left=None, right=None) -> None:
        """
        Init values with default left and right as None
        """
        self.data = data
        self.left = left
        self.right = right


class BST:
    """
    Class for binary search tree
    """

    def __init__(self, root=None) -> None:
        """
        Init BST root with default as None
        """
        self.root = root


    def add(self, item):
        """
        Add item to the binary search tree
        """
        new_node = NodeBST(item)
        # empty tree
        if self.root is None:
            self.root = new_node
            return

        def recurse(root):
            """ Helper function """
            if root.data > item and root.right is None:
                root.right = new_node
            elif root.data > item:
                recurse(root.right)
            elif root.left is None:
                root.left = new_node
            else:
                recurse(root.left)
        recurse(self.root)


    def more_than(self, flag) -> list:
        """
        Return list with nodes which values are more than flag
        """
        result = []

        def recurse(root):
            """ Helper function find result in subtrees """
            if root is None:
                return
            if root.data <= flag:
                recurse(root.left)
            else:
                result.append(root.data)
                recurse(root.left)
                recurse(root.right)
        recurse(self.root)
        return result
