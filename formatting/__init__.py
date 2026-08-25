# __init__.py

# Text and Morse Code formatting package for the Morse Translator

# Contains general text formatting utilities, Morse Code formatting
# functionality, whitespace normalization, word separation, and
# output preparation used throughout the translation workflow

# Modules
# formatter - General text formatting and normalization
# morse_formatter - Morse Code-specific formatting and separators

from .formatter import (
    Formatter,
    normalize_text,
    clean_text,
    normalize_whitespace,
)

from .morse_formatter import (
    MorseFormatter,
    format_morse,
    format_morse_word,
    format_morse_character,
    normalize_morse,
)

__all__ = [
    # General Formatting
    "Formatter",
    "normalize_text",
    "clean_text",
    "normalize_whitespace",
    # Morse Formatting
    "MorseFormatter",
    "format_morse",
    "format_morse_word",
    "format_morse_character",
    "normalize_morse",
]

