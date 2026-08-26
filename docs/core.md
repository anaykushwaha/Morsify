````markdown
# Core Package Documentation

## Overview

The `core/` package contains the central Morse Code translation engine used throughout the Morse Translator project.

It provides the project's standard International Morse Code mappings, English-to-Morse encoding, Morse-to-English decoding, translation result models, translation direction definitions, and the high-level `MorseTranslator` interface.

The package is intentionally independent from the user interface, command-line interface, history management, validation framework, utilities, and automated tests.

The purpose of the `core/` package is to provide a clean and reusable translation foundation that other parts of the application can build upon.

```text
core/
│
├── __init__.py
├── morse_code.py
├── translation.py
├── encoder.py
├── decoder.py
└── translator.py
````

# Package Responsibilities

The `core/` package is responsible for:

* Providing the standard Morse Code mappings.
* Converting individual English characters into Morse Code.
* Converting individual Morse Code sequences into English characters.
* Encoding complete English words.
* Encoding complete English text.
* Decoding complete Morse Code words.
* Decoding complete Morse Code text.
* Handling Morse Code character and word separators.
* Representing translation directions.
* Representing completed translation results.
* Recording translation timestamps.
* Providing a high-level translation interface.
* Providing convenient English-to-Morse and Morse-to-English functions.
* Providing reusable translation functionality to the rest of the application.

The package does **not** handle:

* User interface rendering.
* Command-line menus.
* User prompts.
* Persistent translation history.
* File management.
* Application configuration.
* Logging.
* Automated test execution.
* GUI-specific validation.
* Application-level error presentation.

Those responsibilities belong to other packages in the project.

# Module Structure

## `__init__.py`

The package initializer provides the public interface for the `core/` package.

It imports and exposes the most important functionality from the individual core modules so that other parts of the project can access the translation engine without needing to know the internal organization of the package.

The initializer exposes functionality from:

* `morse_code`
* `translation`
* `encoder`
* `decoder`
* `translator`

The initializer also defines `__all__` to explicitly identify the public API of the package.

### Purpose

The initializer allows higher-level code to use the core translation system through a centralized interface.

For example:

```python
from core import (
    MorseTranslator,
    encode,
    decode,
)
```

rather than requiring the caller to import every component from its individual module.

### Public Components

The package initializer exposes:

* Morse Code mappings.
* Morse Code lookup functions.
* Translation models.
* Encoding functions.
* Decoding functions.
* Morse input normalization.
* The `MorseTranslator` class.
* Translation convenience functions.

# `morse_code.py`

`morse_code.py` contains the standard International Morse Code mappings and low-level lookup utilities used by the translation engine.

This module acts as the foundational reference for the encoding and decoding systems.

It does not perform complete sentence translation. Instead, it provides the character-level mappings and validation utilities required by `encoder.py` and `decoder.py`.

## Morse Code Mappings

### `ENGLISH_TO_MORSE`

`ENGLISH_TO_MORSE` is the primary mapping between supported English characters and their Morse Code representations.

The mapping contains:

* Uppercase English letters.
* Numerical digits.
* Common punctuation characters.

Examples include:

```text
A → .-
B → -...
C → -.-.
E → .
S → ...
0 → -----
1 → .----
```

The mapping is used primarily when converting English characters into Morse Code.

### `MORSE_TO_ENGLISH`

`MORSE_TO_ENGLISH` is the reverse mapping of `ENGLISH_TO_MORSE`.

It allows Morse Code sequences to be converted back into their corresponding English characters.

For example:

```text
.-    → A
-...  → B
...   → S
```

The reverse mapping is automatically generated from `ENGLISH_TO_MORSE` so that the two mappings remain consistent.

## Lookup Functions

### `get_morse_code()`

`get_morse_code()` returns the Morse Code representation of a single supported character.

The function:

* Requires exactly one character.
* Normalizes alphabetic characters to uppercase.
* Looks up the character in `ENGLISH_TO_MORSE`.
* Raises an error when the supplied character is invalid or unsupported.

Example:

```python
from core.morse_code import get_morse_code

