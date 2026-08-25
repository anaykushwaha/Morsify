# morse_code.py
# Morse Code mappings and lookup utilities for the Morse Translator

# Contains the standard Morse Code mappings used throughout the project,
# including English-to-Morse and Morse-to-English conversion tables,
# supported-character checks, and Morse sequence validation utilities

#Morse Code Mappings 
# Standard International Morse Code mapping for supported English
# characters, numbers, and commonly used punctuation

ENGLISH_TO_MORSE = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",

    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
}


# Reverse mapping used when decoding Morse Code back into English 
MORSE_TO_ENGLISH = {
    morse: character
    for character, morse in ENGLISH_TO_MORSE.items()
}

# Lookup Functions

def get_morse_code(character: str) -> str: 
    # Returns the Morse Code representation of a supported character 
    # Characters are normalized to uppercase before lookup so that
    # lowercase English input can be handled consistently 

    if not isinstance(character, str):
        raise ValueError("Character must be a string.")
    if len(character) != 1:
        raise ValueError("Exactly one character must be provided.")

    normalized_character = character.upper()
    return ENGLISH_TO_MORSE[normalized_character]


def get_english_character(morse_sequence: str) -> str: 
    # Returns the English character represented by a Morse Code sequence 

    if not isinstance(morse_sequence, str):
        raise ValueError("Morse sequence must be a string.")
    if not morse_sequence:
        raise ValueError("Morse sequence cannot be empty.")

    return MORSE_TO_ENGLISH[morse_sequence]


# Character and Sequence Validation

def is_supported_character(character: str) -> bool: 
    # Determines whether a character is supported by the translator 
    # English letters are checked case-insensitively 
    # Numbers and supported punctuation are checked directly 

    if not isinstance(character, str) or len(character) != 1:
        return False

    return character.upper() in ENGLISH_TO_MORSE


def is_valid_morse_sequence(morse_sequence: str) -> bool: 
    # Determines whether a Morse Code sequence represents a supported character 
    # A valid sequence contains only dots and dashes and must exist
    # in the reverse Morse Code mapping 

    if not isinstance(morse_sequence, str):
        return False
    if not morse_sequence:
        return False
    if any(symbol not in ".-" for symbol in morse_sequence):
        return False

    return morse_sequence in MORSE_TO_ENGLISH


# Public Module Interface

__all__ = [
    "ENGLISH_TO_MORSE",
    "MORSE_TO_ENGLISH",
    "get_morse_code",
    "get_english_character",
    "is_supported_character",
    "is_valid_morse_sequence",
]

