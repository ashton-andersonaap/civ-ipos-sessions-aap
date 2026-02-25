from src.greeter import greet
import unittest

class TestGreeter(unittest.TestCase):
    def test_name_is_string(self):
        self.assertEqual(greet('ashton'), 'Hello, ashton')


if __name__ == '__main__':
    unittest.main()