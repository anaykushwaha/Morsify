# morse_validator.py
# Morse Code validation utilities for the Morse Translator

# Contains validation functions for Morse Code input, including
# character-sequence validation, word validation, separator handling,
# unsupported sequence detection, normalization, and complete Morse
# text validation

from typing import Any, List, Optional, Tuple

from core.morse_code import is_valid_morse_sequence
from .validator import (
    is_non_empty_string,
    normalize_whitespace,
)


# Morse Code Separators

MORSE_CHARACTER_SEPARATOR = " "
MORSE_WORD_SEPARATOR = "/"

VALID_MORSE_SYMBOLS = frozenset({".", "-"})

# Morse Code Validation

def is_morse_symbol(symbol: Any) -> bool:
    # Determines whether the supplied value is a valid Morse Code symbol
    #
    # Valid Morse Code symbols are:
    # "." for a dot
    # "-" for a dash

    if not isinstance(symbol, str):
        return False

    return symbol in VALID_MORSE_SYMBOLS


def is_morse_sequence(sequence: Any) -> bool:
    # Determines whether the supplied value contains only Morse Code
    # dots and dashes
    #
    # This function checks the structure of a sequence but does not
    # require the sequence to represent a known Morse Code character

    if not isinstance(sequence, str):
        return False

    if not sequence:
        return False

    return all(
        symbol in VALID_MORSE_SYMBOLS
        for symbol in sequence
    )


def is_valid_character_sequence(sequence: Any) -> bool:
    # Determines whether a Morse Code sequence represents a supported
    # Morse Code character

    if not is_morse_sequence(sequence):
        return False

    return is_valid_morse_sequence(sequence)


# Morse Word Validation

def split_morse_word(word: str) -> List[str]:
    # Splits a Morse Code word into individual character sequences
    #
    # Each Morse character is separated by whitespace

    if not isinstance(word, str):
        raise ValueError("Morse word must be a string.")

    normalized = " ".join(word.strip().split())

    if not normalized:
        return []

    return normalized.split(MORSE_CHARACTER_SEPARATOR)


def is_valid_morse_word(word: Any) -> bool:
    # Determines whether every Morse sequence within a word is valid

    if not isinstance(word, str):
        return False

    if not word.strip():
        return False

    sequences = split_morse_word(word)

    return all(
        is_valid_character_sequence(sequence)
        for sequence in sequences
    )


def get_invalid_sequences(word: str) -> List[str]:
    # Returns all unique invalid Morse sequences contained in a word
    #
    # The order of first appearance is preserved

    if not isinstance(word, str):
        raise ValueError("Morse word must be a string.")

    invalid_sequences: List[str] = []

    for sequence in split_morse_word(word):
        if not is_valid_character_sequence(sequence):
            if sequence not in invalid_sequences:
                invalid_sequences.append(sequence)

    return invalid_sequences


# Morse Text Validation

def split_morse_text(text: str) -> List[str]:
    # Splits Morse text into individual Morse words
    #
    # The slash character represents a word boundary

    if not isinstance(text, str):
        raise ValueError("Morse text must be a string.")

    normalized = normalize_morse_text(text)

    if not normalized:
        return []

    return [
        word.strip()
        for word in normalized.split(MORSE_WORD_SEPARATOR)
        if word.strip()
    ]


def is_valid_morse_text(
    text: Any,
    allow_empty: bool = False,
) -> bool:
    # Determines whether complete Morse Code text is valid
    #
    # Morse characters are separated by spaces and Morse words are
    # separated by forward slashes

    if not isinstance(text, str):
        return False

    if not allow_empty and not is_non_empty_string(text):
        return False

    if not text.strip():
        return allow_empty

    words = split_morse_text(text)

    if not words:
        return allow_empty

    return all(
        is_valid_morse_word(word)
        for word in words
    )


def validate_morse_text(
    text: Any,
    allow_empty: bool = False,
) -> str:
    # Validates complete Morse Code text and returns the original input
    #
    # Raises ValueError when the input contains invalid Morse Code

    if not isinstance(text, str):
        raise ValueError("Morse text must be a string.")

    if not allow_empty and not is_non_empty_string(text):
        raise ValueError("Morse text cannot be empty.")

    if not text.strip():
        return text

    invalid_sequences = get_invalid_sequences_from_text(text)

    if invalid_sequences:
        sequences = ", ".join(
            repr(sequence)
            for sequence in invalid_sequences
        )

        raise ValueError(
            f"Invalid Morse Code sequence(s): {sequences}"
        )

    return text


# Invalid Sequence Detection

def get_invalid_sequences_from_text(
    text: str,
) -> List[str]:
    # Returns all unique invalid Morse Code sequences found in the
    # supplied Morse text
    #
    # The order of first appearance is preserved

    if not isinstance(text, str):
        raise ValueError("Morse text must be a string.")

    invalid_sequences: List[str] = []

    for word in split_morse_text(text):
        for sequence in split_morse_word(word):
            if not is_valid_character_sequence(sequence):
                if sequence not in invalid_sequences:
                    invalid_sequences.append(sequence)

    return invalid_sequences


