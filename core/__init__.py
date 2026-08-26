# __init__.py
# Core translation package for the Morse Translator

# Contains the complete translation engine used by the Morse Translator,
# including Morse Code mappings, character and sequence lookup utilities,
# English-to-Morse encoding, Morse-to-English decoding, translation
# result models, translation direction definitions, and the high-level
# MorseTranslator interface


# Modules
# morse_code - Standard Morse Code mappings and lookup utilities
# translation - Translation result data model and direction definitions
# encoder - English-to-Morse Code encoding functions
# decoder - Morse-to-English Code decoding functions
# translator - High-level translation interface and convenience functions


# Morse Code Mappings

from .morse_code import (
    ENGLISH_TO_MORSE,
    MORSE_TO_ENGLISH,
    get_morse_code,
    get_english_character,
    is_supported_character,
    is_valid_morse_sequence,
)


# Translation Models

from .translation import (
    Translation,
    TranslationDirection,
    create_translation,
)


# English-to-Morse Encoding

from .encoder import (
    encode,
    encode_character,
    encode_word,
    encode_characters,
    encode_words,
)


# Morse-to-English Decoding

from .decoder import (
    decode,
    decode_character,
    decode_word,
    decode_characters,
    decode_words,
    normalize_morse_input,
)


# High-Level Translation Interface

from .translator import (
    MorseTranslator,
    translate_to_morse,
    translate_to_english,
)


# Public Module Interface

__all__ = [
    # Morse Code Mappings
    "ENGLISH_TO_MORSE",
    "MORSE_TO_ENGLISH",
    "get_morse_code",
    "get_english_character",
    "is_supported_character",
    "is_valid_morse_sequence",
    # Translation Models
    "Translation",
    "TranslationDirection",
    "create_translation",
    # English-to-Morse Encoding
    "encode",
    "encode_character",
    "encode_word",
    "encode_characters",
    "encode_words",
    # Morse-to-English Decoding
    "decode",
    "decode_character",
    "decode_word",
    "decode_characters",
    "decode_words",
    "normalize_morse_input",
    # High-Level Translation Interface
    "MorseTranslator",
    "translate_to_morse",
    "translate_to_english",
]

