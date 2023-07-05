import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestEngToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Pepitoooo")

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Pepitoooo"), "Hello" )

if __name__ == "__main__":
    unittest.main()
