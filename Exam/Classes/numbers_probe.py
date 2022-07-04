"""
Exam task 1.1 Number Unittests
"""
import unittest
from numbers import First, Second


class TestNumbers(unittest.TestCase):
    """
    Main class to test numbers module
    """

    def test_constructior(self):
        """
        Test basic methods:
            __init__
            __str__
        """
        alpha1 = First(1, 5, 3, 4, 2, 3)  # First's constructor takes variable of arguments
        self.assertEqual(alpha1.evens, [2, 4])   # evens are in sorted order
        self.assertEqual(alpha1.odds, [1, 5, 3, 3])  # odds are in	the original order
        self.assertEqual(str(First(4, 3, 2, 5)) , 'First(evens=[2, 4], odds=[3, 5])') # use __class__ and __name__ attribute

    def test_equal(self):
        """
        Check equal operator: __eq__
        """
        # Two	First's object are equal if their evens are equal.
        self.assertEqual(First(4, 3, 2, 5) , First(2, 3, 4))
        self.assertNotEqual(First(4, 3, 2, 5),  First(3, 4, 5))
        self.assertNotEqual(First(4, 3, 2, 5), "Correct handling this situation")

        s = []
        self.assertNotIn(First(1, 2), s)
        s.append(First(1, 2))
        self.assertIn(First(1, 2), s)
        self.assertIn(First(1, 2, 3), s)
        beta1 = Second(3, 7)  # creates an	First with values [3,4,5,6,7]
        self.assertTrue(isinstance(beta1, First))
        self.assertEqual(str(beta1) , 'First(evens=[4, 6], odds=[3, 5, 7])') # use __class__, __bases__, __name__ attribute


    def test_delete(self):
        """
        Test delete methods:
                del_odds
                deleted_odds
        """
        # del_odds and deleted_odds are different methods (one is destructive)
        alpha2 = First(4, 3, 2, 5)
        alpha2.del_odds()
        self.assertEqual(str(alpha2) , 'First(evens=[2, 4], odds=[])')
        alpha3 = First(4, 3, 2, 5)
        alpha4 = alpha3.deleted_odds() # use __class__ attribute
        self.assertTrue(isinstance(alpha4, First))
        self.assertEqual(str(alpha3) , 'First(evens=[2, 4], odds=[3, 5])')
        self.assertEqual(str(alpha4) , 'First(evens=[2, 4], odds=[])')


    def test_transform(self):
        """
        Check Second class, and transform method
        """
        # only	Second's object can call transform:
        beta1 = Second(3, 7)
        beta2 = beta1.transform(2)                # so instead of (3,7) it's now (3+2,7+2)
        self.assertEqual(str(beta2) , 'First(evens=[6, 8], odds=[5, 7, 9])')
        self.assertEqual(type(beta2) , Second)
        crashed = False
        try:
            alpha = First(1, 2).transform()
        except:
            crashed = True
        self.assertTrue(crashed)


if __name__  ==  '__main__':
    unittest.main()
