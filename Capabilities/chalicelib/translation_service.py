import boto3


class TranslationService:
    def __init__(self):
        # Creates a boto3 client for Translate
        self.client = boto3.client("translate")

    def translate_text(self, text, source_language="auto", target_language="en"):
        # Calls Translate to translate the text
        response = self.client.translate_text(
            Text=text,
            SourceLanguageCode=source_language,
            TargetLanguageCode=target_language,
        )

        # Returns the translated text along with source and target language info
        translation = {
            "translatedText": response["TranslatedText"],
            "sourceLanguage": response["SourceLanguageCode"],
            "targetLanguage": response["TargetLanguageCode"],
        }

        return translation
