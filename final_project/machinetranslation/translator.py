"""
This module demonstrates translation between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French.
    """
    # Here in this Piece of Code
    # English language is being translated to French
    french_text = ""
    translator = MyMemoryTranslator(source='en-GB', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.
    """
    # Here in this Piece of Code
    # French language is being translated to English
    english_text = ""
    translator = MyMemoryTranslator(source='fr-FR', target='en-GB')
    english_text = translator.translate(french_text)
    return english_text
