import unittest

from numpy.ma.testutils import assert_equal

from calculator import add2 # Note the absolute import

class TestaddFunction(unittest.TestCase):

    pass
    # Types
    def test_types(self):
        with self.assertRaises(TypeError):
            add2(2,"3")
            add2 ("hello", "world")
            add2 ([2,4,5],["hello","world"])
            add2([],0)
        pass


    # float
    def test_add(self):
        self.assertEqual(add2(1,2),3)
        self.assertEqual(add2(-1,-2),-3, "Negative Integers Fail")
        self.assertEqual(add2(55,67),122)

        self.assertEqual(add2(1.1, 3.6), 4.7, "Float Test Fail")

    # complex
    def test_complex(self):
        self.assertEqual(add2((1 + 2j), 3 - 1j), 4 + 1j, "Complex Test Fail")

    # TODO use case - whats left to tests???
    # string
    # boolean
    # collections other objects
    # null values

        # arrange

            # act - type
    
            # act - type
  
        # assert

if __name__ == "__main__":
    unittest.main()