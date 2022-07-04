"""
Exam task 2 Binary Tree
"""
from collections import deque
from queue import Queue


class BinatyTree:
    """
    Binary tree class with basic functional
    Version with tree as node
    with data, left and right children
    """

    def __init__(self, data) -> None:
        """
        Init root with default left and right as None
        """
        self.data = data
        self.left_child = None
        self.right_child = None

    def get_root(self):
        """
        Return root data
        """
        return self.data

    def set_root(self, value) -> None:
        """
        Set root data as value
        """
        self.data = value

    def add_left(self, item) -> None:
        """ Add the lefy child to the root.
            Left child of the new node is old tree's right child
        """
        new_subtree = BinatyTree(item)
        new_subtree.left_child = self.get_left()
        self.left_child = new_subtree

    def add_right(self, item) -> None:
        """ Add the right child to the root.
            Right child of the new node is old tree's right child
        """
        new_subtree = BinatyTree(item)
        new_subtree.right_child = self.get_right()
        self.right_child = new_subtree

    def get_right(self):
        """
        Return right child of the tree
        """
        return self.right_child

    def get_left(self):
        """
        Return left child of the tree
        """
        return self.left_child

    def is_leaf(self):
        """
        Check if self Node is leaf
        """
        return self.get_left() is None and self.get_right() is None

    def inorder(self) -> list:
        """
        Return list with tree vertices
        data visited in inorder travelsal
        """
        result = []

        def recurse(root):
            """
            Helper function to add nodes
            """
            if root.left_child is not None:
                recurse(root.left_child)
            result.append(root.data)
            if root.right_child is not None:
                recurse(root.right_child)
        recurse(self)
        return result

    def right_most(self) -> list:
        """
        Return list with rightmost nodes for
        each level (starts from the root)
        """
        # Set initial values
        node_queue = Queue()
        node_queue.put(self)
        rightmost = []
        while not node_queue.empty():
            # get number of elements on current level
            num_node_on_level = node_queue.qsize()
            # iterate through items on one level
            for i in range(num_node_on_level):
                current = node_queue.get()
                # it is the most right item
                if i == num_node_on_level - 1:
                    rightmost.append(current.data)
                # add children nodes to the queue
                if current.left_child is not None:
                    node_queue.put(current.left_child)
                if current.right_child is not None:
                    node_queue.put(current.right_child)
        return rightmost

    def leaf_paths(self) -> list:
        """
        Return list with leaf path to the root
        """
        # init starting values
        child_parent_dict = {}
        paths = []
        nodes_stack = deque()
        nodes_stack.append(self)

        while nodes_stack:
            current = nodes_stack.pop()
            # if current is a leaf find its root path
            if current.is_leaf():
                curr_value = current.data
                paths.append([curr_value])
                while curr_value in child_parent_dict:
                    curr_value = child_parent_dict[curr_value]
                    paths[-1].append(curr_value)
            else:
                # Append children nodes to the stack
                # add child-parent pairs to the dictionary.
                if current.right_child is not None:
                    nodes_stack.append(current.get_right())
                    child_parent_dict[current.right_child.data] = current.data
                if current.left_child is not None:
                    nodes_stack.append(current.left_child)
                    child_parent_dict[current.left_child.data] = current.data
        return paths
