import unittest
from chalicelib.translation_service import TranslationService


class TranslationServiceTest(unittest.TestCase):
    def setUp(self):
        # Set up the service instance
        self.service = TranslationService()

    def test_translate_text(self):
        # Test the translate_text method with a sample German word
        translation = self.service.translate_text("Einbahnstrabe")

        # Assertions to validate the translation output
        self.assertTrue(translation)  # Check if translation exists
        self.assertEqual(
            "de", translation["sourceLanguage"]
        )  # Check the source language is German
        self.assertEqual(
            "One way street", translation["translatedText"]
        )  # Check if the translation is correct


if __name__ == "__main__":
    unittest.main()
