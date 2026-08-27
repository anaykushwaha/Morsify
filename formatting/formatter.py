# formatter.py
# General text formatting utilities for the Morse Translator

# Contains reusable formatting functions for cleaning, normalizing,
# and preparing English text and translated output for consistent
# display and processing throughout the project


# Text Normalization

def normalize_text(text: str) -> str:
    # Normalizes text by removing unnecessary surrounding whitespace
    # and converting repeated internal whitespace into single spaces

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return " ".join(text.strip().split())


def normalize_case(text: str) -> str:
    # Normalizes text to uppercase for consistent processing
    # without changing numbers, spaces, or punctuation

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return text.upper()


def clean_text(text: str) -> str:
    # Cleans text by removing leading and trailing whitespace
    # while preserving meaningful internal spacing

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return text.strip()


# Spacing and Display Formatting

def normalize_spaces(text: str) -> str:
    # Replaces consecutive whitespace characters with a single space

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return " ".join(text.split())


def preserve_line_breaks(text: str) -> str:
    # Cleans whitespace from individual lines while preserving
    # the original line structure

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    lines = text.splitlines()

    return "\n".join(line.strip() for line in lines)


def format_multiline_text(text: str) -> str:
    # Formats multiline text by cleaning each line and removing
    # unnecessary whitespace surrounding the complete input

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    lines = [
        line.strip()
        for line in text.strip().splitlines()
    ]

    return "\n".join(lines)


# Output Formatting

def format_translation_output(text: str) -> str:
    # Formats translated text into a clean representation suitable
    # for display in the command-line interface or graphical interface

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    return text.strip()


def format_labeled_output(label: str, text: str) -> str:
    # Creates a simple labeled representation of formatted output

    if not isinstance(label, str):
        raise ValueError("Label must be a string.")

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    normalized_label = label.strip()
    formatted_text = text.strip()

    if not normalized_label:
        raise ValueError("Label cannot be empty.")

    return f"{normalized_label}: {formatted_text}"


def format_input_output(input_text: str, output_text: str) -> str:
    # Creates a consistent two-line representation of an input
    # and its corresponding translated output

    if not isinstance(input_text, str):
        raise ValueError("Input text must be a string.")

    if not isinstance(output_text, str):
        raise ValueError("Output text must be a string.")

    formatted_input = input_text.strip()
    formatted_output = output_text.strip()

    return (
        f"Input: {formatted_input}\n"
        f"Output: {formatted_output}"
    )


# Length and Display Helpers

def truncate_text(
    text: str,
    max_length: int,
    suffix: str = "...",
) -> str:
    # Truncates text when it exceeds the supplied maximum length
    # and appends the specified suffix

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    if not isinstance(max_length, int):
        raise ValueError("Maximum length must be an integer.")

    if max_length < 0:
        raise ValueError("Maximum length cannot be negative.")

    if not isinstance(suffix, str):
        raise ValueError("Suffix must be a string.")

    if len(text) <= max_length:
        return text

    if len(suffix) >= max_length:
        return suffix[:max_length]

    return text[:max_length - len(suffix)] + suffix


def pad_text(
    text: str,
    width: int,
    alignment: str = "left",
) -> str:
    # Pads text to a requested width using the specified alignment

    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    if not isinstance(width, int):
        raise ValueError("Width must be an integer.")

    if width < 0:
        raise ValueError("Width cannot be negative.")

    if alignment not in {"left", "right", "center"}:
        raise ValueError(
            "Alignment must be 'left', 'right', or 'center'."
        )

    if alignment == "left":
        return text.ljust(width)

    if alignment == "right":
        return text.rjust(width)

    return text.center(width)


# Formatting Validation

def is_empty_text(text: str) -> bool:
    # Determines whether text is empty or contains only whitespace

    if not isinstance(text, str):
        return False

    return not text.strip()


def has_multiple_lines(text: str) -> bool:
    # Determines whether the supplied text contains more than one line

    if not isinstance(text, str):
        return False

    return len(text.splitlines()) > 1


# Public Module Interface

__all__ = [
    # Text Normalization
    "normalize_text",
    "normalize_case",
    "clean_text",

    # Spacing and Display Formatting
    "normalize_spaces",
    "preserve_line_breaks",
    "format_multiline_text",

    # Output Formatting
    "format_translation_output",
    "format_labeled_output",
    "format_input_output",

    # Length and Display Helpers
    "truncate_text",
    "pad_text",

    # Formatting Validation
    "is_empty_text",
    "has_multiple_lines",
]

