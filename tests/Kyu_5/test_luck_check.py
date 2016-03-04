import unittest

from Kyu_5.luck_check import luck_check


class LuckCheckTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(luck_check('683179'))

    def test_false(self):
        self.assertFalse(luck_check('683000'))


if __name__ == '__main__':
    unittest.main()