result = get_morse_code("A")

print(result)
```

Output:

```text
.-
```

### `get_english_character()`

`get_english_character()` performs the reverse lookup.

It accepts a Morse Code sequence and returns the corresponding English character.

Example:

```python
from core.morse_code import get_english_character

result = get_english_character("...")

print(result)
```

Output:

```text
S
```

## Character Validation

### `is_supported_character()`

`is_supported_character()` determines whether an individual character is supported by the translator.

It accepts:

* English letters.
* Supported numbers.
* Supported punctuation.

The function returns a Boolean value rather than raising an exception.

Example:

```python
from core.morse_code import is_supported_character

print(is_supported_character("A"))
print(is_supported_character("#"))
```

### `is_valid_morse_sequence()`

`is_valid_morse_sequence()` determines whether a Morse Code sequence represents a valid supported character.

A valid sequence:

* Must be a string.
* Must not be empty.
* Must contain only `.` and `-`.
* Must exist in `MORSE_TO_ENGLISH`.

Example:

```python
from core.morse_code import is_valid_morse_sequence

print(is_valid_morse_sequence("..."))
print(is_valid_morse_sequence("abc"))
```

## Design Goal

Keeping Morse Code mappings and character-level lookup functionality in one module prevents the encoder and decoder from duplicating the same mapping data.

The module therefore acts as the shared reference layer for the entire translation engine.

# `translation.py`

`translation.py` contains the data models used to represent completed translations.

Rather than returning only a translated string, the project can represent a translation as a structured object containing the original input, translated output, direction, and timestamp.

## `TranslationDirection`

`TranslationDirection` is an enumeration representing the two supported translation directions.

The available values are:

* `ENGLISH_TO_MORSE`
* `MORSE_TO_ENGLISH`

Example:

```python
from core.translation import TranslationDirection

direction = TranslationDirection.ENGLISH_TO_MORSE
```

Using an enumeration instead of arbitrary strings provides a consistent representation throughout the application.

## `Translation`

`Translation` is a dataclass representing a completed translation.

It contains:

* `original_text`
* `translated_text`
* `direction`
* `timestamp`

Example conceptual representation:

```text
Translation
│
├── Original Text
│   └── HELLO
│
├── Translated Text
│   └── .... . .-.. .-.. ---
│
├── Direction
│   └── English → Morse
│
└── Timestamp
    └── Date and time of translation
```

### `__post_init__()`

The `__post_init__()` method validates the types of the fields supplied to a `Translation` object.

It ensures that:

* `original_text` is a string.
* `translated_text` is a string.
* `direction` is a `TranslationDirection`.
* `timestamp` is a `datetime`.

### `is_english_to_morse()`

Determines whether the translation represents an English-to-Morse operation.

### `is_morse_to_english()`

Determines whether the translation represents a Morse-to-English operation.

### `direction_name()`

Returns the human-readable name of the translation direction.

For example:

```text
English → Morse
```

### `to_dict()`

Converts the translation object into a dictionary.

This provides a convenient representation for future history and serialization functionality.

The resulting structure contains:

```text
original_text
translated_text
direction
timestamp
```

## `create_translation()`

`create_translation()` is a factory function that creates a `Translation` object using the current date and time.

This allows the translation engine to create completed translation records without requiring every caller to manually construct a timestamp.

## Design Goal

The translation model separates the concept of a **translation result** from the actual translation algorithm.

The encoder and decoder perform transformations.

The `Translation` model represents the result of those transformations.

This separation becomes particularly useful for the history package later in the project.

# `encoder.py`

`encoder.py` contains the English-to-Morse Code encoding functionality.

It builds on the character mappings provided by `morse_code.py` and provides multiple levels of encoding.

The module supports:

* Individual character encoding.
* Word encoding.
* Complete text encoding.
* Lists of characters.
* Lists of words.

## Morse Separators

The module defines two separators.

### `MORSE_CHARACTER_SEPARATOR`

This is a single space:

```text
" "
```

It separates individual Morse Code characters.

For example:

```text
.... . .-.. .-.. ---
```

represents:

```text
H E L L O
```

### `MORSE_WORD_SEPARATOR`

This is:

```text
" / "
```

It separates words.

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

represents:

```text
HELLO WORLD
```

## `encode_character()`

`encode_character()` converts one supported English character into Morse Code.

Example:

```python
from core.encoder import encode_character

