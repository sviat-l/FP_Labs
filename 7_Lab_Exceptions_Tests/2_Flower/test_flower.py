"""
Lab 7.2 Tests
Test flower classes
"""

import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

class TestFlower(unittest.TestCase):

    def test_flower_init(self):
        """ Check flower class init function and values correctness"""

        fl = Flower('pink', 13, 20)
        self.assertEqual(fl.color, 'red')
        self.assertEqual(fl.petals, 13)
        self.assertEqual(fl.price, 20)

        with self.assertRaises(TypeError):
            Flower([], 1, 31)
        with self.assertRaises(ValueError):
            Flower("red", 14.88, 31)
        with self.assertRaises(ValueError):
            Flower("red", 13, -31)

    def test_subclasses(self):
        """ Tests for subclasses """

        tul = Tulip(10, 30)
        self.assertTrue(issubclass(Tulip, Flower))
        self.assertEqual(tul.color, 'pink')

        rose = Rose(20, 80)
        self.assertTrue(issubclass(Rose, Flower))
        self.assertEqual(rose.color, 'red')

        cham = Chamomile(30, 120)
        self.assertTrue(issubclass(Chamomile, Flower))
        self.assertEqual(cham.color, 'white')

    def test_flower_set(self):
        """ Test flowerSet class """

        flower_set = FlowerSet()
        flower_set.add_flower(Rose(15, 111))
        with self.assertRaises(TypeError):
            flower_set.add_flower(Flower('blue', 10, 50))
        flower_set.add_flower(Rose(14, 199))
        flower_set.add_flower(Rose(13, 200))
        self.assertEqual(len(flower_set.flower_set), 4)


    def test_bucket(self):
        """ Test bucket class methods """

        flowers1 = FlowerSet()
        flowers1.add_flower(Rose(15, 111))
        flowers1.add_flower(Rose(14, 199))
        flowers1.add_flower(Rose(13, 200))

        flowers2 = FlowerSet()
        flowers2.add_flower(Tulip(50, 230))
        flowers2.add_flower(Tulip(120, 400))

        flowers3 = FlowerSet()
        flowers3.add_flower(Flower('black', 100, 10))
        flowers3.add_flower(Flower('blue', 25, 100))
        flowers3.add_flower(Flower('yellow', 25, 200))

        bucket = Bucket()
        bucket.add_set(flowers1)
        bucket.add_set(flowers2)
        bucket.add_set(flowers3)
        self.assertEqual(len(bucket.bucket), 3)
        self.assertEqual(bucket.total_price(), 1450)

if __name__ == "__main__":
    unittest.main()