def has_invalid_sequences(text: Any) -> bool:
    # Determines whether complete Morse text contains invalid sequences

    if not isinstance(text, str):
        return False

    return bool(
        get_invalid_sequences_from_text(text)
    )


# Morse Input Normalization

def normalize_morse_text(text: str) -> str:
    # Normalizes Morse Code input while preserving word boundaries
    #
    # Multiple spaces between Morse characters are reduced to a
    # single space, and whitespace around word separators is cleaned

    if not isinstance(text, str):
        raise ValueError("Morse text must be a string.")

    normalized = " ".join(text.strip().split())

    normalized = normalized.replace(
        " / ",
        f" {MORSE_WORD_SEPARATOR} ",
    )

    normalized = normalized.replace(
        f"{MORSE_WORD_SEPARATOR} ",
        f" {MORSE_WORD_SEPARATOR} ",
    )

    normalized = normalized.replace(
        f" {MORSE_WORD_SEPARATOR}",
        f" {MORSE_WORD_SEPARATOR} ",
    )

    normalized = " ".join(normalized.split())

    return normalized


def normalize_morse_word(word: str) -> str:
    # Normalizes whitespace within a single Morse Code word

    if not isinstance(word, str):
        raise ValueError("Morse word must be a string.")

    return " ".join(word.strip().split())


# Separator Validation

def has_valid_separators(text: Any) -> bool:
    # Determines whether Morse Code separators are positioned correctly
    #
    # A valid Morse text should not contain:
    # - Leading word separators
    # - Trailing word separators
    # - Consecutive word separators

    if not isinstance(text, str):
        return False

    normalized = normalize_morse_text(text)

    if not normalized:
        return False

    if normalized.startswith(MORSE_WORD_SEPARATOR):
        return False

    if normalized.endswith(MORSE_WORD_SEPARATOR):
        return False

    if "//" in normalized:
        return False

    return True


# Sequence Analysis

def get_morse_sequence_length(sequence: Any) -> int:
    # Returns the number of dots and dashes in a Morse sequence

    if not isinstance(sequence, str):
        raise ValueError("Morse sequence must be a string.")

    return len(sequence)


def get_morse_symbol_counts(
    sequence: str,
) -> Tuple[int, int]:
    # Returns the number of dots and dashes in a Morse sequence
    #
    # The returned tuple contains:
    # (dot_count, dash_count)

    if not is_morse_sequence(sequence):
        raise ValueError(
            "Sequence must contain only Morse Code dots and dashes."
        )

    dot_count = sequence.count(".")
    dash_count = sequence.count("-")

    return dot_count, dash_count


# Validation Error Helpers

def get_morse_validation_error(
    text: Any,
) -> Optional[str]:
    # Returns a descriptive validation error for Morse Code text
    #
    # Returns None when the text is valid

    if not isinstance(text, str):
        return "Morse text must be a string."

    if not text.strip():
        return "Morse text cannot be empty."

    if not has_valid_separators(text):
        return "Morse Code contains invalid word separators."

    invalid_sequences = get_invalid_sequences_from_text(text)

    if invalid_sequences:
        sequences = ", ".join(
            repr(sequence)
            for sequence in invalid_sequences
        )

        return (
            f"Invalid Morse Code sequence(s): "
            f"{sequences}"
        )

    return None


# Morse Validation Summary

def morse_text_summary(text: Any) -> dict:
    # Returns a summary of the supplied Morse Code text
    #
    # The summary provides information useful to validation,
    # interface, and debugging components

    if not isinstance(text, str):
        return {
            "is_valid": False,
            "length": 0,
            "word_count": 0,
            "character_count": 0,
            "dot_count": 0,
            "dash_count": 0,
            "invalid_sequences": [],
            "error": "Morse text must be a string.",
        }

    normalized = normalize_morse_text(text)
    words = split_morse_text(normalized)

    character_count = 0
    dot_count = 0
    dash_count = 0

    for word in words:
        sequences = split_morse_word(word)

        character_count += len(sequences)

        for sequence in sequences:
            dot_count += sequence.count(".")
            dash_count += sequence.count("-")

    invalid_sequences = (
        get_invalid_sequences_from_text(text)
    )

    return {
        "is_valid": is_valid_morse_text(text),
        "length": len(text),
        "word_count": len(words),
        "character_count": character_count,
        "dot_count": dot_count,
        "dash_count": dash_count,
        "invalid_sequences": invalid_sequences,
        "error": get_morse_validation_error(text),
    }


# Public Module Interface

__all__ = [
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",
    "VALID_MORSE_SYMBOLS",
    "is_morse_symbol",
    "is_morse_sequence",
    "is_valid_character_sequence",
    "split_morse_word",
    "is_valid_morse_word",
    "get_invalid_sequences",
    "split_morse_text",
    "is_valid_morse_text",
    "validate_morse_text",
    "get_invalid_sequences_from_text",
    "has_invalid_sequences",
    "normalize_morse_text",
    "normalize_morse_word",
    "has_valid_separators",
    "get_morse_sequence_length",
    "get_morse_symbol_counts",
    "get_morse_validation_error",
    "morse_text_summary",
]

