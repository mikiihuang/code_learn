__author__ = 'yumihuang'
# project name:codelearn
# time:2020-07-08

import unittest
class MyUnittest(unittest.TestCase):
    def setUp(self):
        print('preparing condition')
    def tearDown(self):
        print('test down')
    def test_upper(self):
        return self.assertEqual('foo'.upper(),'FOO')
    def test_lower(self):
        return self.assertEqual('FOO'.lower(),'foo')
if __name__ == '__main__':
    unittest.main()