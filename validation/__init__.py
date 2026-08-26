# __init__.py
# Input validation package for the Morse Translator

# Contains general validation utilities, English text validation,
# Morse Code validation, structured validation results, validation
# error helpers, normalization utilities, and validation summaries

# Modules
# validator - General validation and input utility functions
# english_validator - English text and character validation
# morse_validator - Morse Code sequence and text validation
# validation_result - Structured validation result model and helpers


# General Validation

from .validator import (
    is_string,
    is_non_empty_string,
    is_empty_string,
    is_none_or_empty,
    normalize_text,
    normalize_whitespace,
    is_within_length,
    validate_length,
    is_single_character,
    is_whitespace_character,
    is_list,
    is_non_empty_list,
    validate_string,
    validate_character,
    get_string_error,
    get_character_error,
)


# English Validation

from .english_validator import (
    is_english_letter,
    is_english_digit,
    is_supported_punctuation,
    is_supported_english_character,
    get_unsupported_characters,
    has_unsupported_characters,
    is_valid_english_text,
    validate_english_text,
    normalize_english_text,
    get_character_type,
    is_letter_only,
    is_numeric_only,
    get_words,
    validate_words,
    get_english_validation_error,
    english_text_summary,
)


# Morse Validation

from .morse_validator import (
    MORSE_CHARACTER_SEPARATOR,
    MORSE_WORD_SEPARATOR,
    VALID_MORSE_SYMBOLS,
    is_morse_symbol,
    is_morse_sequence,
    is_valid_character_sequence,
    split_morse_word,
    is_valid_morse_word,
    get_invalid_sequences,
    split_morse_text,
    is_valid_morse_text,
    validate_morse_text,
    get_invalid_sequences_from_text,
    has_invalid_sequences,
    normalize_morse_text,
    normalize_morse_word,
    has_valid_separators,
    get_morse_sequence_length,
    get_morse_symbol_counts,
    get_morse_validation_error,
    morse_text_summary,
)


# Validation Results

from .validation_result import (
    ValidationResult,
    combine_results,
    valid_result,
    invalid_result,
    is_validation_result,
    ensure_validation_result,
)


# Public Package Interface

__all__ = [

    # General Validation

    "is_string",
    "is_non_empty_string",
    "is_empty_string",
    "is_none_or_empty",
    "normalize_text",
    "normalize_whitespace",
    "is_within_length",
    "validate_length",
    "is_single_character",
    "is_whitespace_character",
    "is_list",
    "is_non_empty_list",
    "validate_string",
    "validate_character",
    "get_string_error",
    "get_character_error",


    # English Validation

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


    # Morse Validation

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


    # Validation Results

    "ValidationResult",
    "combine_results",
    "valid_result",
    "invalid_result",
    "is_validation_result",
    "ensure_validation_result",
]

