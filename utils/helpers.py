# helpers.py
# General-purpose helper utilities for the Morse Translator

# Contains reusable helper functions for type checking, text inspection,
# translation-direction handling, Morse Code analysis, safe conversions,
# and other small operations shared throughout the project


# Type Checking Helpers

def is_string(value) -> bool:
    # Determines whether the supplied value is a string

    return isinstance(value, str)


def is_integer(value) -> bool:
    # Determines whether the supplied value is an integer
    # Boolean values are excluded because bool is a subclass of int

    return isinstance(value, int) and not isinstance(value, bool)


def is_positive_integer(value) -> bool:
    # Determines whether the supplied value is a positive integer

    return is_integer(value) and value > 0


def is_boolean(value) -> bool:
    # Determines whether the supplied value is a boolean

    return isinstance(value, bool)


# Text Inspection Helpers

def is_empty(value: str) -> bool:
    # Determines whether a string is empty or contains only whitespace

    if not isinstance(value, str):
        return False

    return not value.strip()


def get_text_length(text: str) -> int:
    # Returns the number of characters contained in the supplied text

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return len(text)


def count_words(text: str) -> int:
    # Counts the number of whitespace-separated words in a text string

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return len(text.split())


def count_lines(text: str) -> int:
    # Counts the number of lines contained in the supplied text

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    if not text:
        return 0

    return len(text.splitlines())


def count_characters(
    text: str,
    include_spaces: bool = True,
) -> int:
    # Counts characters in text with an option to include or exclude spaces

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    if not isinstance(include_spaces, bool):
        raise ValueError("include_spaces must be a boolean.")

    if include_spaces:
        return len(text)

    return sum(
        1
        for character in text
        if not character.isspace()
    )


# Text Comparison Helpers

def texts_match(
    first: str,
    second: str,
    ignore_case: bool = False,
) -> bool:
    # Determines whether two text values are equal
    # with optional case-insensitive comparison

    if not isinstance(first, str):
        raise ValueError("First text must be a string.")

    if not isinstance(second, str):
        raise ValueError("Second text must be a string.")

    if not isinstance(ignore_case, bool):
        raise ValueError("ignore_case must be a boolean.")

    if ignore_case:
        return first.casefold() == second.casefold()

    return first == second


def normalized_text_matches(
    first: str,
    second: str,
) -> bool:
    # Compares two strings after removing surrounding whitespace
    # and normalizing repeated internal whitespace

    if not isinstance(first, str):
        raise ValueError("First text must be a string.")

    if not isinstance(second, str):
        raise ValueError("Second text must be a string.")

    normalized_first = " ".join(first.strip().split())
    normalized_second = " ".join(second.strip().split())

    return normalized_first == normalized_second


# Translation Direction Helpers

def is_valid_translation_direction(
    direction: str,
) -> bool:
    # Determines whether a translation direction is supported
    # by the Morse Translator application

    from .constants import TRANSLATION_DIRECTIONS

    if not isinstance(direction, str):
        return False

    return direction in TRANSLATION_DIRECTIONS


def reverse_translation_direction(
    direction: str,
) -> str:
    # Returns the opposite translation direction

    from .constants import (
        ENGLISH_TO_MORSE,
        MORSE_TO_ENGLISH,
    )

    if direction == ENGLISH_TO_MORSE:
        return MORSE_TO_ENGLISH

    if direction == MORSE_TO_ENGLISH:
        return ENGLISH_TO_MORSE

    raise ValueError("Invalid translation direction.")


# Morse Code Helpers

def is_morse_symbol(symbol: str) -> bool:
    # Determines whether a character is a valid Morse Code symbol

    if not isinstance(symbol, str):
        return False

    return symbol in {".", "-"}


def count_morse_symbols(morse: str) -> int:
    # Counts dots and dashes contained in a Morse Code string
    # while ignoring separators and whitespace

    if not isinstance(morse, str):
        raise ValueError("Morse Code must be a string.")

    return sum(
        1
        for character in morse
        if character in ".-"
    )


def count_morse_characters(morse: str) -> int:
    # Counts Morse Code character sequences separated by whitespace

    if not isinstance(morse, str):
        raise ValueError("Morse Code must be a string.")

    return len(morse.split())


def contains_morse_symbols(text: str) -> bool:
    # Determines whether a string contains at least one Morse
    # Code dot or dash

    if not isinstance(text, str):
        return False

    return any(
        character in ".-"
        for character in text
    )


# Safe Conversion Helpers

def safe_int(
    value,
    default: int = 0,
) -> int:
    # Attempts to convert a value to an integer
    # and returns a default value if conversion fails

    if not is_integer(default):
        raise ValueError("Default value must be an integer.")

    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def safe_string(
    value,
    default: str = "",
) -> str:
    # Converts a value to a string when possible
    # and returns the supplied default for None

    if not isinstance(default, str):
        raise ValueError("Default value must be a string.")

    if value is None:
        return default

    return str(value)


# Collection Helpers

def list_is_empty(values) -> bool:
    # Determines whether a collection is empty

    if values is None:
        return True

    try:
        return len(values) == 0
    except TypeError:
        return False


def contains_value(
    values,
    value,
) -> bool:
    # Determines whether a collection contains a specified value

    if values is None:
        return False

    try:
        return value in values
    except TypeError:
        return False


# Display Helpers

def create_separator(
    length: int = 40,
    character: str = "-",
) -> str:
    # Creates a repeated-character separator for command-line
    # or text-based display output

    if not is_positive_integer(length):
        raise ValueError(
            "Length must be a positive integer."
        )

    if not isinstance(character, str):
        raise ValueError(
            "Separator character must be a string."
        )

    if len(character) != 1:
        raise ValueError(
            "Separator character must contain exactly one character."
        )

    return character * length


def create_label(
    label: str,
    width: int = 20,
) -> str:
    # Creates a padded label suitable for aligned text output

    if not isinstance(label, str):
        raise ValueError("Label must be a string.")

    if not is_positive_integer(width):
        raise ValueError(
            "Width must be a positive integer."
        )

    return label.strip().ljust(width)


# General Utility Helpers

def clamp(
    value: int,
    minimum: int,
    maximum: int,
) -> int:
    # Restricts an integer value to a specified minimum and maximum range

    if not is_integer(value):
        raise ValueError("Value must be an integer.")

    if not is_integer(minimum):
        raise ValueError("Minimum must be an integer.")

    if not is_integer(maximum):
        raise ValueError("Maximum must be an integer.")

    if minimum > maximum:
        raise ValueError(
            "Minimum cannot be greater than maximum."
        )

    return max(minimum, min(value, maximum))


def ensure_range(
    value: int,
    minimum: int,
    maximum: int,
) -> int:
    # Validates that an integer falls within an inclusive range
    # and returns the value when valid

    if not is_integer(value):
        raise ValueError("Value must be an integer.")

    if not is_integer(minimum):
        raise ValueError("Minimum must be an integer.")

    if not is_integer(maximum):
        raise ValueError("Maximum must be an integer.")

    if minimum > maximum:
        raise ValueError(
            "Minimum cannot be greater than maximum."
        )

    if not minimum <= value <= maximum:
        raise ValueError(
            f"Value must be between {minimum} and {maximum}."
        )

    return value


def remove_none_values(values: dict) -> dict:
    # Creates a copy of a dictionary with entries containing None
    # removed from the result

    if not isinstance(values, dict):
        raise ValueError("Values must be a dictionary.")

    return {
        key: value
        for key, value in values.items()
        if value is not None
    }


# Public Module Interface

__all__ = [
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

