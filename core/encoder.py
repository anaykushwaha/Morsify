# encoder.py
# English-to-Morse Code encoding utilities for the Morse Translator

# Contains the functions responsible for converting English text into
# Morse Code, including individual character encoding, word encoding,
# complete text encoding, and handling of word separators.


# Morse Code Dependencies

from .morse_code import (
    get_morse_code,
    is_supported_character,
)


# Morse Code Separators

MORSE_CHARACTER_SEPARATOR = " "
MORSE_WORD_SEPARATOR = " / "


# Character Encoding

def encode_character(character: str) -> str:
    # Returns the Morse Code representation of a single English character
    # Characters are normalized by the Morse Code lookup system

    if not isinstance(character, str):
        raise TypeError("Character must be a string.")

    if len(character) != 1:
        raise ValueError("Exactly one character must be provided.")

    if character == " ":
        raise ValueError(
            "Spaces must be handled as word separators, not characters."
        )

    if not is_supported_character(character):
        raise ValueError(
            f"Unsupported character: {character!r}"
        )

    return get_morse_code(character)


# Word Encoding

def encode_word(word: str) -> str:
    # Encodes every supported character in a single word
    # Individual Morse characters are separated by spaces

    if not isinstance(word, str):
        raise TypeError("Word must be a string.")

    if not word:
        return ""

    if any(character.isspace() for character in word):
        raise ValueError(
            "encode_word() accepts a single word and cannot contain spaces."
        )

    encoded_characters = [
        encode_character(character)
        for character in word
    ]

    return MORSE_CHARACTER_SEPARATOR.join(encoded_characters)


# Text Encoding

def encode(text: str) -> str:
    # Converts complete English text into Morse Code
    # Characters within words use character separators
    # Individual words use the Morse word separator

    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    if not text:
        return ""

    normalized_text = " ".join(text.split())

    if not normalized_text:
        return ""

    encoded_words = []

    for word in normalized_text.split(" "):
        encoded_word = encode_word(word)
        encoded_words.append(encoded_word)

    return MORSE_WORD_SEPARATOR.join(encoded_words)


# Encoding Helpers

def encode_characters(characters: list[str]) -> str:
    # Encodes a sequence of individual English characters
    # This helper is useful when characters have already been separated

    if not isinstance(characters, list):
        raise TypeError("Characters must be provided as a list.")

    encoded_characters = []

    for character in characters:
        encoded_characters.append(
            encode_character(character)
        )

    return MORSE_CHARACTER_SEPARATOR.join(encoded_characters)


def encode_words(words: list[str]) -> str:
    # Encodes a sequence of words into Morse Code
    # Words are separated using the standard Morse word separator

    if not isinstance(words, list):
        raise TypeError("Words must be provided as a list.")

    encoded_words = []

    for word in words:
        encoded_words.append(
            encode_word(word)
        )

    return MORSE_WORD_SEPARATOR.join(encoded_words)


# Public Module Interface

__all__ = [
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",
    "encode_character",
    "encode_word",
    "encode",
    "encode_characters",
    "encode_words",
] 

