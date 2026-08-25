# decoder.py
# Morse-to-English Code decoding utilities for the Morse Translator

# Contains the functions responsible for converting Morse Code into
# English text, including individual Morse character decoding,
# word decoding, complete text decoding, and handling of Morse
# character and word separators.


# Morse Code Dependencies

from .morse_code import (
    get_english_character,
    is_valid_morse_sequence,
)


# Morse Code Separators

MORSE_CHARACTER_SEPARATOR = " "
MORSE_WORD_SEPARATOR = "/"


# Character Decoding

def decode_character(morse_sequence: str) -> str:
    # Returns the English character represented by a Morse sequence
    # The sequence must contain only valid Morse Code symbols

    if not isinstance(morse_sequence, str):
        raise TypeError("Morse sequence must be a string.")

    if not morse_sequence:
        raise ValueError("Morse sequence cannot be empty.")

    if not is_valid_morse_sequence(morse_sequence):
        raise ValueError(
            f"Invalid Morse Code sequence: {morse_sequence!r}"
        )

    return get_english_character(morse_sequence)


# Word Decoding

def decode_word(word: str) -> str:
    # Decodes a single Morse Code word into English
    # Morse characters within a word are separated by spaces

    if not isinstance(word, str):
        raise TypeError("Word must be a string.")

    word = word.strip()

    if not word:
        return ""

    sequences = word.split(MORSE_CHARACTER_SEPARATOR)
    decoded_characters = []

    for sequence in sequences:
        if not sequence:
            continue

        decoded_characters.append(
            decode_character(sequence)
        )

    return "".join(decoded_characters)


# Text Decoding

def decode(text: str) -> str:
    # Converts complete Morse Code text into English
    # Morse character sequences are separated by spaces
    # Morse words are separated using a forward slash

    if not isinstance(text, str):
        raise TypeError("Morse text must be a string.")

    text = text.strip()

    if not text:
        return ""

    normalized_text = " ".join(text.split())

    words = normalized_text.split(MORSE_WORD_SEPARATOR)
    decoded_words = []

    for word in words:
        decoded_word = decode_word(word)

        if decoded_word:
            decoded_words.append(decoded_word)

    return " ".join(decoded_words)


# Decoding Helpers

def decode_characters(sequences: list[str]) -> str:
    # Decodes a sequence of individual Morse Code characters
    # Each item in the list should represent one Morse character

    if not isinstance(sequences, list):
        raise TypeError("Sequences must be provided as a list.")

    decoded_characters = []

    for sequence in sequences:
        decoded_characters.append(
            decode_character(sequence)
        )

    return "".join(decoded_characters)


def decode_words(words: list[str]) -> str:
    # Decodes a sequence of Morse Code words
    # Individual decoded words are separated by spaces

    if not isinstance(words, list):
        raise TypeError("Words must be provided as a list.")

    decoded_words = []

    for word in words:
        decoded_words.append(
            decode_word(word)
        )

    return " ".join(decoded_words)


# Morse Text Normalization

def normalize_morse_input(text: str) -> str:
    # Normalizes Morse Code whitespace while preserving word separators
    # Multiple spaces are reduced to a single character separator

    if not isinstance(text, str):
        raise TypeError("Morse text must be a string.")

    return " ".join(text.strip().split())


# Public Module Interface

__all__ = [
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",
    "decode_character",
    "decode_word",
    "decode",
    "decode_characters",
    "decode_words",
    "normalize_morse_input",
]