result = encode_character("A")

print(result)
```

Output:

```text
.-
```

The function validates that:

* The input is a string.
* Exactly one character is supplied.
* The character is not a space.
* The character is supported by the Morse Code mapping.

## `encode_word()`

`encode_word()` converts an individual English word into Morse Code.

Example:

```python
from core.encoder import encode_word

result = encode_word("HELLO")

print(result)
```

Output:

```text
.... . .-.. .-.. ---
```

Individual Morse characters are separated by spaces.

## `encode()`

`encode()` is the primary English-to-Morse text encoding function.

It accepts complete English text and:

1. Normalizes whitespace.
2. Separates the text into words.
3. Encodes each word.
4. Separates encoded words using `/`.

Example:

```python
from core.encoder import encode

result = encode("HELLO WORLD")

print(result)
```

Output:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## `encode_characters()`

`encode_characters()` accepts a list of individual characters and converts them into Morse Code.

Example:

```python
from core.encoder import encode_characters

result = encode_characters(
    ["H", "E", "L", "L", "O"]
)
```

The characters are encoded individually and joined using the Morse character separator.

## `encode_words()`

`encode_words()` accepts a list of words and encodes each word into Morse Code.

The resulting words are separated using the Morse word separator.

## Design Goal

The encoder is structured in multiple layers rather than placing all translation logic inside one function.

The structure is:

```text
encode()
   │
   ├── encode_word()
   │       │
   │       └── encode_character()
   │
   └── encode_word()
           │
           └── encode_character()
```

This allows each operation to be reused independently.

# `decoder.py`

`decoder.py` contains the reverse translation system for converting Morse Code into English.

It mirrors the architecture of `encoder.py`.

The module supports:

* Individual Morse character decoding.
* Morse word decoding.
* Complete Morse text decoding.
* Lists of Morse sequences.
* Lists of Morse words.
* Morse input normalization.

## Morse Separators

The decoder recognizes:

```text
Space → Morse character separator
/     → Morse word separator
```

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

is interpreted as:

```text
HELLO WORLD
```

## `decode_character()`

`decode_character()` converts one valid Morse Code sequence into an English character.

Example:

```python
from core.decoder import decode_character

result = decode_character("....")

print(result)
```

Output:

```text
H
```

The function verifies that the supplied sequence represents a valid supported Morse Code character.

## `decode_word()`

`decode_word()` converts a single Morse Code word into English.

Example:

```python
from core.decoder import decode_word

result = decode_word(
    ".... . .-.. .-.. ---"
)

print(result)
```

Output:

```text
HELLO
```

## `decode()`

`decode()` is the primary Morse-to-English translation function.

It:

1. Validates the input type.
2. Removes unnecessary surrounding whitespace.
3. Normalizes repeated whitespace.
4. Separates Morse words.
5. Decodes each Morse word.
6. Reconstructs the English text.

Example:

```python
from core.decoder import decode

result = decode(
    ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
)

print(result)
```

Output:

```text
HELLO WORLD
```

## `decode_characters()`

`decode_characters()` accepts a list of Morse Code sequences and converts them into English characters.

For example:

```python
from core.decoder import decode_characters

