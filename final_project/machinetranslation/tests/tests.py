""" test """
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(), 'Bonjour')
        self.assertIsNotNone(english_to_french())

class TestFrenchToEnglish(unittest.TestCase):    
    def test1(self):
        self.assertEqual(french_to_english(), 'Hello')
        self.assertIsNotNone(french_to_english())
        
if __name__ == '__main__':
    unittest.main()