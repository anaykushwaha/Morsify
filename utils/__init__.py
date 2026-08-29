# __init__.py
# Shared utilities package for the Morse Translator

# Contains application-wide constants, translation configuration,
# GUI configuration, validation messages, supported character
# definitions, reusable helper functions, text inspection utilities,
# Morse Code utilities, safe conversion functions, display helpers,
# and general-purpose utilities shared throughout the project


# Modules

# constants - Application-wide constants and configuration values
# helpers - General-purpose helper functions used throughout the project


# Application Information

from .constants import (
    APPLICATION_NAME,
    APPLICATION_VERSION,
    APPLICATION_DESCRIPTION,
)


# Translation Configuration

from .constants import (
    ENGLISH_TO_MORSE,
    MORSE_TO_ENGLISH,
    TRANSLATION_DIRECTIONS,
)


# Morse Code Configuration

from .constants import (
    MORSE_CHARACTER_SEPARATOR,
    MORSE_WORD_SEPARATOR,
    MORSE_SYMBOLS,
    MORSE_DOT,
    MORSE_DASH,
)


# Input and Output Defaults

from .constants import (
    DEFAULT_INPUT_TEXT,
    DEFAULT_OUTPUT_TEXT,
    DEFAULT_TRANSLATION_DIRECTION,
)


# Text Formatting Configuration

from .constants import (
    DEFAULT_TEXT_ENCODING,
    DEFAULT_MAX_INPUT_LENGTH,
    DEFAULT_MAX_OUTPUT_LENGTH,
    DEFAULT_TRUNCATION_SUFFIX,
)


# History Configuration

from .constants import (
    DEFAULT_HISTORY_LIMIT,
    MIN_HISTORY_LIMIT,
    MAX_HISTORY_LIMIT,
    HISTORY_TIMESTAMP_FORMAT,
)


# GUI Configuration

from .constants import (
    DEFAULT_WINDOW_WIDTH,
    DEFAULT_WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,
    WINDOW_RESIZABLE,
)


# GUI Text

from .constants import (
    APP_TITLE,
    INPUT_LABEL,
    OUTPUT_LABEL,
    TRANSLATE_BUTTON_TEXT,
    CLEAR_BUTTON_TEXT,
    COPY_BUTTON_TEXT,
    SWAP_BUTTON_TEXT,
    HISTORY_BUTTON_TEXT,
    CLEAR_HISTORY_BUTTON_TEXT,
    EXIT_BUTTON_TEXT,
)


# Validation Messages

from .constants import (
    EMPTY_INPUT_MESSAGE,
    INVALID_INPUT_TYPE_MESSAGE,
    INVALID_DIRECTION_MESSAGE,
    UNSUPPORTED_CHARACTER_MESSAGE,
    INVALID_MORSE_MESSAGE,
)


# Application Messages

from .constants import (
    TRANSLATION_SUCCESS_MESSAGE,
    TRANSLATION_ERROR_MESSAGE,
    COPY_SUCCESS_MESSAGE,
    HISTORY_EMPTY_MESSAGE,
    HISTORY_CLEARED_MESSAGE,
)


# Supported Characters

from .constants import (
    SUPPORTED_LETTERS,
    SUPPORTED_DIGITS,
    SUPPORTED_PUNCTUATION,
    SUPPORTED_ENGLISH_CHARACTERS,
)


# File and Data Configuration

from .constants import (
    HISTORY_FILE_NAME,
    DEFAULT_DATA_DIRECTORY,
    JSON_ENCODING,
    JSON_INDENT,
)


# Utility Configuration

from .constants import (
    MIN_TEXT_LENGTH,
    DEFAULT_TRUNCATE_LENGTH,
    DEFAULT_PADDING_WIDTH,
    DEFAULT_ALIGNMENT,
    VALID_ALIGNMENTS,
)


# Boolean Defaults

from .constants import (
    DEFAULT_CASE_SENSITIVE,
    DEFAULT_PRESERVE_SPACES,
    DEFAULT_PRESERVE_LINE_BREAKS,
)


# Type Checking Helpers

from .helpers import (
    is_string,
    is_integer,
    is_positive_integer,
    is_boolean,
)


# Text Inspection Helpers

from .helpers import (
    is_empty,
    get_text_length,
    count_words,
    count_lines,
    count_characters,
)


# Text Comparison Helpers

from .helpers import (
    texts_match,
    normalized_text_matches,
)


# Translation Direction Helpers

from .helpers import (
    is_valid_translation_direction,
    reverse_translation_direction,
)


# Morse Code Helpers

from .helpers import (
    is_morse_symbol,
    count_morse_symbols,
    count_morse_characters,
    contains_morse_symbols,
)


