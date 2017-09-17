import unittest


def fun(x):
    return x+1;


class MyTest(unittest.TestCase):
    def test_that_add_one(self):
        self.assertEqual(fun(3), 4)


