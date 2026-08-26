# translator.py
# High-level translation interface for the Morse Translator

# Contains the main MorseTranslator class responsible for coordinating
# English-to-Morse and Morse-to-English translation, creating translation
# results, and providing a single interface for the rest of the application.


# Translation Dependencies

from .encoder import (
    encode,
)

from .decoder import (
    decode,
)

from .translation import (
    Translation,
    TranslationDirection,
    create_translation,
)


# Morse Translator

class MorseTranslator:
    # Provides the primary interface for performing Morse Code translations
    # Coordinates the encoder, decoder, and translation result model

    def translate(
        self,
        text: str,
        direction: TranslationDirection,
    ) -> Translation:
        # Translates text according to the requested translation direction
        # Returns a Translation object containing the completed result

        if not isinstance(text, str):
            raise TypeError("Text must be a string.")

        if not isinstance(direction, TranslationDirection):
            raise TypeError(
                "Direction must be a TranslationDirection value."
            )

        if direction == TranslationDirection.ENGLISH_TO_MORSE:
            translated_text = encode(text)

        elif direction == TranslationDirection.MORSE_TO_ENGLISH:
            translated_text = decode(text)

        else:
            raise ValueError(
                f"Unsupported translation direction: {direction}"
            )

        return create_translation(
            original_text=text,
            translated_text=translated_text,
            direction=direction,
        )

    # English-to-Morse Translation

    def to_morse(self, text: str) -> Translation:
        # Translates English text into Morse Code
        # Provides a convenient shortcut for the main translate method

        return self.translate(
            text,
            TranslationDirection.ENGLISH_TO_MORSE,
        )

    # Morse-to-English Translation

    def to_english(self, text: str) -> Translation:
        # Translates Morse Code into English text
        # Provides a convenient shortcut for the main translate method

        return self.translate(
            text,
            TranslationDirection.MORSE_TO_ENGLISH,
        )

    # Translation Direction Helpers

    def translate_to_morse(self, text: str) -> str:
        # Translates English text into Morse Code and returns only the result

        translation = self.to_morse(text)

        return translation.translated_text

    def translate_to_english(self, text: str) -> str:
        # Translates Morse Code into English text and returns only the result

        translation = self.to_english(text)

        return translation.translated_text

    # Direction Inspection

    @staticmethod
    def is_english_to_morse(
        direction: TranslationDirection,
    ) -> bool:
        # Determines whether a direction represents English-to-Morse

        return direction == TranslationDirection.ENGLISH_TO_MORSE

    @staticmethod
    def is_morse_to_english(
        direction: TranslationDirection,
    ) -> bool:
        # Determines whether a direction represents Morse-to-English

        return direction == TranslationDirection.MORSE_TO_ENGLISH


# Convenience Functions

def translate_to_morse(text: str) -> str:
    # Convenience function for directly translating English into Morse Code
    # Creates a translator instance automatically

    translator = MorseTranslator()

    return translator.translate_to_morse(text)


def translate_to_english(text: str) -> str:
    # Convenience function for directly translating Morse Code into English
    # Creates a translator instance automatically

    translator = MorseTranslator()

    return translator.translate_to_english(text)


# Public Module Interface

__all__ = [
    "MorseTranslator",
    "translate_to_morse",
    "translate_to_english",
]

