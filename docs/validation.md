# Validation Package Documentation

## Overview

The `validation/` package contains the input validation system used throughout the Morse Translator.

It provides general-purpose validation utilities, English text validation, Morse Code validation, input normalization, validation error reporting, and structured validation result objects.

The package is designed to ensure that invalid or unsupported input is detected before it reaches the translation engine.

The validation layer sits between user/application input and the core translation components.

```text
validation/

│
├── __init__.py
├── validator.py
├── english_validator.py
├── morse_validator.py
└── validation_result.py
```

# Package Responsibilities

The `validation/` package is responsible for:

* Validating general input types.

* Detecting empty or whitespace-only input.

* Validating individual characters.

* Validating input lengths.

* Normalizing whitespace.

* Validating English text.

* Detecting unsupported English characters.

* Validating Morse Code symbols.

* Validating Morse Code character sequences.

* Validating Morse Code words and complete messages.

* Detecting invalid Morse Code sequences.

* Validating Morse Code separators.

* Providing structured validation results.

* Providing descriptive validation errors.

* Providing validation summaries for interface and debugging components.

The package does **not** handle:

* Morse Code encoding.

* Morse Code decoding.

* Translation logic.

* User interface rendering.

* Command-line menus.

* File management.

* Application configuration.

* Persistent translation history.

Those responsibilities belong to other packages in the project.

# Module Structure

## `__init__.py`

The package initializer exposes the public validation functionality to the rest of the Morse Translator.

It provides a centralized interface for importing commonly used validation functions, constants, and result models.

The initializer exposes functionality from:

* `validator`

* `english_validator`

* `morse_validator`

* `validation_result`

### Purpose

The initializer allows higher-level components to access validation functionality without needing to know the internal organization of the package.

For example:

```python
from validation import (
    validate_english_text,
    validate_morse_text,
    ValidationResult,
)
```

This keeps imports clean and provides a consistent public API.

# `validator.py`

`validator.py` contains the general-purpose validation utilities used throughout the validation package.

It is intentionally independent from Morse Code and English-specific rules.

The module provides reusable functionality that can be used by both specialized validators and future validation components.

## General Type Validation

### `is_string()`

Determines whether a supplied value is a Python string.

```python
is_string("Hello")
```

returns:

```text
True
```

while:

```python
is_string(123)
```

returns:

```text
False
```

### `is_non_empty_string()`

Determines whether a value is a string containing meaningful content.

Whitespace-only strings are considered empty.

### `is_empty_string()`

Determines whether a string is empty or contains only whitespace.

### `is_none_or_empty()`

Checks whether a value is:

* `None`.

* An empty string.

* A whitespace-only string.

## Text Normalization

### `normalize_text()`

Normalizes general text by:

* Removing leading whitespace.

* Removing trailing whitespace.

* Collapsing repeated internal whitespace.

For example:

```text
"   Hello     World   "
```

becomes:

```text
"Hello World"
```

### `normalize_whitespace()`

Removes leading and trailing whitespace while preserving the internal whitespace structure.

This distinction is useful because some parts of the translator may need to preserve internal formatting.

# Length Validation

## `is_within_length()`

Determines whether a string falls within an optional minimum and maximum length.

The function supports:

* Minimum length.

* Maximum length.

* Both minimum and maximum values.

## `validate_length()`

Performs the same validation while raising a `ValueError` when the supplied string violates the configured length limits.

This allows higher-level code to choose between:

```python
if is_within_length(text, minimum=1):
    ...
```

and:

```python
validate_length(text, minimum=1)
```

depending on the required error-handling style.

# Character Validation

## `is_single_character()`

Determines whether a value is a string containing exactly one character.

## `is_whitespace_character()`

Determines whether a value is a single whitespace character.

These utilities are useful when validating individual characters before applying more specialized rules.

# Collection Validation

## `is_list()`

Determines whether a value is a Python list.

## `is_non_empty_list()`

Determines whether a value is a list containing at least one element.

These functions provide basic collection validation for components that may eventually process lists of characters, words, validation errors, or translation results.

# Generic Validation

## `validate_string()`

