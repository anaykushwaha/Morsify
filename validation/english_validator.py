# english_validator.py
# English text validation utilities for the Morse Translator

# Contains validation functions for English input, including supported
# character checks, unsupported character detection, letter and number
# detection, punctuation validation, and complete text validation

from typing import Any, List, Optional

from core.morse_code import is_supported_character
from .validator import (
    is_non_empty_string,
    normalize_text,
)


# English Character Validation

def is_english_letter(character: Any) -> bool:
    # Determines whether the supplied value is an English alphabetic character
    #
    # Both uppercase and lowercase letters are supported

    if not isinstance(character, str) or len(character) != 1:
        return False

    return character.isalpha() and character.isascii()


def is_english_digit(character: Any) -> bool:
    # Determines whether the supplied value is an ASCII numerical digit

    if not isinstance(character, str) or len(character) != 1:
        return False

    return character.isdigit() and character.isascii()


def is_supported_punctuation(character: Any) -> bool:
    # Determines whether the supplied character is a supported
    # punctuation character in the Morse Code mapping

    if not isinstance(character, str) or len(character) != 1:
        return False

    if character.isalnum() or character.isspace():
        return False

    return is_supported_character(character)


def is_supported_english_character(character: Any) -> bool:
    # Determines whether a character can be processed by the
    # English-to-Morse translation system
    #
    # Spaces are accepted because they represent word boundaries

    if not isinstance(character, str) or len(character) != 1:
        return False

    if character.isspace():
        return True

    return is_supported_character(character)


# Unsupported Character Detection

def get_unsupported_characters(text: str) -> List[str]:
    # Returns all unique characters that are not supported by the
    # English-to-Morse translation system
    #
    # The original order of first appearance is preserved

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    unsupported: List[str] = []

    for character in text:
        if character.isspace():
            continue

        if not is_supported_character(character):
            if character not in unsupported:
                unsupported.append(character)

    return unsupported


def has_unsupported_characters(text: str) -> bool:
    # Determines whether English text contains any unsupported characters

    if not isinstance(text, str):
        return False

    return bool(get_unsupported_characters(text))


# Text Validation

def is_valid_english_text(
    text: Any,
    allow_empty: bool = False,
) -> bool:
    # Determines whether complete English text can be processed
    # by the Morse Translator
    #
    # Supported letters, numbers, punctuation, and whitespace are accepted

    if not isinstance(text, str):
        return False

    if not allow_empty and not is_non_empty_string(text):
        return False

    return not has_unsupported_characters(text)


def validate_english_text(
    text: Any,
    allow_empty: bool = False,
) -> str:
    # Validates English text and returns the original text
    #
    # Raises ValueError when the text cannot be processed

    if not isinstance(text, str):
        raise ValueError("English text must be a string.")

    if not allow_empty and not is_non_empty_string(text):
        raise ValueError("English text cannot be empty.")

    unsupported = get_unsupported_characters(text)

    if unsupported:
        characters = ", ".join(
            repr(character)
            for character in unsupported
        )

        raise ValueError(
            f"Unsupported character(s): {characters}"
        )

    return text


# Text Normalization

def normalize_english_text(text: str) -> str:
    # Normalizes English text before translation
    #
    # Leading and trailing whitespace is removed and repeated
    # internal whitespace is collapsed into a single space

    if not isinstance(text, str):
        raise ValueError("English text must be a string.")

    return normalize_text(text)


# Character Classification

def get_character_type(character: Any) -> Optional[str]:
    # Returns the general category of a supported English character
    #
    # Possible results:
    # "letter"
    # "digit"
    # "punctuation"
    # "whitespace"
    # None for unsupported values

    if not isinstance(character, str) or len(character) != 1:
        return None

    if character.isspace():
        return "whitespace"

    if is_english_letter(character):
        return "letter"

    if is_english_digit(character):
        return "digit"

    if is_supported_punctuation(character):
        return "punctuation"

    return None


def is_letter_only(text: Any) -> bool:
    # Determines whether the supplied text contains only English letters

    if not isinstance(text, str) or not text:
        return False

    return all(is_english_letter(character) for character in text)


def is_numeric_only(text: Any) -> bool:
    # Determines whether the supplied text contains only ASCII digits

    if not isinstance(text, str) or not text:
        return False

    return all(is_english_digit(character) for character in text)


# Word Validation

def get_words(text: str) -> List[str]:
    # Returns the individual words contained in English text
    #
    # Whitespace is treated as the word separator

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return text.split()


def validate_words(text: str) -> List[str]:
    # Validates every word in a piece of English text
    #
    # Returns the list of words when all characters are supported

    words = get_words(text)

    if not words:
        raise ValueError("Text must contain at least one word.")

    for word in words:
        unsupported = get_unsupported_characters(word)

        if unsupported:
            characters = ", ".join(
                repr(character)
                for character in unsupported
            )

            raise ValueError(
                f"Unsupported character(s) in word "
                f"{word!r}: {characters}"
            )

    return words


# Validation Error Helpers

def get_english_validation_error(
    text: Any,
) -> Optional[str]:
    # Returns a descriptive validation error for English text
    #
    # Returns None when the text is valid

    if not isinstance(text, str):
        return "English text must be a string."

    if not text.strip():
        return "English text cannot be empty."

    unsupported = get_unsupported_characters(text)

    if unsupported:
        characters = ", ".join(
            repr(character)
            for character in unsupported
        )

        return f"Unsupported character(s): {characters}"

    return None


# Validation Summary

def english_text_summary(text: Any) -> dict:
    # Returns a summary of the supplied English text
    #
    # The summary provides useful information for validation,
    # translation, and interface components

    if not isinstance(text, str):
        return {
            "is_valid": False,
            "length": 0,
            "word_count": 0,
            "letter_count": 0,
            "digit_count": 0,
            "punctuation_count": 0,
            "whitespace_count": 0,
            "unsupported_characters": [],
            "error": "English text must be a string.",
        }

    unsupported = get_unsupported_characters(text)

    letter_count = 0
    digit_count = 0
    punctuation_count = 0
    whitespace_count = 0

    for character in text:
        character_type = get_character_type(character)

        if character_type == "letter":
            letter_count += 1
        elif character_type == "digit":
            digit_count += 1
        elif character_type == "punctuation":
            punctuation_count += 1
        elif character_type == "whitespace":
            whitespace_count += 1

    return {
        "is_valid": is_valid_english_text(text),
        "length": len(text),
        "word_count": len(text.split()),
        "letter_count": letter_count,
        "digit_count": digit_count,
        "punctuation_count": punctuation_count,
        "whitespace_count": whitespace_count,
        "unsupported_characters": unsupported,
        "error": get_english_validation_error(text),
    }


# Public Module Interface

__all__ = [
    "is_english_letter",
    "is_english_digit",
    "is_supported_punctuation",
    "is_supported_english_character",
    "get_unsupported_characters",
    "has_unsupported_characters",
    "is_valid_english_text",
    "validate_english_text",
    "normalize_english_text",
    "get_character_type",
    "is_letter_only",
    "is_numeric_only",
    "get_words",
    "validate_words",
    "get_english_validation_error",
    "english_text_summary",
]

