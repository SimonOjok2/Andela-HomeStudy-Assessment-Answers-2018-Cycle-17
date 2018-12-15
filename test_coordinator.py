import unittest

from coordinator import numbertoordinal

class Test(unittest.TestCase):
    def test_digitalize(self):
        cordn = numbertoordinal(1000)
        self.assertEqual(cordn, "1000th", msg="Invalid")