Validates that a value is a string.

By default, empty strings are rejected.

The `allow_empty` parameter can be used when empty strings are acceptable.

## `validate_character()`

Validates that a value is a string containing exactly one character.

It raises a `ValueError` when the supplied value is not a valid single-character string.

# Validation Error Helpers

## `get_string_error()`

Returns a descriptive error message when a general string is invalid.

If the string is valid, it returns `None`.

## `get_character_error()`

Returns a descriptive error message when a single-character value is invalid.

If the character is valid, it returns `None`.

# Design Goal

The primary design goal of `validator.py` is **reusability**.

Instead of duplicating basic checks inside every specialized validator, common functionality is centralized here.

```text
Generic Validation
        │
        ├── Type checks
        ├── Empty checks
        ├── Length checks
        ├── Character checks
        └── Normalization
                │
                ▼
       Specialized Validators
```

# `english_validator.py`

`english_validator.py` contains validation logic specifically designed for English input intended for English-to-Morse translation.

It determines whether characters and complete pieces of text are supported by the translator.

The module uses the canonical Morse mappings from `core/morse_code.py` rather than maintaining a second independent list of supported characters.

# English Character Validation

## `is_english_letter()`

Determines whether a character is an English alphabetic character.

Both uppercase and lowercase English letters are accepted.

For example:

```text
A → True
Z → True
a → True
z → True
```

Non-English alphabetic characters are not accepted.

## `is_english_digit()`

Determines whether a character is an ASCII numerical digit.

The supported digits are:

```text
0 1 2 3 4 5 6 7 8 9
```

## `is_supported_punctuation()`

Determines whether a punctuation character exists in the translator's Morse Code mapping.

Supported punctuation is determined by `core.morse_code.ENGLISH_TO_MORSE`.

## `is_supported_english_character()`

Determines whether a character can be processed by the English-to-Morse translation system.

Letters, digits, supported punctuation, and whitespace can be accepted.

# Unsupported Character Detection

## `get_unsupported_characters()`

Returns all unique unsupported characters found in an English string.

The order in which unsupported characters first appear is preserved.

For example:

```text
Hello # World %
```

could produce:

```text
['#', '%']
```

rather than returning duplicate occurrences of the same character.

## `has_unsupported_characters()`

Provides a convenient boolean check for determining whether unsupported characters exist.

# English Text Validation

## `is_valid_english_text()`

Determines whether complete English text can be processed by the translator.

The function checks:

* Correct input type.

* Empty input.

* Supported characters.

* Whitespace.

* Supported punctuation.

* Numbers.

It returns a boolean rather than raising an exception.

## `validate_english_text()`

Performs full English input validation.

Unlike `is_valid_english_text()`, this function raises a `ValueError` when validation fails.

For example:

```python
validate_english_text("Hello World")
```

is valid.

An input containing unsupported characters produces a descriptive error.

# English Text Normalization

## `normalize_english_text()`

Normalizes English text before translation.

It removes unnecessary leading and trailing whitespace and collapses repeated internal whitespace.

For example:

```text
"   Hello     World   "
```

becomes:

```text
"Hello World"
```

This gives the translation engine a predictable input format.

# Character Classification

## `get_character_type()`

Classifies supported characters into categories.

Possible results include:

```text
letter
digit
punctuation
whitespace
```

Unsupported characters return:

```text
None
```

This classification is useful for statistics, validation summaries, and interface components.

## `is_letter_only()`

Determines whether a string contains only English letters.

## `is_numeric_only()`

Determines whether a string contains only ASCII digits.

# Word Validation

## `get_words()`

Splits English text into individual words using whitespace as the separator.

## `validate_words()`

Validates every word in a piece of English text.

If an unsupported character appears inside a word, the function raises a descriptive `ValueError`.

# Validation Error Reporting

## `get_english_validation_error()`

Returns a human-readable validation error for English text.

If the input is valid, it returns:

```text
None
```

This makes it useful for interfaces that want to display an error without using exception handling.

# English Validation Summary

## `english_text_summary()`

Returns structured information about the supplied English text.

