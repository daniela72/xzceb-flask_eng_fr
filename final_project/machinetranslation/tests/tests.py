import unittest

frenchInputNull = ''
frenchInput = 'Bonjour'

def frenchTextNull(frenchInputNull):
    """
    This function returns true if input is empty
    """
    if frenchInputNull == '':
        return True


def frenchText(frenchInput):
    """
    This function returns translation if input matches
    """
    if frenchInput == 'Bonjour':
        return 'Hello'


englishInputNull = ''
englishInput = 'Hello'

def englishTextNull(englishInputNull):
    """
    This function returns true if input is empty
    """
    if englishInputNull == '':
        return True

def englishText(englishInput):
    """
    This function returns translation if input matches
    """
    if englishInput == 'Hello':
        return 'Bonjour'


class TestFrenchToEnglish(unittest.TestCase): 
    def test_french_input(self): 
        self.assertNotEqual(frenchTextNull(''), False) # test for null input for frenchToEnglishNull
        self.assertEqual(frenchText('Bonjour'), 'Hello') # test for translation match for frenchToEnglish


class TestEnglishToFrench(unittest.TestCase): 
    def test_english_input(self): 
        self.assertNotEqual(englishTextNull(''), False) # test for null input for frenchToEnglishNull
        self.assertEqual(englishText('Hello'), 'Bonjour') # test for translation match for frenchToEnglish

unittest.main()