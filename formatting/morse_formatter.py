# morse_formatter.py
# Morse Code formatting utilities for the Morse Translator

# Contains Morse-specific formatting functions for preparing,
# normalizing, grouping, and displaying Morse Code consistently
# throughout the translation workflow


# Morse Formatting Constants

MORSE_SYMBOLS = {".", "-"}

MORSE_CHARACTER_SEPARATOR = " "

MORSE_WORD_SEPARATOR = " / "


# Morse Sequence Formatting

def normalize_morse_spacing(morse_text: str) -> str:
    # Normalizes whitespace around Morse Code while preserving
    # word separators represented by forward slashes

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    text = morse_text.strip()

    if not text:
        return ""

    words = text.split("/")

    formatted_words = []

    for word in words:
        symbols = word.split()

        if symbols:
            formatted_words.append(" ".join(symbols))
        else:
            formatted_words.append("")

    return " / ".join(formatted_words)


def normalize_morse_word_separator(morse_text: str) -> str:
    # Converts different forms of forward-slash word separators
    # into the standard " / " representation

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    text = morse_text.strip()

    if not text:
        return ""

    words = text.split("/")

    return " / ".join(
        " ".join(word.split())
        for word in words
    )


def normalize_morse(text: str) -> str:
    # Applies the standard Morse Code formatting rules to a complete
    # Morse string including symbol spacing and word separators

    if not isinstance(text, str):
        raise ValueError("Morse text must be a string.")

    return normalize_morse_spacing(text)


# Morse Character Formatting

def format_morse_character(morse_sequence: str) -> str:
    # Formats a single Morse Code character by removing unnecessary
    # surrounding whitespace

    if not isinstance(morse_sequence, str):
        raise ValueError("Morse sequence must be a string.")

    sequence = morse_sequence.strip()

    if not sequence:
        raise ValueError("Morse sequence cannot be empty.")

    if any(symbol not in MORSE_SYMBOLS for symbol in sequence):
        raise ValueError(
            "Morse sequence can only contain dots and dashes."
        )

    return sequence


def format_morse_word(morse_word: str) -> str:
    # Formats a sequence of Morse characters representing one word

    if not isinstance(morse_word, str):
        raise ValueError("Morse word must be a string.")

    word = morse_word.strip()

    if not word:
        return ""

    characters = word.split()

    for character in characters:
        if any(symbol not in MORSE_SYMBOLS for symbol in character):
            raise ValueError(
                "Morse word contains an invalid Morse sequence."
            )

    return " ".join(characters)


# Morse Word Formatting

def split_morse_words(morse_text: str) -> list[str]:
    # Splits Morse text into individual word groups using the
    # standard forward-slash word separator

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    normalized = normalize_morse(morse_text)

    if not normalized:
        return []

    return [
        word.strip()
        for word in normalized.split("/")
    ]


def join_morse_words(words: list[str]) -> str:
    # Combines formatted Morse word groups using the standard
    # Morse Code word separator

    if not isinstance(words, list):
        raise ValueError("Words must be provided as a list.")

    formatted_words = []

    for word in words:
        if not isinstance(word, str):
            raise ValueError("Each Morse word must be a string.")

        formatted_words.append(format_morse_word(word))

    return MORSE_WORD_SEPARATOR.join(formatted_words)


# Morse Character Grouping

def split_morse_characters(morse_word: str) -> list[str]:
    # Splits a Morse word into individual Morse character sequences

    if not isinstance(morse_word, str):
        raise ValueError("Morse word must be a string.")

    formatted_word = format_morse_word(morse_word)

    if not formatted_word:
        return []

    return formatted_word.split()


def join_morse_characters(characters: list[str]) -> str:
    # Combines individual Morse character sequences using the
    # standard single-space character separator

    if not isinstance(characters, list):
        raise ValueError("Characters must be provided as a list.")

    formatted_characters = []

    for character in characters:
        formatted_characters.append(
            format_morse_character(character)
        )

    return MORSE_CHARACTER_SEPARATOR.join(
        formatted_characters
    )


# Morse Display Formatting

def format_morse_output(morse_text: str) -> str:
    # Formats Morse Code into the standard human-readable representation
    # used by the translator's output interfaces

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    return normalize_morse(morse_text)


def format_morse_labeled_output(
    label: str,
    morse_text: str,
) -> str:
    # Creates a labeled representation of Morse Code output

    if not isinstance(label, str):
        raise ValueError("Label must be a string.")

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    normalized_label = label.strip()

    if not normalized_label:
        raise ValueError("Label cannot be empty.")

    formatted_morse = format_morse_output(morse_text)

    return f"{normalized_label}: {formatted_morse}"


def format_morse_input_output(
    input_text: str,
    output_text: str,
) -> str:
    # Creates a consistent two-line representation for Morse input
    # and translated output

    if not isinstance(input_text, str):
        raise ValueError("Input text must be a string.")

    if not isinstance(output_text, str):
        raise ValueError("Output text must be a string.")

    formatted_input = format_morse_output(input_text)
    formatted_output = output_text.strip()

    return (
        f"Input: {formatted_input}\n"
        f"Output: {formatted_output}"
    )


# Morse Formatting Utilities

def count_morse_characters(morse_text: str) -> int:
    # Counts the number of Morse character sequences contained
    # in a formatted Morse string

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    words = split_morse_words(morse_text)

    return sum(
        len(split_morse_characters(word))
        for word in words
    )


def count_morse_words(morse_text: str) -> int:
    # Counts the number of word groups contained in Morse text

    if not isinstance(morse_text, str):
        raise ValueError("Morse text must be a string.")

    words = split_morse_words(morse_text)

    return len(words)


def is_morse_text_empty(morse_text: str) -> bool:
    # Determines whether Morse text contains no meaningful content

    if not isinstance(morse_text, str):
        return False

    return not morse_text.strip()


# Public Module Interface

__all__ = [
    # Morse Formatting Constants
    "MORSE_SYMBOLS",
    "MORSE_CHARACTER_SEPARATOR",
    "MORSE_WORD_SEPARATOR",

    # Morse Sequence Formatting
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

    # Morse Display Formatting
    "format_morse_output",
    "format_morse_labeled_output",
    "format_morse_input_output",

    # Morse Formatting Utilities
    "count_morse_characters",
    "count_morse_words",
    "is_morse_text_empty",
]