The summary includes information such as:

* Whether the text is valid.

* Text length.

* Word count.

* Letter count.

* Digit count.

* Punctuation count.

* Whitespace count.

* Unsupported characters.

* Validation error.

This information can later be used by the GUI, CLI, testing system, or debugging tools.

# `morse_validator.py`

`morse_validator.py` contains validation logic specifically designed for Morse Code input.

It validates both individual Morse sequences and complete Morse messages.

The module does **not** decode Morse Code.

Its responsibility is only to determine whether Morse Code input is valid and properly formatted.

# Morse Code Separators

The module defines two primary separator constants.

## `MORSE_CHARACTER_SEPARATOR`

```text
" "
```

A space separates individual Morse Code characters.

For example:

```text
.... . .-.. .-.. ---
```

represents:

```text
H E L L O
```

## `MORSE_WORD_SEPARATOR`

```text
"/"
```

A forward slash separates words.

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

represents:

```text
HELLO WORLD
```

## `VALID_MORSE_SYMBOLS`

Defines the symbols allowed inside a Morse Code sequence:

```text
.
-
```

# Morse Symbol Validation

## `is_morse_symbol()`

Determines whether a value is a valid individual Morse Code symbol.

The only valid symbols are:

```text
.
-
```

## `is_morse_sequence()`

Determines whether a sequence contains only dots and dashes.

For example:

```text
"..."
```

and:

```text
".-"
```

are structurally valid sequences.

However, structural validity does not necessarily mean that the sequence corresponds to a supported Morse Code character.

# Character Sequence Validation

## `is_valid_character_sequence()`

Determines whether a Morse Code sequence:

1. Contains only dots and dashes.

2. Exists in the project's Morse Code mapping.

For example:

```text
".-"
```

is valid because it represents `A`.

An unknown sequence is rejected even if it contains only valid Morse symbols.

# Morse Word Validation

## `split_morse_word()`

Splits a Morse Code word into individual character sequences.

For example:

```text
"... --- ..."
```

becomes:

```text
[
    "...",
    "---",
    "..."
]
```

## `is_valid_morse_word()`

Determines whether every Morse Code character sequence within a word is valid.

## `get_invalid_sequences()`

Returns unique invalid Morse sequences found inside a Morse Code word.

# Morse Text Validation

## `split_morse_text()`

Splits complete Morse Code input into Morse words using `/` as the word separator.

For example:

```text
"... --- ... / .... . .-.. .-.. ---"
```

becomes separate Morse words representing:

```text
SOS
HELLO
```

## `is_valid_morse_text()`

Determines whether an entire Morse Code message is valid.

It checks:

* Input type.

* Empty input.

* Morse symbols.

* Morse character sequences.

* Word separators.

* Supported Morse mappings.

## `validate_morse_text()`

Performs full Morse Code validation and raises a `ValueError` if invalid sequences are found.

# Invalid Sequence Detection

## `get_invalid_sequences_from_text()`

Searches an entire Morse message for invalid sequences.

The function returns unique invalid sequences while preserving their order of appearance.

## `has_invalid_sequences()`

Provides a boolean check for whether invalid Morse sequences exist.

# Morse Input Normalization

## `normalize_morse_text()`

Normalizes Morse Code input while preserving its logical structure.

The function can clean unnecessary whitespace around Morse characters and word separators.

For example:

```text
"...   ---   ... /   .... ."
```

can be normalized into a consistent representation.

## `normalize_morse_word()`

Normalizes whitespace inside an individual Morse word.

# Separator Validation

## `has_valid_separators()`

Checks whether Morse word separators are positioned correctly.

Invalid structures include:

```text
/ .... . .-.. .-.. ---
```

and:

```text
.... . .-.. .-.. --- /
```

as well as:

```text
.... . .-.. // .-.. ---
```

The goal is to ensure that `/` represents an actual word boundary rather than malformed input.

# Morse Sequence Analysis

## `get_morse_sequence_length()`

Returns the number of dots and dashes contained in a Morse sequence.

## `get_morse_symbol_counts()`

Returns the number of dots and dashes in a sequence.

For example:

