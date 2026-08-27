# __init__.py
# Text and Morse Code formatting package for the Morse Translator

# Contains general text formatting utilities, Morse Code-specific
# formatting functionality, whitespace normalization, character and
# word grouping, output preparation, display formatting, and formatting
# constants used throughout the translation workflow

# Modules
# formatter - General text formatting, normalization, display formatting,
#             text validation helpers, and output preparation
# morse_formatter - Morse Code formatting, normalization, grouping,
#                   separators, and Morse-specific display utilities

# General Formatting
from .formatter import (
    normalize_text,
    normalize_case,
    clean_text,
    normalize_spaces,
    preserve_line_breaks,
    format_multiline_text,
    format_translation_output,
    format_labeled_output,
    format_input_output,
    truncate_text,
    pad_text,
    is_empty_text,
    has_multiple_lines,
)

# Morse Code Formatting
from .morse_formatter import (
    MORSE_SYMBOLS,
    MORSE_CHARACTER_SEPARATOR,
    MORSE_WORD_SEPARATOR,
    normalize_morse_spacing,
    normalize_morse_word_separator,
    normalize_morse,
    format_morse_character,
    format_morse_word,
    split_morse_words,
    join_morse_words,
    split_morse_characters,
    join_morse_characters,
    format_morse_output,
    format_morse_labeled_output,
    format_morse_input_output,
    count_morse_characters,
    count_morse_words,
    is_morse_text_empty,
)


# Public Module Interface
#
# The package-level API exposes the most commonly used formatting
# functionality so other parts of the Morse Translator can import
# formatting utilities directly from the formatting package.

__all__ = [

    # General Text Formatting

    "normalize_text",
    "normalize_case",
    "clean_text",
    "normalize_spaces",
    "preserve_line_breaks",
    "format_multiline_text",

    # General Output Formatting

    "format_translation_output",
    "format_labeled_output",
    "format_input_output",

    # Text Display Helpers

    "truncate_text",
    "pad_text",

    # General Formatting Checks

    "is_empty_text",
    "has_multiple_lines",

    # Morse Formatting Constants

    "MORSE_SYMBOLS",
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",

    # Morse Normalization

    "normalize_morse_spacing",
    "normalize_morse_word_separator",
    "normalize_morse",

    # Morse Character Formatting

    "format_morse_character",
    "format_morse_word",

    # Morse Word Formatting

    "split_morse_words",
    "join_morse_words",

    # Morse Character Grouping

    "split_morse_characters",
    "join_morse_characters",

    # Morse Output Formatting

    "format_morse_output",
    "format_morse_labeled_output",
    "format_morse_input_output",

    # Morse Formatting Utilities

    "count_morse_characters",
    "count_morse_words",
    "is_morse_text_empty",
]