# Safe Conversion Helpers

from .helpers import (
    safe_int,
    safe_string,
)


# Collection Helpers

from .helpers import (
    list_is_empty,
    contains_value,
)


# Display Helpers

from .helpers import (
    create_separator,
    create_label,
)


# General Utility Helpers

from .helpers import (
    clamp,
    ensure_range,
    remove_none_values,
)


# Public Module Interface

__all__ = [
    # Application Information
    "APPLICATION_NAME",
    "APPLICATION_VERSION",
    "APPLICATION_DESCRIPTION",

    # Translation Configuration
    "ENGLISH_TO_MORSE",
    "MORSE_TO_ENGLISH",
    "TRANSLATION_DIRECTIONS",

    # Morse Code Configuration
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",
    "MORSE_SYMBOLS",
    "MORSE_DOT",
    "MORSE_DASH",

    # Input and Output Defaults
    "DEFAULT_INPUT_TEXT",
    "DEFAULT_OUTPUT_TEXT",
    "DEFAULT_TRANSLATION_DIRECTION",

    # Text Formatting Configuration
    "DEFAULT_TEXT_ENCODING",
    "DEFAULT_MAX_INPUT_LENGTH",
    "DEFAULT_MAX_OUTPUT_LENGTH",
    "DEFAULT_TRUNCATION_SUFFIX",

    # History Configuration
    "DEFAULT_HISTORY_LIMIT",
    "MIN_HISTORY_LIMIT",
    "MAX_HISTORY_LIMIT",
    "HISTORY_TIMESTAMP_FORMAT",

    # GUI Configuration
    "DEFAULT_WINDOW_WIDTH",
    "DEFAULT_WINDOW_HEIGHT",
    "MIN_WINDOW_WIDTH",
    "MIN_WINDOW_HEIGHT",
    "WINDOW_RESIZABLE",

    # GUI Text
    "APP_TITLE",
    "INPUT_LABEL",
    "OUTPUT_LABEL",
    "TRANSLATE_BUTTON_TEXT",
    "CLEAR_BUTTON_TEXT",
    "COPY_BUTTON_TEXT",
    "SWAP_BUTTON_TEXT",
    "HISTORY_BUTTON_TEXT",
    "CLEAR_HISTORY_BUTTON_TEXT",
    "EXIT_BUTTON_TEXT",

    # Validation Messages
    "EMPTY_INPUT_MESSAGE",
    "INVALID_INPUT_TYPE_MESSAGE",
    "INVALID_DIRECTION_MESSAGE",
    "UNSUPPORTED_CHARACTER_MESSAGE",
    "INVALID_MORSE_MESSAGE",

    # Application Messages
    "TRANSLATION_SUCCESS_MESSAGE",
    "TRANSLATION_ERROR_MESSAGE",
    "COPY_SUCCESS_MESSAGE",
    "HISTORY_EMPTY_MESSAGE",
    "HISTORY_CLEARED_MESSAGE",

    # Supported Characters
    "SUPPORTED_LETTERS",
    "SUPPORTED_DIGITS",
    "SUPPORTED_PUNCTUATION",
    "SUPPORTED_ENGLISH_CHARACTERS",

    # File and Data Configuration
    "HISTORY_FILE_NAME",
    "DEFAULT_DATA_DIRECTORY",
    "JSON_ENCODING",
    "JSON_INDENT",

    # Utility Configuration
    "MIN_TEXT_LENGTH",
    "DEFAULT_TRUNCATE_LENGTH",
    "DEFAULT_PADDING_WIDTH",
    "DEFAULT_ALIGNMENT",
    "VALID_ALIGNMENTS",

    # Boolean Defaults
    "DEFAULT_CASE_SENSITIVE",
    "DEFAULT_PRESERVE_SPACES",
    "DEFAULT_PRESERVE_LINE_BREAKS",

    # Type Checking Helpers
    "is_string",
    "is_integer",
    "is_positive_integer",
    "is_boolean",

    # Text Inspection Helpers
    "is_empty",
    "get_text_length",
    "count_words",
    "count_lines",
    "count_characters",

    # Text Comparison Helpers
    "texts_match",
    "normalized_text_matches",

    # Translation Direction Helpers
    "is_valid_translation_direction",
    "reverse_translation_direction",

    # Morse Code Helpers
    "is_morse_symbol",
    "count_morse_symbols",
    "count_morse_characters",
    "contains_morse_symbols",

    # Safe Conversion Helpers
    "safe_int",
    "safe_string",

    # Collection Helpers
    "list_is_empty",
    "contains_value",

    # Display Helpers
    "create_separator",
    "create_label",

    # General Utility Helpers
    "clamp",
    "ensure_range",
    "remove_none_values",
]

