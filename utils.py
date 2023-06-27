import unittest

class TestBasica(unittest.TestCase):

    def test_es_menor_que(self):
        self.assertTrue(3<5)

if __name__=="__main__":
    unittest.main()
