"""
Exam task 2 Binary tree Test
"""
import unittest
from binary_tree import BinatyTree

class TestBinaryTree(unittest.TestCase):

    def test_creation(self):
        """
        Test tree creation
        """
        TestBinaryTree.tree = BinatyTree(1)
        TestBinaryTree.tree.left_child = BinatyTree(2)
        TestBinaryTree.tree.right_child = BinatyTree(8)
        TestBinaryTree.tree.left_child.add_left(4)
        TestBinaryTree.tree.left_child.add_right(5)
        TestBinaryTree.tree.right_child.add_left(6)
        TestBinaryTree.tree.right_child.add_right(7)
        TestBinaryTree.tree.add_right(3)
        # check root, left and right chidren
        tree = TestBinaryTree.tree
        self.assertTrue( isinstance(tree, BinatyTree))
        self.assertEqual(tree.get_root(), 1)
        self.assertEqual(tree.get_left().get_root(), 2)
        self.assertEqual(tree.get_right().get_root(), 3)
        # check other nodes
        self.assertEqual(tree.get_left().get_left().get_left(), None)
        self.assertEqual(tree.get_right().get_right().get_left().get_root(), 6)
        self.assertEqual(tree.get_left().get_right().get_root(), 5)
        self.assertEqual(tree.get_right().get_right().get_root(), 8)
        # check setters
        tree.set_root('changed')
        self.assertEqual(tree.get_root(), 'changed')
        tree.set_root(1)
        self.assertEqual(tree.get_root(), 1)

    def test_inorder(self):
        """
        Test inorder travelsal
        """
        inorder = TestBinaryTree.tree.inorder()
        self.assertEqual(len(inorder), 8)
        self.assertIn(1, inorder)
        self.assertNotIn(0, inorder)
        self.assertIn(6, inorder)
        self.assertNotIn(9, inorder)
        self.assertEqual(inorder, [4, 2, 5, 1, 3, 6, 8, 7])



    def test_right_most(self):
        """
        Test right most method
        """
        rightmosts = TestBinaryTree.tree.right_most()
        self.assertEqual(len(rightmosts), 4)
        self.assertIn(1, rightmosts)
        self.assertNotIn(6, rightmosts)
        self.assertIn(8, rightmosts)
        self.assertNotIn(4, rightmosts)
        self.assertEqual(rightmosts, [1, 3, 8, 7])


    def test_leaf_paths(self):
        """
        Test leaf path method
        """
        leaf_paths = TestBinaryTree.tree.leaf_paths()
        self.assertEqual(len(leaf_paths), 4)
        self.assertEqual(leaf_paths[0][0], 4)
        self.assertIn([4, 2, 1], leaf_paths)
        self.assertNotIn([1, 2, 4], leaf_paths)
        self.assertIn([7, 8, 3,1], leaf_paths)
        self.assertNotIn(1, leaf_paths)
        self.assertEqual(leaf_paths, [[4, 2, 1], [5, 2, 1], [6, 8, 3, 1], [7, 8, 3, 1]])


if __name__ == '__main__':
    unittest.main()
