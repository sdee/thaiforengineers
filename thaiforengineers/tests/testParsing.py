import unittest
from syllableParser import SyllableParser


class TestParsing(unittest.TestCase):
    def setUp(self):
        self.parser = SyllableParser()


    def test_identify_characters(self):
        self.assertTrue(self.parser.is_vowel(u'\u0e2F'))
        self.assertFalse(self.parser.is_consonant(u'\u0e2F'))
        self.assertTrue(self.parser.is_consonant(u'\u0e01'))
        self.assertFalse(self.parser.is_vowel(u'\u0e01'))


if __name__ == '__main__':
    unittest.main()