result = decode_characters(
    [
        "....",
        ".",
        ".-..",
        ".-..",
        "---",
    ]
)
```

The result is:

```text
HELLO
```

## `decode_words()`

`decode_words()` accepts a list of Morse Code words and converts them into English words.

The resulting English words are joined with spaces.

## `normalize_morse_input()`

`normalize_morse_input()` normalizes Morse Code whitespace.

Its purpose is to make the decoder more tolerant of inconsistent whitespace while preserving the meaning of Morse character and word separators.

## Design Goal

The decoder mirrors the encoder so that the two systems remain conceptually consistent.

```text
Encoder

English
   │
   ▼
Words
   │
   ▼
Characters
   │
   ▼
Morse Code
```

The decoder reverses this process:

```text
Decoder

Morse Code
   │
   ▼
Characters
   │
   ▼
Words
   │
   ▼
English
```

This symmetry makes the translation engine easier to understand, test, and maintain.

# `translator.py`

`translator.py` provides the high-level interface for the entire core translation engine.

It coordinates:

* `encoder.py`
* `decoder.py`
* `translation.py`

Rather than requiring other parts of the project to manually select an encoder or decoder, they can use `MorseTranslator`.

## `MorseTranslator`

`MorseTranslator` is the primary high-level translation class.

It provides a unified interface for both translation directions.

### `translate()`

`translate()` performs a translation based on a supplied `TranslationDirection`.

For English-to-Morse:

```text
TranslationDirection.ENGLISH_TO_MORSE
```

the method calls the encoder.

For Morse-to-English:

```text
TranslationDirection.MORSE_TO_ENGLISH
```

the method calls the decoder.

The method then creates and returns a `Translation` object.

Conceptually:

```text
Input
  │
  ▼
Translation Direction
  │
  ├───────────────┐
  │               │
  ▼               ▼
Encoder         Decoder
  │               │
  └───────┬───────┘
          │
          ▼
   Translation Object
```

### `to_morse()`

`to_morse()` provides a convenient English-to-Morse interface.

Example:

```python
translator = MorseTranslator()

result = translator.to_morse("HELLO")
```

The result is a `Translation` object.

### `to_english()`

`to_english()` provides a convenient Morse-to-English interface.

Example:

```python
translator = MorseTranslator()

result = translator.to_english(
    ".... . .-.. .-.. ---"
)
```

The result is a `Translation` object.

## String Convenience Functions

### `translate_to_morse()`

`translate_to_morse()` provides a simple function for English-to-Morse translation when the caller only needs the translated string.

Example:

```python
from core.translator import translate_to_morse

result = translate_to_morse("HELLO")

print(result)
```

Output:

```text
.... . .-.. .-.. ---
```

### `translate_to_english()`

`translate_to_english()` provides the equivalent convenience function for Morse-to-English translation.

Example:

```python
from core.translator import translate_to_english

result = translate_to_english(
    "... --- ..."
)

print(result)
```

Output:

```text
SOS
```

## Direction Helpers

The `MorseTranslator` class also provides helper methods for determining the requested translation direction.

### `is_english_to_morse()`

Determines whether a direction represents English-to-Morse translation.

### `is_morse_to_english()`

Determines whether a direction represents Morse-to-English translation.

## Design Goal

`translator.py` acts as the public orchestration layer of the core package.

It does not reimplement encoding or decoding logic.

Instead, it coordinates existing components:

```text
translator.py
      │
      ├──────────────► encoder.py
      │
      ├──────────────► decoder.py
      │
      └──────────────► translation.py
```

This keeps the individual modules focused while giving the rest of the application a simple interface.

# Core Architecture

The `core/` package follows a layered architecture.

```text
                         core/
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
       morse_code.py              translation.py
             │                           │
             │                           │
       ┌─────┴─────┐                     │
       │           │                     │
       ▼           ▼                     │
   encoder.py   decoder.py               │
       │           │                     │
       └─────┬─────┘                     │
             │                           │
             └───────────┬───────────────┘
                         │
                         ▼
                  translator.py
                         │
                         ▼
                 Rest of Application
```

The architecture separates:

```text
Morse Code Data
      │
      ▼