```text
".-"
```

contains:

```text
1 dot
1 dash
```

This information is primarily useful for validation summaries, testing, and future interface features.

# Morse Validation Error Reporting

## `get_morse_validation_error()`

Returns a descriptive validation error for Morse Code text.

If the input is valid, it returns:

```text
None
```

This allows user interfaces to display validation messages without requiring exception handling.

# Morse Validation Summary

## `morse_text_summary()`

Returns structured information about Morse Code input.

The summary includes:

* Whether the input is valid.

* Input length.

* Word count.

* Morse character count.

* Dot count.

* Dash count.

* Invalid sequences.

* Validation error.

This can be useful for debugging, testing, or future GUI statistics.

# `validation_result.py`

`validation_result.py` contains the structured validation result model used by the validation package.

The module provides a consistent way of representing validation outcomes.

Instead of relying exclusively on:

```python
True
```

or:

```python
False
```

validation components can return a structured object containing additional information.

# `ValidationResult`

`ValidationResult` is a dataclass containing:

```text
is_valid
message
invalid_values
metadata
```

## `is_valid`

Indicates whether validation succeeded.

```text
True
```

means validation passed.

```text
False
```

means validation failed.

## `message`

Contains a human-readable description of the validation result.

For example:

```text
"English text is valid."
```

or:

```text
"Unsupported characters detected."
```

## `invalid_values`

Contains values that caused validation to fail.

For English validation this might contain unsupported characters.

For Morse validation it might contain invalid Morse sequences.

## `metadata`

Contains additional structured information associated with the validation operation.

For example:

```python
{
    "word_count": 5,
    "character_count": 18
}
```

# Boolean Behavior

`ValidationResult` implements `__bool__()`.

This allows it to be used directly in conditional statements.

```python
result = ValidationResult.success()

if result:
    print("Validation passed.")
```

The result behaves according to its `is_valid` value.

# Result Status Methods

## `passed()`

Returns `True` when validation succeeded.

## `failed()`

Returns `True` when validation failed.

## `has_errors()`

Determines whether the result represents an error condition or contains an error message or invalid values.

# Error Information

## `error_message()`

Returns the validation error message when validation fails.

If validation succeeded, it returns:

```text
None
```

# Invalid Value Management

## `add_invalid_value()`

Adds a single invalid value to the result.

Duplicate values are not added.

## `add_invalid_values()`

Adds multiple invalid values while preventing duplicates.

## `has_invalid_values()`

Determines whether invalid values have been recorded.

# Metadata Management

## `add_metadata()`

Adds or updates a metadata value.

For example:

```python
result.add_metadata(
    "word_count",
    4,
)
```

## `get_metadata()`

Retrieves metadata associated with a key.

A default value can be provided when the key does not exist.

## `has_metadata()`

Determines whether a specific metadata key exists.

# Result Conversion

## `to_dict()`

Converts a `ValidationResult` into a standard Python dictionary.

This can be useful for:

* JSON serialization.

* Logging.

* GUI processing.

* Testing.

* Debugging.

# Result Summaries

## `summary()`

Returns a concise human-readable representation of the result.

For example:

```text
Valid: English text is valid.
```

or:

```text
Invalid: Unsupported characters detected.
```

# Result Factory Methods

## `ValidationResult.success()`

Creates a successful validation result.

```python
result = ValidationResult.success(
    message="Input is valid."
)
```

## `ValidationResult.failure()`

Creates a failed validation result.

```python
result = ValidationResult.failure(
    message="Invalid Morse Code.",
    invalid_values=["....----"],
)
```

These factory methods make result creation more readable.

# Result Combination

## `combine_results()`

Combines multiple `ValidationResult` objects into a single result.

The combined result is valid only when all supplied results are valid.

Conceptually:

```text
Validation Result 1
        │
Validation Result 2
        │
Validation Result 3
        │
        ▼
combine_results()
        │
        ▼
Combined ValidationResult
```

This provides a foundation for more complex validation workflows in the future.

# Result Helper Functions

## `valid_result()`

Convenience function for creating a successful validation result.

## `invalid_result()`

