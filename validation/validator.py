# validator.py
# General validation utilities for the Morse Translator

# Contains shared validation functions used throughout the validation
# package, including type checking, empty-input detection, whitespace
# handling, and common validation helpers

from typing import Any, Optional


# General Input Validation

def is_string(value: Any) -> bool:
    # Determines whether the supplied value is a string

    return isinstance(value, str)


def is_non_empty_string(value: Any) -> bool:
    # Determines whether the supplied value is a non-empty string
    #
    # Whitespace-only strings are considered empty

    if not isinstance(value, str):
        return False

    return bool(value.strip())


def is_empty_string(value: Any) -> bool:
    # Determines whether the supplied value is an empty or whitespace-only string

    if not isinstance(value, str):
        return False

    return not bool(value.strip())


def is_none_or_empty(value: Any) -> bool:
    # Determines whether a value is None, an empty string,
    # or a whitespace-only string

    if value is None:
        return True

    if isinstance(value, str):
        return not bool(value.strip())

    return False


# Input Normalization

def normalize_text(value: str) -> str:
    # Normalizes general text input by removing leading and trailing
    # whitespace and collapsing repeated internal whitespace

    if not isinstance(value, str):
        raise ValueError("Value must be a string.")

    return " ".join(value.strip().split())


def normalize_whitespace(value: str) -> str:
    # Removes leading and trailing whitespace while preserving
    # internal whitespace structure

    if not isinstance(value, str):
        raise ValueError("Value must be a string.")

    return value.strip()


# Length Validation

def is_within_length(
    value: str,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
) -> bool:
    # Determines whether a string falls within the supplied length range
    #
    # Minimum and maximum values are optional

    if not isinstance(value, str):
        return False

    if minimum is not None:
        if not isinstance(minimum, int) or minimum < 0:
            raise ValueError(
                "Minimum length must be a non-negative integer."
            )

        if len(value) < minimum:
            return False

    if maximum is not None:
        if not isinstance(maximum, int) or maximum < 0:
            raise ValueError(
                "Maximum length must be a non-negative integer."
            )

        if len(value) > maximum:
            return False

    if (
        minimum is not None
        and maximum is not None
        and minimum > maximum
    ):
        raise ValueError(
            "Minimum length cannot be greater than maximum length."
        )

    return True


def validate_length(
    value: str,
    minimum: Optional[int] = None,
    maximum: Optional[int] = None,
) -> None:
    # Validates that a string falls within the supplied length range
    #
    # Raises ValueError when the value is invalid

    if not isinstance(value, str):
        raise ValueError("Value must be a string.")

    if (
        minimum is not None
        and maximum is not None
        and minimum > maximum
    ):
        raise ValueError(
            "Minimum length cannot be greater than maximum length."
        )

    if minimum is not None:
        if not isinstance(minimum, int) or minimum < 0:
            raise ValueError(
                "Minimum length must be a non-negative integer."
            )

        if len(value) < minimum:
            raise ValueError(
                f"Value must contain at least {minimum} characters."
            )

    if maximum is not None:
        if not isinstance(maximum, int) or maximum < 0:
            raise ValueError(
                "Maximum length must be a non-negative integer."
            )

        if len(value) > maximum:
            raise ValueError(
                f"Value cannot contain more than {maximum} characters."
            )


# Character Validation

def is_single_character(value: Any) -> bool:
    # Determines whether the supplied value contains exactly one character

    return isinstance(value, str) and len(value) == 1


def is_whitespace_character(value: Any) -> bool:
    # Determines whether the supplied value is a single whitespace character

    return (
        isinstance(value, str)
        and len(value) == 1
        and value.isspace()
    )


# Collection Validation

def is_list(value: Any) -> bool:
    # Determines whether the supplied value is a list

    return isinstance(value, list)


def is_non_empty_list(value: Any) -> bool:
    # Determines whether the supplied value is a non-empty list

    return isinstance(value, list) and bool(value)


# Generic Validation

def validate_string(
    value: Any,
    field_name: str = "Value",
    allow_empty: bool = False,
) -> str:
    # Validates and returns a string value
    #
    # Raises ValueError when the supplied value is not a string
    # or when an empty value is not allowed

    if not isinstance(value, str):
        raise ValueError(
            f"{field_name} must be a string."
        )

    if not allow_empty and not value.strip():
        raise ValueError(
            f"{field_name} cannot be empty."
        )

    return value


def validate_character(
    value: Any,
    field_name: str = "Character",
) -> str:
    # Validates and returns a single-character string

    if not isinstance(value, str):
        raise ValueError(
            f"{field_name} must be a string."
        )

    if len(value) != 1:
        raise ValueError(
            f"{field_name} must contain exactly one character."
        )

    return value


# Validation Summary Helpers

def get_string_error(
    value: Any,
    field_name: str = "Value",
) -> Optional[str]:
    # Returns a descriptive validation error for a general string
    #
    # Returns None when the value is valid

    if not isinstance(value, str):
        return f"{field_name} must be a string."

    if not value.strip():
        return f"{field_name} cannot be empty."

    return None


def get_character_error(
    value: Any,
    field_name: str = "Character",
) -> Optional[str]:
    # Returns a descriptive validation error for a single character
    #
    # Returns None when the value is valid

    if not isinstance(value, str):
        return f"{field_name} must be a string."

    if len(value) != 1:
        return f"{field_name} must contain exactly one character."

    return None


# Public Module Interface

__all__ = [
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
]

