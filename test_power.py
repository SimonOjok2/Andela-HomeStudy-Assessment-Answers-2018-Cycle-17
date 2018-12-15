import unittest

from power import power

class Test(unittest.TestCase):
    def test_returns_correct_power(self):
        base, exp = 2, 3
        res = power(base, exp)
        self.assertEqual(
            res, 8, msg='Expected {}, got {}'.format(8, res))

    def test_return_1_when_exp_is_0(self):
        base, exp = 4, 0
        res = power(base, exp)
        self.assertEqual(
            res,
            1,
            msg='A number power 0 should be 1'
        )

    def test_return_0_when_base_is_0(self):
        base, exp = 0, 10
        res = power(base, exp)
        self.assertEqual(
            res,
            0,
            msg='O power any number should be 0'
        )

    def test_non_digit_argument(self):
        with self.assertRaises(TypeError) as context:
            base, exp = 'base', 'exp'
            res = power(base, exp)
            self.assertEqual(
                'Argument must be interfer or float',
                context.exception.message,
                'Only digits are allowed as input'
            )

    def test_if_recursive(self):
        # Python 3 will raise RecursionError, Python 2 will raise RuntimeError.
        # Instead of asserting it raises either of those, assert it raises an
        # error and check the message, which is the same across the Py versions.
        with self.assertRaises(Exception) as context:
            power(100000, 5)
            self.assertIn(
                'maximum recursion depth exceeded',
                context.exception.message,
                msg='You must use recursion when implementing replicate_recur.'
            )