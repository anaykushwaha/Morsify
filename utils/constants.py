# constants.py
# Shared constants for the Morse Translator

# Contains application-wide constants used throughout the project,
# including application metadata, translation directions, Morse Code
# separators, history settings, formatting values, and supported
# configuration options


# Application Information

APPLICATION_NAME = "Morse Translator"

APPLICATION_VERSION = "1.0.0"

APPLICATION_DESCRIPTION = (
    "A Python application for translating English text "
    "to Morse Code and Morse Code to English."
)


# Translation Directions

ENGLISH_TO_MORSE = "English to Morse"

MORSE_TO_ENGLISH = "Morse to English"

TRANSLATION_DIRECTIONS = (
    ENGLISH_TO_MORSE,
    MORSE_TO_ENGLISH,
)


# Morse Code Separators

MORSE_CHARACTER_SEPARATOR = " "

MORSE_WORD_SEPARATOR = " / "

MORSE_SYMBOLS = ".-"

MORSE_DOT = "."

MORSE_DASH = "-"


# Input and Output Defaults

DEFAULT_INPUT_TEXT = ""

DEFAULT_OUTPUT_TEXT = ""

DEFAULT_TRANSLATION_DIRECTION = ENGLISH_TO_MORSE


# Text Formatting

DEFAULT_TEXT_ENCODING = "utf-8"

DEFAULT_MAX_INPUT_LENGTH = 10000

DEFAULT_MAX_OUTPUT_LENGTH = 20000

DEFAULT_TRUNCATION_SUFFIX = "..."


# History Configuration

DEFAULT_HISTORY_LIMIT = 50

MIN_HISTORY_LIMIT = 1

MAX_HISTORY_LIMIT = 1000

HISTORY_TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


# GUI Configuration

DEFAULT_WINDOW_WIDTH = 800

DEFAULT_WINDOW_HEIGHT = 600

MIN_WINDOW_WIDTH = 600

MIN_WINDOW_HEIGHT = 450

WINDOW_RESIZABLE = True


# GUI Text

APP_TITLE = APPLICATION_NAME

INPUT_LABEL = "Input"

OUTPUT_LABEL = "Output"

TRANSLATE_BUTTON_TEXT = "Translate"

CLEAR_BUTTON_TEXT = "Clear"

COPY_BUTTON_TEXT = "Copy"

SWAP_BUTTON_TEXT = "Swap"

HISTORY_BUTTON_TEXT = "History"

CLEAR_HISTORY_BUTTON_TEXT = "Clear History"

EXIT_BUTTON_TEXT = "Exit"


# Validation Messages

EMPTY_INPUT_MESSAGE = "Input cannot be empty."

INVALID_INPUT_TYPE_MESSAGE = "Input must be a string."

INVALID_DIRECTION_MESSAGE = "Invalid translation direction."

UNSUPPORTED_CHARACTER_MESSAGE = "Input contains unsupported characters."

INVALID_MORSE_MESSAGE = "Input contains invalid Morse Code."


# General Application Messages

TRANSLATION_SUCCESS_MESSAGE = "Translation completed successfully."

TRANSLATION_ERROR_MESSAGE = "Translation could not be completed."

COPY_SUCCESS_MESSAGE = "Output copied to clipboard."

HISTORY_EMPTY_MESSAGE = "No translation history available."

HISTORY_CLEARED_MESSAGE = "Translation history cleared."


# Supported Character Categories

SUPPORTED_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

SUPPORTED_DIGITS = "0123456789"

SUPPORTED_PUNCTUATION = (
    ".,?'!/()&:;=+-_\"$@"
)

SUPPORTED_ENGLISH_CHARACTERS = (
    SUPPORTED_LETTERS
    + SUPPORTED_DIGITS
    + SUPPORTED_PUNCTUATION
)


# File and Data Configuration

HISTORY_FILE_NAME = "translation_history.json"

DEFAULT_DATA_DIRECTORY = "data"

JSON_ENCODING = "utf-8"

JSON_INDENT = 4


# Utility Configuration

MIN_TEXT_LENGTH = 1

DEFAULT_TRUNCATE_LENGTH = 50

DEFAULT_PADDING_WIDTH = 20

DEFAULT_ALIGNMENT = "left"

VALID_ALIGNMENTS = (
    "left",
    "right",
    "center",
)


# Boolean Defaults

DEFAULT_CASE_SENSITIVE = False

DEFAULT_PRESERVE_SPACES = True

DEFAULT_PRESERVE_LINE_BREAKS = True


# Public Module Interface

__all__ = [
    # Application Information
    "APPLICATION_NAME",
    "APPLICATION_VERSION",
    "APPLICATION_DESCRIPTION",

    # Translation Directions
    "ENGLISH_TO_MORSE",
    "MORSE_TO_ENGLISH",
    "TRANSLATION_DIRECTIONS",

    # Morse Code Separators
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",
    "MORSE_SYMBOLS",
    "MORSE_DOT",
    "MORSE_DASH",

    # Input and Output Defaults
    "DEFAULT_INPUT_TEXT",
    "DEFAULT_OUTPUT_TEXT",
    "DEFAULT_TRANSLATION_DIRECTION",

    # Text Formatting
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

    # Supported Character Categories
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
]