Character Operations
      │
      ▼
Text Translation
      │
      ▼
Translation Results
      │
      ▼
High-Level Interface
```

Each layer has a specific responsibility.

# Core Processing Flow

## English-to-Morse

A typical English-to-Morse operation follows this process:

```text
English Input
      │
      ▼
MorseTranslator
      │
      ▼
encode()
      │
      ▼
encode_word()
      │
      ▼
encode_character()
      │
      ▼
get_morse_code()
      │
      ▼
Morse Code Mapping
      │
      ▼
Encoded Morse Text
      │
      ▼
Translation Object
```

For example:

```text
HELLO
```

becomes:

```text
H → ....
E → .
L → .-..
L → .-..
O → ---
```

which produces:

```text
.... . .-.. .-.. ---
```

## Morse-to-English

A Morse-to-English operation follows the reverse process:

```text
Morse Input
      │
      ▼
MorseTranslator
      │
      ▼
decode()
      │
      ▼
decode_word()
      │
      ▼
decode_character()
      │
      ▼
get_english_character()
      │
      ▼
Morse Code Mapping
      │
      ▼
English Text
      │
      ▼
Translation Object
```

# Relationship Between Core Modules

The modules have a clear division of responsibilities.

```text
morse_code.py
    │
    ├── Character mappings
    ├── Character lookup
    └── Morse sequence validation
             │
             ├───────────────┐
             ▼               ▼
        encoder.py       decoder.py
             │               │
             └───────┬───────┘
                     ▼
              translator.py
                     │
                     ▼
              translation.py
```

The encoder and decoder depend on the Morse mappings.

The translator depends on the encoder and decoder.

The translator also creates `Translation` objects.

Higher-level application packages depend on the core package rather than the core package depending on those application packages.

# Relationship With Other Packages

The `core/` package is the foundation of the Morse Translator project.

Other packages can build on the translation functionality provided here.

A simplified project architecture is:

```text
                    Morse Translator
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
           core       validation      history
             │             │             │
             │             │             │
             └─────────────┼─────────────┘
                           │
                    Application Layer
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
             interface             utils
                 │
                 ▼
               tests
```

## `validation/`

The validation package can use core functionality to determine whether text can be safely processed by the translation engine.

The core package should remain independent of application-level validation.

## `history/`

The history package can use the `Translation` model to store completed translations.

For example:

```text
Translation
     │
     ▼
History Manager
     │
     ▼
Stored Translation History
```

## `interface/`

The interface package will provide the user-facing interaction layer.

It can call the high-level translation functions without needing to know the internal details of the encoder and decoder.

## `utils/`

Utility functionality can support the rest of the application without becoming part of the translation engine itself.

## `tests/`

The testing package can test individual core modules as well as complete translation workflows.

# Design Principles

## Separation of Concerns

Each core module has a focused responsibility.

```text
morse_code.py   → Morse Code mappings and lookup
translation.py  → Translation data models
encoder.py      → English-to-Morse conversion
decoder.py      → Morse-to-English conversion
translator.py   → High-level orchestration
```

No single module is responsible for the entire application.

## Reusability

The core translation functions are designed to be reusable by multiple parts of the project.

The same encoding operation can eventually be used by:

* A command-line interface.
* A graphical interface.
* History functionality.
* Automated tests.
* Utility functions.
* Future application components.

## Modularity

The encoder, decoder, mappings, and translation model are separated into individual modules.

This makes it possible to modify one component without unnecessarily changing the others.

For example, changes to the Morse Code mapping system should not require rewriting the high-level translator.

## Composability

The high-level translator is composed from lower-level components.

```text
MorseTranslator
      │
      ├── Encoder
      │
      ├── Decoder
      │
      └── Translation Model
```

Each component performs one part of the overall process.

## Testability

The core functions are designed so that individual behaviors can be tested independently.

Testing can occur at multiple levels:

```text
Character Level
      │
      ▼
