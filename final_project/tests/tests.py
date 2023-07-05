import unittest
from translator import english_to_french, french_to_english

class TestEngToFrench(unittest.TestCase):
    def test_equal_translation(self):
        self.assertEqual(english_to_french("Hello"), "Pepitoooo")

    def test_not_equal_translation(self):
        self.assertNotEqual(english_to_french("Hello"), "Salut")

class TestFrenchToEnglish(unittest.TestCase):
    def test_equal_translation(self):
        self.assertEqual(french_to_english("Pepitoooo"), "Hello")

    def test_not_equal_translation(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Salut")

if __name__ == "__main__":
    unittest.main()