Convenience function for creating a failed validation result.

## `is_validation_result()`

Determines whether an object is a `ValidationResult`.

## `ensure_validation_result()`

Ensures that a supplied object is a `ValidationResult`.

It raises a `TypeError` when the object is not a valid validation result.

# Validation Architecture

The validation package follows a layered structure.

```text
                         validation/
                              │
               ┌──────────────┼──────────────┐
               │              │              │
               ▼              ▼              ▼
          validator.py   english_validator  morse_validator
               │              │              │
               │              │              │
               └──────────────┼──────────────┘
                              │
                              ▼
                    validation_result.py
```

The general validator provides reusable functionality.

The English and Morse validators provide domain-specific rules.

The validation result model provides a standardized representation for validation outcomes.

# Validation Processing Flow

A typical English validation workflow looks like:

```text
English Input
      │
      ▼
General Type Validation
      │
      ▼
Empty Input Check
      │
      ▼
Character Validation
      │
      ▼
Supported Character Check
      │
      ▼
English Validation
      │
      ▼
Validation Result
```

A Morse validation workflow follows a similar structure:

```text
Morse Input
      │
      ▼
General Type Validation
      │
      ▼
Empty Input Check
      │
      ▼
Separator Validation
      │
      ▼
Morse Sequence Validation
      │
      ▼
Mapping Validation
      │
      ▼
Validation Result
```

# Relationship With the Core Package

The `validation/` package depends on the canonical Morse Code definitions in `core/morse_code.py`.

This is important because the project should maintain a single source of truth for supported Morse Code mappings.

```text
core/morse_code.py
        │
        │
        ▼
validation/
        │
        ├── english_validator.py
        │
        └── morse_validator.py
```

The validation package does not duplicate the Morse Code mapping.

Instead, it asks the core mapping whether a character or sequence is supported.

# Relationship With Translation

Validation occurs before translation.

The intended processing flow is:

```text
User Input
    │
    ▼
Validation
    │
    ├── Invalid ──► Error Message
    │
    ▼
Valid Input
    │
    ▼
Translation
    │
    ▼
Translation Result
```

This separation prevents the translation engine from becoming responsible for user-input validation.

# Relationship With the Interface

The validation package should remain independent of GUI and CLI components.

The interface can call validation functions and use their results.

For example:

```python
from validation import get_english_validation_error

error = get_english_validation_error(
    user_input
)

if error:
    display_error(error)
```

The validation package does not decide how the error is displayed.

The GUI or CLI owns that responsibility.

# Design Principles

## Separation of Concerns

Each validation module has a focused responsibility.

```text
validator.py
    → General validation

english_validator.py
    → English validation

morse_validator.py
    → Morse Code validation

validation_result.py
    → Structured validation results
```

This prevents one large validation file from becoming difficult to maintain.

# Reusability

General validation functions are reusable across the project.

For example:

```python
from validation import is_non_empty_string
```

can be used by multiple application components without requiring knowledge of the English or Morse validators.

# Single Source of Truth

The validation system relies on the Morse mappings defined by the core package.

It does not maintain a separate Morse Code dictionary.

This prevents inconsistencies such as:

```text
Core says "." = E

Validation says "." is invalid
```

The mapping used for translation and validation therefore remains consistent.

# Explicit Validation

The validation system provides both boolean-style and exception-style validation.

Boolean checks:

```python
if is_valid_english_text(text):
    ...
```

Exception-based validation:

```python
validate_english_text(text)
```

This gives different application layers flexibility in how they handle invalid input.

# Testability

Validation functions are designed to be independently testable.

Important test categories include:

* Valid English text.

* Invalid English characters.

* Lowercase English text.

* Uppercase English text.

* Numbers.

* Supported punctuation.

* Empty strings.

* Whitespace-only strings.

* Non-string input.

* Valid Morse sequences.

* Invalid Morse sequences.

* Valid Morse words.

* Invalid Morse words.

* Valid Morse word separators.

* Invalid separator placement.

* Multiple spaces.

* Mixed valid and invalid input.

* Validation result creation.

* Validation result combination.

