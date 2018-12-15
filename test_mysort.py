import unittest

from mysort import my_sort

class Test(unittest.TestCase):
    def setUp(self):
        self.result1 = my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.result2 = my_sort([1, 2])
        self.result3 = my_sort([2, 1])
        self.result4 = my_sort([3, 3, 4])
        self.result5 = my_sort([90, 45, 66])
        self.result6 = my_sort([90, 77, 66, 55, 44, 289848, 4983484, 13873, 18827, 13232])
        self.result7 = my_sort([27842, 3234, 245325, 3554, 24525, 224325, 111])
        self.result8 = my_sort([11111, 1, 11, 979749, 1111, 1111])

    def test_output(self):
        self.assertEqual(self.result1,  [1, 3, 5, 7, 9, 2, 4, 6, 8, 10], msg='Invalid sorted output')
        self.assertEqual(self.result2,  [1, 2], msg='Invalid sorted output')
        self.assertEqual(self.result3,  [1, 2], msg='Invalid sorted output')
        self.assertEqual(self.result4,  [3, 3, 4], msg='Invalid sorted output')
        self.assertEqual(self.result5,  [45, 66, 90], msg='Invalid sorted output')

    def test_output_hidden(self):
        self.assertEqual(self.result6,  [55, 77, 13873, 18827, 44, 66, 90, 13232, 289848, 4983484], msg='Invalid sorted output')
        self.assertEqual(self.result7,  [111, 24525, 224325, 245325, 3234, 3554, 27842], msg='Invalid sorted output')
        self.assertEqual(self.result8,  [1, 11, 1111, 1111, 11111, 979749], msg='Invalid sorted output')