Word Level
      │
      ▼
Text Level
      │
      ▼
Translation Level
      │
      ▼
Complete Workflow
```

This allows failures to be isolated more easily.

# Error Handling

The core package performs low-level validation necessary to protect its own functions.

Examples include:

* Confirming that text values are strings.
* Confirming that individual characters contain exactly one character.
* Confirming that Morse sequences are not empty.
* Confirming that characters are supported.
* Confirming that Morse sequences are valid.
* Confirming that translation directions use `TranslationDirection`.
* Confirming that translation timestamps use `datetime`.

The core package raises Python exceptions when invalid low-level data is supplied.

Higher-level packages such as `validation/` can provide more user-friendly validation and error reporting before calling the core translation engine.

This creates a distinction between:

```text
Application Validation
        │
        ▼
User-friendly input checking
        │
        ▼
Core Validation
        │
        ▼
Protection of translation functions
```

# Public API

The `core/` package exposes the following major functionality through `__init__.py`.

## Morse Code

```python
ENGLISH_TO_MORSE
MORSE_TO_ENGLISH
get_morse_code
get_english_character
is_supported_character
is_valid_morse_sequence
```

## Translation Models

```python
Translation
TranslationDirection
create_translation
```

## Encoding

```python
encode
encode_character
encode_word
encode_characters
encode_words
```

## Decoding

```python
decode
decode_character
decode_word
decode_characters
decode_words
normalize_morse_input
```

## High-Level Translation

```python
MorseTranslator
translate_to_morse
translate_to_english
```

# Example Usage

## Using the High-Level Translator

```python
from core import MorseTranslator

translator = MorseTranslator()

result = translator.to_morse("HELLO WORLD")

print(result.translated_text)
```

Output:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

The returned `Translation` object also contains:

```python
result.original_text
result.translated_text
result.direction
result.timestamp
```

## Translating Morse Code to English

```python
from core import MorseTranslator

translator = MorseTranslator()

result = translator.to_english(
    ".... . .-.. .-.. ---"
)

print(result.translated_text)
```

Output:

```text
HELLO
```

## Using the Encoder Directly

```python
from core import encode

result = encode("HELLO")

print(result)
```

Output:

```text
.... . .-.. .-.. ---
```

## Using the Decoder Directly

```python
from core import decode

result = decode(
    ".... . .-.. .-.. ---"
)

print(result)
```

Output:

```text
HELLO
```

## Using Character-Level Functions

```python
from core import (
    encode_character,
    decode_character,
)

morse = encode_character("S")

character = decode_character("...")

print(morse)
print(character)
```

Output:

```text
...
S
```

# Translation Result Lifecycle

A complete translation can be viewed as a lifecycle:

```text
User Input
    │
    ▼
Translation Request
    │
    ▼
Direction Selection
    │
    ├───────────────┐
    ▼               ▼
English → Morse   Morse → English
    │               │
    ▼               ▼
  Encoder         Decoder
    │               │
    └───────┬───────┘
            ▼
    Translated Text
            │
            ▼
    Translation Object
            │
            ├── Original Text
            ├── Translated Text
            ├── Direction
            └── Timestamp
```

This model allows the translation result to be passed to other packages without losing information about how the result was produced.

# Module Dependency Guidelines

The core package should maintain a simple dependency direction.

```text
morse_code.py
      │
      ├───────────────┐
      ▼               ▼
 encoder.py       decoder.py
      │               │
      └───────┬───────┘
              │
              ▼
        translator.py
              │
              ▼
       Translation Model