# Example Usage

## English Validation

```python
from validation import validate_english_text

text = "Hello World!"

validate_english_text(text)

print("English input is valid.")
```

If invalid characters are detected, the function raises a `ValueError`.

# Boolean English Validation

```python
from validation import is_valid_english_text

text = "Hello World"

if is_valid_english_text(text):
    print("Valid English input.")
else:
    print("Invalid English input.")
```

# Morse Validation

```python
from validation import validate_morse_text

morse = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

validate_morse_text(morse)

print("Morse input is valid.")
```

# Validation Result Example

```python
from validation import ValidationResult

result = ValidationResult.success(
    message="Input is valid."
)

if result:
    print(result.summary())
```

A failed result can contain invalid values:

```python
from validation import ValidationResult

result = ValidationResult.failure(
    message="Unsupported characters detected.",
    invalid_values=["#", "%"],
)

print(result.error_message())
```

# Module Dependency Guidelines

The validation package should maintain a mostly one-directional dependency structure.

Recommended relationship:

```text
core.morse_code
       │
       ▼
validator.py
       │
       ├──────────────► english_validator.py
       │
       └──────────────► morse_validator.py
                              │
                              ▼
                    validation_result.py
```

The actual implementation may allow the specialized validators to use shared validation utilities directly.

The important architectural rule is that the validation package should not depend on GUI, CLI, history, or interface components.

# Extending the Validation Package

If additional validation functionality is required, it should be added to the appropriate module whenever possible.

For example, if the translator eventually supports Morse timing input, a dedicated validator could be added:

```text
validation/

├── __init__.py
├── validator.py
├── english_validator.py
├── morse_validator.py
├── validation_result.py
└── timing_validator.py
```

A new validator should:

1. Have a focused responsibility.

2. Reuse utilities from `validator.py`.

3. Return or work with `ValidationResult` where appropriate.

4. Avoid duplicating existing validation logic.

5. Define `__all__` for its public API.

6. Be exposed through `validation/__init__.py` when appropriate.

7. Include automated tests.

8. Be documented in this package documentation.

# Error Handling

Validation functions use two primary approaches.

Boolean validation functions return:

```text
True
False
```

when the caller only needs to know whether input is valid.

Validation functions such as:

```text
validate_english_text()
validate_morse_text()
validate_length()
```

raise `ValueError` when invalid input is encountered.

This allows the caller to choose the appropriate validation style.

# Validation Philosophy

The validation system follows a simple principle:

```text
Reject invalid input early.
```

Rather than allowing invalid data to travel through the application and fail somewhere deeper in the translation system, the input should be checked as close to the entry point as practical.

```text
Input
  │
  ▼
Validate
  │
  ├── Invalid ──► Explain Problem
  │
  └── Valid
       │
       ▼
    Translate
```

This makes errors easier to understand and debugging easier to perform.

# Future Expansion

The validation package can eventually support additional validation requirements without changing its fundamental architecture.

Potential future additions include:

* Maximum translation length validation.

* File-input validation.

* Batch translation validation.

* Custom Morse Code mappings.

* Advanced punctuation validation.

* Translation-mode validation.

* GUI-specific input validation.

* Configuration validation.

* Import/export validation.

* Morse timing validation.

Any future functionality should remain separated according to responsibility.

# Summary

The `validation/` package forms the **input-quality and safety layer** of the Morse Translator.

Its primary responsibility is to ensure that input reaching the translation system is correctly formatted, supported, and meaningful.

The package is structured around:

```text
General Validation
        │
        ├── Type checking
        ├── Empty-input detection
        ├── Length validation
        ├── Character validation
        └── Normalization
                │
                ▼
       Specialized Validation
                │
        ┌───────┴────────┐
        │                │
        ▼                ▼
     English           Morse
     Validation        Validation
        │                │
        └───────┬────────┘
                │
                ▼
       Validation Results
                │
                ▼
        Translation Layer
```

The package keeps validation independent from translation, interfaces, file handling, and application logic.

This separation gives the Morse Translator a cleaner architecture while making individual validation components easy to test, reuse, and extend.


