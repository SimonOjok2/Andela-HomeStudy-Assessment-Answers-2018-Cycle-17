import unittest

from digitalization import digitize

class Test(unittest.TestCase):
    def test_digitalize(self):
        self.assertEqual(digitize(8675309),[8, 6, 7, 5, 3, 0, 9], msg="The numbers are not equal")