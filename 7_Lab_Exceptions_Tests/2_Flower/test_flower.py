"""
Lab 7.2 Tests
Test flower classes
"""

import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

class TestFlower(unittest.TestCase):
    """ Test Flower module classes"""

    def test_flower_init(self):
        """ Check flower class init function and values correctness """

        flower = Flower('pink', 13, 20)
        self.assertEqual(flower.color, 'pink')
        self.assertEqual(flower.petals, 13)
        self.assertEqual(flower.price, 20)

        with self.assertRaises(TypeError):
            Flower([], 1, 31)
        with self.assertRaises(TypeError):
            Flower('red', '11', 31)
        with self.assertRaises(TypeError):
            Flower('pink', 10, '1488')
        with self.assertRaises(TypeError):
            Flower("pink", 14.88, 31)
        with self.assertRaises(ValueError):
            Flower("blue", 31, -31)
        with self.assertRaises(ValueError):
            Flower("white", -31, 31)

    def test_subclasses(self):
        """ Tests for subclasses """

        tulip = Tulip(10, 30)
        self.assertTrue(isinstance(tulip, Flower))
        self.assertTrue(issubclass(Tulip, Flower))
        self.assertEqual(tulip.color, 'pink')
        self.assertEqual(tulip.price, 30)

        rose = Rose(20, 80)
        self.assertTrue(issubclass(Rose, Flower))
        self.assertTrue(isinstance(rose, Flower))
        self.assertEqual(rose.color, 'red')
        self.assertEqual(rose.petals, 20)

        chamomile = Chamomile(30, 120)
        self.assertTrue(issubclass(Chamomile, Flower))
        self.assertTrue(isinstance(chamomile, Flower))
        self.assertEqual(chamomile.color, 'white')
        self.assertEqual(chamomile.price, 120)

    def test_flower_set(self):
        """ Test flowerSet class """

        flower_set = FlowerSet()

        self.assertEqual(flower_set.set_type, None)
        flower_set.add_flower(Rose(15, 111))
        self.assertEqual(flower_set.set_type, Rose)
        self.assertNotEqual(flower_set.set_type, Flower)

        with self.assertRaises(TypeError):
            flower_set.add_flower(Flower('blue', 10, 50))

        flower_set.add_flower(Rose(14, 199))
        flower_set.add_flower(Rose(13, 200))
        self.assertEqual(len(flower_set.flower_set), 3)


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
