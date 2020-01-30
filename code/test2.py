import unittest
import script

class TestGame(unittest.TestCase):
    def test_input(self):
        result = script.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = script.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = script.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = script.run_guess(5, '11')
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
