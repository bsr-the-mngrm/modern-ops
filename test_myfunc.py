import unittest
import myfunc


class TestMyFunc(unittest.TestCase):

    def test_my_func(self):
        self.assertEqual(myfunc.myfunc1(1, 1), 2)