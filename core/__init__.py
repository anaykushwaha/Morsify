# __init__.py

# Core translation package for the Morse Translator

# Contains the primary Morse Code translation engine, English-to-Morse
# encoding, Morse-to-English decoding, Morse Code mappings, and
# translation result data models

# Modules
# translator - High-level translation interface
# encoder - English-to-Morse Code encoding
# decoder - Morse-to-English Code decoding
# morse_code - Morse Code character mappings and lookup utilities
# translation - Translation result and metadata model

from .translator import (
    MorseTranslator,
)

from .encoder import (
    encode,
    encode_character,
    encode_word,
)

from .decoder import (
    decode,
    decode_character,
    decode_word,
)

from .morse_code import (
    ENGLISH_TO_MORSE,
    MORSE_TO_ENGLISH,
    get_morse_code,
    get_english_character,
    is_supported_character,
    is_valid_morse_sequence,
    )

from .translation import (
    Translation,
    TranslationDirection,
)

__all__ = [
    # Translator
    "MorseTranslator",
    # Encoder
    "encode",
    "encode_character",
    "encode_word",
    # Decoder
    "decode",
    "decode_character",
    "decode_word",
    # Morse Code
    "ENGLISH_TO_MORSE",
    "MORSE_TO_ENGLISH",
    "get_morse_code",
    "get_english_character",
    "is_supported_character",
    "is_valid_morse_sequence",
    # Translation
    "Translation",
    "TranslationDirection",
]

