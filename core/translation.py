# translation.py
# Translation data models for the Morse Translator

# Contains the data structures used to represent completed translations,
# including translation direction, original input, translated output,
# and optional metadata associated with a translation.


# Translation Direction

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TranslationDirection(Enum):
    # Represents the direction in which a translation is performed

    ENGLISH_TO_MORSE = "English → Morse"
    MORSE_TO_ENGLISH = "Morse → English"


# Translation Result

@dataclass
class Translation:
    # Represents the result of a single translation operation
    # Stores the original input, translated output, direction, and timestamp

    original_text: str
    translated_text: str
    direction: TranslationDirection
    timestamp: datetime

    def __post_init__(self) -> None:
        # Validates the basic fields of a Translation object
        # before the object is used elsewhere in the application

        if not isinstance(self.original_text, str):
            raise TypeError("Original text must be a string.")

        if not isinstance(self.translated_text, str):
            raise TypeError("Translated text must be a string.")

        if not isinstance(self.direction, TranslationDirection):
            raise TypeError(
                "Direction must be a TranslationDirection value."
            )

        if not isinstance(self.timestamp, datetime):
            raise TypeError("Timestamp must be a datetime object.")

    def is_english_to_morse(self) -> bool:
        # Determines whether this translation converts English to Morse Code

        return self.direction == TranslationDirection.ENGLISH_TO_MORSE

    def is_morse_to_english(self) -> bool:
        # Determines whether this translation converts Morse Code to English

        return self.direction == TranslationDirection.MORSE_TO_ENGLISH

    def direction_name(self) -> str:
        # Returns a human-readable name for the translation direction

        return self.direction.value

    def to_dict(self) -> dict[str, str]:
        # Converts the translation into a dictionary
        # This will be useful later for history storage and serialization

        return {
            "original_text": self.original_text,
            "translated_text": self.translated_text,
            "direction": self.direction.value,
            "timestamp": self.timestamp.isoformat(),
        }


# Translation Factory Functions

def create_translation(
    original_text: str,
    translated_text: str,
    direction: TranslationDirection,
) -> Translation:
    # Creates a Translation object using the current date and time

    return Translation(
        original_text=original_text,
        translated_text=translated_text,
        direction=direction,
        timestamp=datetime.now(),
    )


# Public Module Interface

__all__ = [
    "TranslationDirection",
    "Translation",
    "create_translation",
]

