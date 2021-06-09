import unittest
from src import utils


class UtilsTests(unittest.TestCase):
    def test_flatmap(self):
        arr = [[1, 2], [3, 4]]
        flattened = utils.flatmap(arr)
        self.assertSequenceEqual(flattened, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
