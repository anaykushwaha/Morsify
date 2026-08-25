# __init__.py

# Shared utilities package for the Morse Translator

# Contains application-wide constants, reusable helper functions,
# input/output utilities, and small general-purpose functions that
# are shared across multiple packages

# Modules
# constants - Application-wide constants and configuration values
# helpers - General-purpose helper functions used throughout the project

from .constants import (
    APPLICATION_NAME,
    APPLICATION_VERSION,
    MORSE_CHARACTER_SEPARATOR,
    MORSE_WORD_SEPARATOR,
    SUPPORTED_LETTERS,
    SUPPORTED_DIGITS,
    SUPPORTED_PUNCTUATION,
    SUPPORTED_CHARACTERS,
    MAX_HISTORY_SIZE,
)

from .helpers import (
    timestamp_now,
    truncate_text,
    copy_to_clipboard,
    safe_strip,
)

__all__ = [
    # Application Constants
    "APPLICATION_NAME",
    "APPLICATION_VERSION",
    # Morse Formatting Constants
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",
    # Supported Characters
    "SUPPORTED_LETTERS",
    "SUPPORTED_DIGITS",
    "SUPPORTED_PUNCTUATION",
    "SUPPORTED_CHARACTERS",
    # History
    "MAX_HISTORY_SIZE",
    # Helpers
    "timestamp_now",
    "truncate_text",
    "copy_to_clipboard",
    "safe_strip",
]

