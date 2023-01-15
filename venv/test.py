import unittest
class TestMy(unittest.TestCase):
    def teardown(self):
        print("down")

    def setup(self):
        print("start")

    def test_a(self):
        x,y=1,1
        self.assertEqual(x,y,"error")
if __name__ == '__main__':
    unittest.main