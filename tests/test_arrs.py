import unittest
from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get(["shell", 18, True], 0, "test"), "shell")
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1, 5), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -4), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -2, -1), [3])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