```

The goal is to avoid circular dependencies.

The mapping module should remain low-level.

The encoder and decoder should use the mapping system rather than redefining mappings.

The high-level translator should coordinate the lower-level operations rather than duplicating their logic.

Higher-level application packages should depend on `core`, not the other way around.

# Extending the Core Package

Future core functionality should be added only when it represents a fundamental translation-engine responsibility.

For example, a future feature could add support for another Morse Code standard or additional translation behavior.

A new module should ideally:

1. Have one clearly defined responsibility.
2. Reuse existing Morse Code mappings where appropriate.
3. Follow the project's formatting conventions.
4. Use type hints.
5. Validate its inputs.
6. Define `__all__` for its public API when appropriate.
7. Be exposed through `core/__init__.py` if it is part of the public API.
8. Be tested in the `tests/` package.
9. Be documented in `docs/core.md`.

New functionality should not be placed in `core/` simply because it is convenient.

For example, GUI rendering should remain in the interface package rather than being added to the core translation engine.

# Future Expansion

The current core package focuses on the fundamental English ↔ Morse Code translation system.

Potential future expansion could include:

* Additional supported Morse Code characters.
* International Morse Code extensions.
* Additional formatting utilities.
* More advanced translation metadata.
* Translation statistics.
* Alternative Morse Code representations.
* More flexible separator handling.
* Additional translation result information.

Any future expansion should preserve the separation between translation logic and application-level functionality.

# Core Testing Strategy

The core package should eventually be tested at multiple levels.

## Mapping Tests

The Morse Code mapping system should verify:

* Known character mappings.
* Reverse mappings.
* Supported characters.
* Invalid characters.
* Valid Morse sequences.
* Invalid Morse sequences.

## Encoder Tests

The encoder should verify:

* Individual characters.
* Complete words.
* Complete sentences.
* Numbers.
* Supported punctuation.
* Multiple words.
* Whitespace normalization.
* Unsupported characters.

## Decoder Tests

The decoder should verify:

* Individual Morse sequences.
* Complete Morse words.
* Complete Morse sentences.
* Word separators.
* Character separators.
* Whitespace normalization.
* Invalid Morse sequences.

## Translation Model Tests

The translation model should verify:

* Correct original text.
* Correct translated text.
* Correct translation direction.
* Correct timestamps.
* Dictionary conversion.
* Direction helper methods.

## Translator Tests

The high-level translator should verify:

* English-to-Morse translation.
* Morse-to-English translation.
* Correct `Translation` objects.
* Correct convenience functions.
* Correct direction handling.

The formal tests will be implemented in the project's `tests/` package rather than inside `core/`.

# Core Package Design Philosophy

The core package follows a simple principle:

```text
Keep the translation engine focused.
```

The package should know:

```text
How Morse Code works
How to encode English
How to decode Morse Code
How to represent a translation
How to coordinate those operations
```

It should not need to know:

```text
How the user interacts with the application
Where translation history is stored
How the GUI looks
How command-line menus work
How files are managed
How errors are displayed to users
```

This keeps the core translation engine reusable across different interfaces.

# Summary

The `core/` package forms the **central translation engine** of the Morse Translator project.

Its architecture is built around five major responsibilities:

```text
Morse Code Mappings
        │
        ▼
Character-Level Operations
        │
        ├───────────────┐
        ▼               ▼
    Encoding         Decoding
        │               │
        └───────┬───────┘
                ▼
       Translation Model
                │
                ▼
       High-Level Translator
```

The package currently consists of:

```text
core/
│
├── __init__.py
│
├── morse_code.py
│
├── translation.py
│
├── encoder.py
│
├── decoder.py
│
└── translator.py
```

Each module has a focused responsibility:

```text
__init__.py
    → Public package API

morse_code.py
    → Morse Code mappings and lookup

translation.py
    → Translation result models

encoder.py
    → English-to-Morse conversion

decoder.py
    → Morse-to-English conversion

translator.py
    → High-level translation orchestration
```

This structure gives the project a stable foundation for the remaining packages.

The `core/` package is intentionally independent from user interfaces, history, utilities, validation workflows, and testing infrastructure. Those systems can build on top of the core translation engine without modifying the fundamental Morse Code algorithms.

The result is a translation system that is **modular, reusable, testable, understandable, and easy to extend** as the Morse Translator project grows.

```
```
