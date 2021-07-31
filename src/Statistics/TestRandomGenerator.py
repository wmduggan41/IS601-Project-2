import unittest

from RandomGenerator import RandomGenerator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.randomGenerator = RandomGenerator()

    def test_random_generator_instantiate(self):
        self.assertIsInstance(self.randomGenerator, RandomGenerator)

    def test_random_generator_rand_int(self):
        # int must be in range
        start = 1
        end = 7
        rand_int = self.randomGenerator.getRandIntRange(start, end)
        self.assertTrue(rand_int >= start)
        self.assertTrue(rand_int <= end)

    def test_random_generator_rand_int_seed(self):
        # 3 calls to range with same seed should not change result
        start = 1
        end = 7
        seed = 8
        rand_int_1 = self.randomGenerator.getRandIntRangeWithSeed(start, end, seed)
        rand_int_2 = self.randomGenerator.getRandIntRangeWithSeed(start, end, seed)
        rand_int_3 = self.randomGenerator.getRandIntRangeWithSeed(start, end, seed)
        self.assertEqual(rand_int_1, rand_int_2)
        self.assertTrue(rand_int_2, rand_int_3)




if __name__ == '__main__':
    unittest.main()
