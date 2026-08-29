# Utils Package Documentation

## Overview

The `utils/` package contains shared constants and general-purpose helper functions used throughout the Morse Translator.

It provides application-wide configuration values, translation settings, Morse Code separators, GUI defaults, history settings, validation messages, supported character definitions, and reusable utility functions.

The package is designed to prevent duplicated constants and small helper operations across the project.

The utilities package does **not** contain the core Morse Code translation algorithms, input validation rules, formatting logic, history management, or GUI implementation. Those responsibilities belong to their respective packages.

```text
utils/

│
├── __init__.py
├── constants.py
└── helpers.py
```

# Package Responsibilities

The `utils/` package is responsible for:

* Providing shared application constants.

* Defining translation directions.

* Defining Morse Code separators and symbols.

* Defining application metadata.

* Defining default configuration values.

* Defining GUI configuration constants.

* Defining history configuration values.

* Defining application and validation messages.

* Defining supported character categories.

* Providing reusable type-checking helpers.

* Providing general text inspection utilities.

* Providing translation-direction utilities.

* Providing Morse Code inspection helpers.

* Providing safe conversion functions.

* Providing collection utilities.

* Providing small display helpers.

* Providing general-purpose numerical utilities.

The package does **not** handle:

* Morse Code encoding.

* Morse Code decoding.

* Translation algorithms.

* Detailed input validation.

* Text formatting rules.

* Translation history storage.

* GUI rendering.

* GUI event handling.

* Automated testing.

Those responsibilities belong to other packages in the project.

# Module Structure

## `__init__.py`

The package initializer provides the public interface for the `utils/` package.

It collects commonly used constants and helper functions and makes them available through a centralized package-level API.

The initializer organizes its exports into logical groups including:

* Application information.

* Translation configuration.

* Morse Code configuration.

* Input and output defaults.

* Text formatting configuration.

* History configuration.

* GUI configuration.

* GUI text.

* Validation messages.

* Application messages.

* Supported characters.

* File and data configuration.

* Utility configuration.

* Boolean defaults.

* Type-checking helpers.

* Text inspection helpers.

* Text comparison helpers.

* Translation-direction helpers.

* Morse Code helpers.

* Safe conversion helpers.

* Collection helpers.

* Display helpers.

* General utility helpers.

### Purpose

The initializer allows other packages to import commonly used utilities without needing to know exactly which module contains each value or function.

For example:

```python
from utils import (
    APPLICATION_NAME,
    MORSE_CHARACTER_SEPARATOR,
    is_empty,
    count_words,
)
```

This creates a consistent public API while still allowing direct module imports when specialized functionality is required.

# `constants.py`

The `constants.py` module contains application-wide constant values used throughout the Morse Translator.

Keeping these values centralized prevents individual modules from defining their own versions of the same configuration values.

This improves consistency and makes future configuration changes easier.

# Application Information

The module defines metadata describing the application.

### `APPLICATION_NAME`

Stores the official application name.

```text
Morse Translator
```

### `APPLICATION_VERSION`

Stores the current application version.

The initial project version is:

```text
1.0.0
```

### `APPLICATION_DESCRIPTION`

Provides a short description of the application's purpose.

These values can be used by the GUI, command-line interface, documentation, or other application-level components.

# Translation Configuration

The package defines the two supported translation directions.

### `ENGLISH_TO_MORSE`

Represents translation from English text into Morse Code.

### `MORSE_TO_ENGLISH`

Represents translation from Morse Code into English text.

### `TRANSLATION_DIRECTIONS`

Contains the supported translation directions.

Conceptually:

```text
TRANSLATION_DIRECTIONS

├── English to Morse
└── Morse to English
```

Keeping these values centralized prevents different modules from using inconsistent direction names.

# Morse Code Configuration

The module defines constants describing Morse Code structure.

### `MORSE_CHARACTER_SEPARATOR`

Defines the separator used between individual Morse Code characters.

The default value is a single space:

```text
...
```

For example:

```text
.... . .-.. .-.. ---
```

Each Morse sequence is separated by a space.

### `MORSE_WORD_SEPARATOR`

Defines the separator used between words.

The default representation is:

```text
 / 
```

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

The separator allows the decoder to distinguish word boundaries.

### `MORSE_SYMBOLS`

Contains the supported Morse Code symbols:

```text
.-
```

### `MORSE_DOT`

Represents the Morse Code dot symbol:

```text
.
```

### `MORSE_DASH`

Represents the Morse Code dash symbol:

```text
-
```

These values are shared across the application rather than repeatedly hard-coded in different modules.

# Input and Output Defaults

The module defines default values for translation input and output.

### `DEFAULT_INPUT_TEXT`

Represents the default state of the application's input field.

### `DEFAULT_OUTPUT_TEXT`

Represents the default state of the translation output.

### `DEFAULT_TRANSLATION_DIRECTION`

Defines the initial translation direction.

The application defaults to:

```text
English to Morse
```

These values are particularly useful to the GUI and application startup logic.

# Text Formatting Configuration

The module defines shared text-processing configuration.

### `DEFAULT_TEXT_ENCODING`

Defines the default text encoding:

```text
utf-8
```

### `DEFAULT_MAX_INPUT_LENGTH`

Defines the maximum recommended input length.

### `DEFAULT_MAX_OUTPUT_LENGTH`

Defines the maximum recommended output length.

### `DEFAULT_TRUNCATION_SUFFIX`

Defines the suffix used when displaying truncated text.

The default value is:

```text
...
```

These values provide consistent limits and display behavior across the application.

# History Configuration

The module contains constants controlling translation history.

### `DEFAULT_HISTORY_LIMIT`

Defines the default maximum number of history entries.

The default is:

```text
50
```

### `MIN_HISTORY_LIMIT`

Defines the minimum supported history size.

### `MAX_HISTORY_LIMIT`

Defines the maximum supported history size.

### `HISTORY_TIMESTAMP_FORMAT`

Defines the standard timestamp representation used by history records.

The default format is:

```text
%Y-%m-%d %H:%M:%S
```

This allows history records to display consistent timestamps.

# GUI Configuration

The module provides shared window configuration values.

### `DEFAULT_WINDOW_WIDTH`

Defines the default application window width.

### `DEFAULT_WINDOW_HEIGHT`

Defines the default application window height.

### `MIN_WINDOW_WIDTH`

Defines the minimum supported window width.

### `MIN_WINDOW_HEIGHT`

Defines the minimum supported window height.

### `WINDOW_RESIZABLE`

Determines whether the application window can be resized.

These values are consumed primarily by the `interface/` package.

# GUI Text

The module also centralizes common interface labels.

These include:

* `APP_TITLE`

* `INPUT_LABEL`

* `OUTPUT_LABEL`

* `TRANSLATE_BUTTON_TEXT`

* `CLEAR_BUTTON_TEXT`

* `COPY_BUTTON_TEXT`

* `SWAP_BUTTON_TEXT`

* `HISTORY_BUTTON_TEXT`

* `CLEAR_HISTORY_BUTTON_TEXT`

* `EXIT_BUTTON_TEXT`

Centralizing GUI text provides a single location for common interface wording.

This also makes future wording changes easier without modifying multiple GUI components.

# Validation Messages

The module contains shared messages associated with invalid application input.

### `EMPTY_INPUT_MESSAGE`

Used when the user provides no meaningful input.

### `INVALID_INPUT_TYPE_MESSAGE`

Used when an operation receives a value of an unexpected type.

### `INVALID_DIRECTION_MESSAGE`

Used when an unsupported translation direction is supplied.

### `UNSUPPORTED_CHARACTER_MESSAGE`

Used when English input contains a character that is not supported by the translator.

### `INVALID_MORSE_MESSAGE`

Used when Morse Code input contains an invalid sequence.

These messages provide consistent wording across application components.

# Application Messages

The module defines common user-facing messages.

These include:

* `TRANSLATION_SUCCESS_MESSAGE`

* `TRANSLATION_ERROR_MESSAGE`

* `COPY_SUCCESS_MESSAGE`

* `HISTORY_EMPTY_MESSAGE`

* `HISTORY_CLEARED_MESSAGE`

Centralizing these messages prevents slightly different versions of the same message from appearing in different parts of the application.

# Supported Characters

The module defines the character categories supported by the Morse Translator.

### `SUPPORTED_LETTERS`

Contains the English alphabet:

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### `SUPPORTED_DIGITS`

Contains:

```text
0123456789
```

### `SUPPORTED_PUNCTUATION`

Contains the punctuation characters supported by the project.

### `SUPPORTED_ENGLISH_CHARACTERS`

Combines the supported letters, digits, and punctuation into a single collection.

Conceptually:

```text
SUPPORTED_ENGLISH_CHARACTERS

├── Letters
├── Digits
└── Punctuation
```

The core Morse mapping remains in `core/morse_code.py`.

The constants in this module are intended to provide convenient project-wide access to supported character categories.

# File and Data Configuration

The module contains constants related to persistent application data.

### `HISTORY_FILE_NAME`

Defines the default filename used for translation history storage.

The current filename is:

```text
translation_history.json
```

### `DEFAULT_DATA_DIRECTORY`

Defines the default directory for application data.

### `JSON_ENCODING`

Defines the encoding used for JSON data.

### `JSON_INDENT`

Defines the indentation level used when producing formatted JSON.

These values are primarily useful to the history and file-management portions of the application.

# Utility Configuration

The module defines defaults used by general helper functions.

### `MIN_TEXT_LENGTH`

Defines the minimum supported text length.

### `DEFAULT_TRUNCATE_LENGTH`

Defines the default length used when shortening text for display.

### `DEFAULT_PADDING_WIDTH`

Defines the default width used by display-alignment helpers.

### `DEFAULT_ALIGNMENT`

Defines the default text alignment.

### `VALID_ALIGNMENTS`

Contains the supported alignment values:

```text
left
right
center
```

# Boolean Defaults

The module defines boolean configuration values for common application behavior.

### `DEFAULT_CASE_SENSITIVE`

Determines the default case-sensitivity behavior.

### `DEFAULT_PRESERVE_SPACES`

Determines whether spaces should be preserved by default.

### `DEFAULT_PRESERVE_LINE_BREAKS`

Determines whether line breaks should be preserved by default.

These settings provide shared defaults that can be referenced by higher-level components.

# `helpers.py`

The `helpers.py` module contains small, reusable functions that do not belong specifically to the core translation, validation, formatting, history, or interface packages.

The functions are intentionally general-purpose.

They should provide useful operations without becoming a second implementation of another package's responsibilities.

# Type Checking Helpers

## `is_string()`

Determines whether a supplied value is a string.

Example:

```python
if is_string(value):
    print("Value is text.")
```

The function provides a simple reusable alternative to repeatedly writing `isinstance(value, str)` throughout the application.

## `is_integer()`

Determines whether a value is an integer.

Boolean values are intentionally excluded because Python treats `bool` as a subclass of `int`.

This means:

```text
True
```

is not considered a valid integer by this helper.

## `is_positive_integer()`

Determines whether a value is a positive integer.

This is useful for values such as:

* History limits.

* Display widths.

* Maximum lengths.

* Collection sizes.

## `is_boolean()`

Determines whether a value is a boolean.

# Text Inspection Helpers

## `is_empty()`

Determines whether text is empty or contains only whitespace.

For example:

```text
""
```

and:

```text
"   "
```

are both considered empty.

This is useful for basic application-level checks.

Detailed input validation remains the responsibility of the `validation/` package.

## `get_text_length()`

Returns the number of characters contained in a string.

Example:

```python
length = get_text_length("Hello")
```

The result is:

```text
5
```

## `count_words()`

Counts whitespace-separated words in a string.

For example:

```text
Hello World
```

contains two words.

## `count_lines()`

Counts the number of lines contained in a string.

This is useful for multiline input and output statistics.

## `count_characters()`

Counts characters in a string.

The function supports an option for including or excluding whitespace.

Example:

```python
count_characters(
    "Hello World",
    include_spaces=True,
)
```

The caller can therefore choose whether spaces should contribute to the count.

# Text Comparison Helpers

## `texts_match()`

Determines whether two strings are equal.

The function supports optional case-insensitive comparison.

For example:

```python
texts_match(
    "Hello",
    "hello",
    ignore_case=True,
)
```

returns:

```text
True
```

## `normalized_text_matches()`

Compares two strings after normalizing surrounding and repeated whitespace.

For example:

```text
"Hello   World"
```

and:

```text
"  Hello World  "
```

can be considered equivalent.

This is useful when comparing user input where insignificant whitespace should not affect the comparison.

# Translation Direction Helpers

## `is_valid_translation_direction()`

Determines whether a supplied translation direction is supported by the application.

The function checks against the centralized `TRANSLATION_DIRECTIONS` constant.

This prevents different modules from maintaining their own lists of valid directions.

## `reverse_translation_direction()`

Returns the opposite translation direction.

Conceptually:

```text
English to Morse
        │
        ▼
Morse to English
```

and:

```text
Morse to English
        │
        ▼
English to Morse
```

This is particularly useful for GUI controls that allow the user to swap translation direction.

# Morse Code Helpers

The Morse Code helpers provide lightweight inspection utilities.

They do not perform actual encoding or decoding.

The actual translation logic belongs to:

```text
core/
├── encoder.py
└── decoder.py
```

## `is_morse_symbol()`

Determines whether a character is a valid Morse Code symbol.

The supported symbols are:

```text
.
-
```

## `count_morse_symbols()`

Counts dots and dashes contained in a Morse Code string.

Separators and whitespace are ignored.

For example:

```text
.... . .-.. .-.. ---
```

contains only the actual Morse symbols in the count.

## `count_morse_characters()`

Counts Morse Code sequences separated by whitespace.

For example:

```text
.... . .-.. .-.. ---
```

contains five Morse character sequences.

## `contains_morse_symbols()`

Determines whether a string contains at least one Morse Code dot or dash.

This is a lightweight inspection helper and is not intended to replace the formal Morse validator.

# Safe Conversion Helpers

## `safe_int()`

Attempts to convert a value to an integer.

If conversion fails, a supplied default value is returned instead.

Example:

```python
number = safe_int(
    "25",
    default=0,
)
```

produces:

```text
25
```

If the value cannot be converted:

```python
number = safe_int(
    "abc",
    default=0,
)
```

the result is:

```text
0
```

This is useful when dealing with user-provided or loosely typed values.

## `safe_string()`

Converts a value to a string.

If the value is `None`, the supplied default string is returned.

This provides a predictable way to obtain a string representation without repeatedly writing custom `None` checks.

# Collection Helpers

## `list_is_empty()`

Determines whether a collection is empty.

The helper can safely handle `None` values.

## `contains_value()`

Determines whether a collection contains a specified value.

The helper provides a small reusable abstraction around membership checking.

# Display Helpers

## `create_separator()`

Creates a repeated-character separator.

Example:

```python
create_separator(
    length=20,
    character="-",
)
```

produces:

```text
--------------------
```

This is particularly useful for command-line or text-based output.

## `create_label()`

Creates a padded label suitable for aligned text output.

For example:

```python
create_label(
    "Input",
    width=15,
)
```

can be used to create consistently aligned output.

# General Utility Helpers

## `clamp()`

Restricts an integer value to a specified minimum and maximum.

For example:

```python
clamp(
    value=120,
    minimum=0,
    maximum=100,
)
```

returns:

```text
100
```

Similarly:

```python
clamp(
    value=-10,
    minimum=0,
    maximum=100,
)
```

returns:

```text
0
```

This is useful for values that must remain within safe boundaries.

## `ensure_range()`

Validates that an integer falls within an inclusive range.

Unlike `clamp()`, it does not modify an out-of-range value.

Instead, it raises an error when the value is outside the requested range.

This is useful when an invalid value should be rejected rather than automatically corrected.

## `remove_none_values()`

Creates a copy of a dictionary with entries whose values are `None` removed.

For example:

```python
values = {
    "input": "Hello",
    "output": None,
}
```

can be transformed into:

```python
{
    "input": "Hello",
}
```

The original dictionary remains unchanged.

# Utility Architecture

The `utils/` package follows a simple two-layer structure.

```text
                    utils/

                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
        constants.py        helpers.py
             │                   │
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
              Rest of Application
```

`constants.py` provides shared values.

`helpers.py` provides reusable operations.

The rest of the project can depend on these utilities without creating duplicate implementations.

# Dependency Structure

The recommended dependency relationship is:

```text
                    utils/
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
        constants.py        helpers.py
                                 │
                                 │
                                 ▼
                         Application Packages
```

The utilities package should remain a low-level dependency.

It should not depend heavily on higher-level application packages.

This helps prevent circular dependencies.

# Relationship With Other Packages

The `utils/` package is shared by many other parts of the Morse Translator.

```text
                    Morse Translator

                          │
                          ▼
                         utils
                          │
          ┌───────────────┼────────────────┐
          │               │                │
          ▼               ▼                ▼
        core        validation        formatting
          │               │                │
          └───────────────┼────────────────┘
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
          history                  interface
             │                         │
             └────────────┬────────────┘
                          │
                          ▼
                        tests
```

# Relationship With `core/`

The `core/` package contains the actual Morse translation logic.

The utilities package can provide shared configuration such as:

* Translation direction values.

* Morse separators.

* Supported character categories.

* General text helpers.

The `utils/` package should not implement the actual translation algorithms.

The relationship should therefore remain:

```text
utils
  │
  └── shared configuration
          │
          ▼
        core
          │
          ├── encoder
          ├── decoder
          └── translator
```

# Relationship With `validation/`

The validation package performs formal input validation.

The utilities package only provides small generic helpers that may assist validation.

For example:

```text
utils.is_string()
        │
        ▼
validation
        │
        ▼
Formal validation rules
```

A utility function should not become responsible for deciding whether an entire English or Morse input is valid.

That remains the responsibility of:

```text
validation/
├── validator.py
├── english_validator.py
└── morse_validator.py
```

# Relationship With `formatting/`

The formatting package is responsible for transforming text and Morse Code into presentation-ready representations.

The utilities package may provide basic helpers such as:

* Text length calculations.

* Empty-value checks.

* General display helpers.

However, formatting-specific behavior should remain inside:

```text
formatting/
├── formatter.py
└── morse_formatter.py
```

This keeps generic helpers separate from formatting rules.

# Relationship With `history/`

The history package manages translation records and stored translation history.

The utilities package provides configuration that can be useful to history management.

For example:

```text
DEFAULT_HISTORY_LIMIT
HISTORY_TIMESTAMP_FORMAT
HISTORY_FILE_NAME
DEFAULT_DATA_DIRECTORY
```

The actual creation, storage, retrieval, and removal of history records remains the responsibility of:

```text
history/
├── history_manager.py
└── translation_record.py
```

# Relationship With `interface/`

The interface package contains the Tkinter GUI.

The utilities package provides shared GUI-related constants such as:

* Window dimensions.

* Window title.

* Button labels.

* Input/output labels.

* Default configuration values.

The actual widgets, layout, styling, and event handling remain inside:

```text
interface/
├── gui.py
├── components.py
└── styles.py
```

# Relationship With `tests/`

The test package verifies that utilities behave correctly.

The helper functions should be tested for:

* Normal values.

* Empty values.

* Whitespace.

* Invalid types.

* Boundary values.

* Case differences.

* Morse symbols.

* Valid translation directions.

* Invalid translation directions.

* Conversion failures.

* Collection behavior.

* Range handling.

# Design Principles

## Centralized Configuration

Shared values should be defined once in `constants.py`.

Instead of:

```python
MAX_HISTORY = 50
```

being independently defined across several modules, the application should use:

```python
from utils import DEFAULT_HISTORY_LIMIT
```

This prevents configuration drift.

## Reusability

Helper functions should solve small problems that can reasonably appear in multiple parts of the application.

For example:

```text
count_words()
count_lines()
is_empty()
is_string()
```

can be reused without tying them to a specific interface.

## Single Responsibility

Each helper should perform one focused operation.

For example:

```text
is_integer()
```

should determine whether something is an integer.

It should not also perform translation validation, formatting, or history management.

## Low-Level Dependency

The utilities package should remain relatively independent of higher-level packages.

This creates a stable foundation that other components can safely depend upon.

## No Business Logic Duplication

The utilities package should not recreate functionality that already exists elsewhere.

For example:

```text
Encoding       → core/encoder.py
Decoding       → core/decoder.py
Validation     → validation/
Formatting     → formatting/
History        → history/
GUI            → interface/
```

The utility package should provide only shared supporting functionality.

# Public API

The package initializer exposes the most commonly used constants and helper functions.

The public API includes application information:

```python
APPLICATION_NAME
APPLICATION_VERSION
APPLICATION_DESCRIPTION
```

Translation configuration:

```python
ENGLISH_TO_MORSE
MORSE_TO_ENGLISH
TRANSLATION_DIRECTIONS
```

Morse Code configuration:

```python
MORSE_CHARACTER_SEPARATOR
MORSE_WORD_SEPARATOR
MORSE_SYMBOLS
MORSE_DOT
MORSE_DASH
```

History configuration:

```python
DEFAULT_HISTORY_LIMIT
MIN_HISTORY_LIMIT
MAX_HISTORY_LIMIT
HISTORY_TIMESTAMP_FORMAT
```

Supported character definitions:

```python
SUPPORTED_LETTERS
SUPPORTED_DIGITS
SUPPORTED_PUNCTUATION
SUPPORTED_ENGLISH_CHARACTERS
```

And reusable helpers such as:

```python
is_string
is_integer
is_positive_integer
is_boolean

is_empty
get_text_length
count_words
count_lines
count_characters

texts_match
normalized_text_matches

is_valid_translation_direction
reverse_translation_direction

is_morse_symbol
count_morse_symbols
count_morse_characters
contains_morse_symbols

safe_int
safe_string

list_is_empty
contains_value

create_separator
create_label

clamp
ensure_range
remove_none_values
```

# Example Usage

## Importing Constants

```python
from utils import (
    APPLICATION_NAME,
    APPLICATION_VERSION,
)

print(APPLICATION_NAME)
print(APPLICATION_VERSION)
```

## Checking Text

```python
from utils import (
    is_empty,
    count_words,
)

text = "Hello World"

if not is_empty(text):
    print(f"Words: {count_words(text)}")
```

## Checking Translation Direction

```python
from utils import (
    ENGLISH_TO_MORSE,
    reverse_translation_direction,
)

direction = ENGLISH_TO_MORSE

direction = reverse_translation_direction(
    direction
)

print(direction)
```

## Inspecting Morse Code

```python
from utils import (
    count_morse_symbols,
    contains_morse_symbols,
)

morse = ".... . .-.. .-.. ---"

if contains_morse_symbols(morse):
    print(
        count_morse_symbols(morse)
    )
```

## Creating Display Output

```python
from utils import (
    create_separator,
    create_label,
)

print(create_separator())

print(
    create_label("Input")
    + "Hello World"
)
```

# Error Handling

The helper functions use predictable error handling.

Functions that require a specific type generally raise `ValueError` when an invalid type is supplied.

For example:

```python
get_text_length(123)
```

raises an error because the function expects a string.

Boolean-returning inspection helpers generally return `False` for values that cannot satisfy the requested condition.

For example:

```python
is_string(123)
```

returns:

```text
False
```

This distinction makes the helpers convenient for both validation-style checks and strict utility operations.

# Testing Strategy

The utilities should be tested at both the individual-function and integration levels.

Important test categories include:

```text
Normal Input
     │
     ▼
Boundary Values
     │
     ▼
Empty Values
     │
     ▼
Invalid Types
     │
     ▼
Invalid Configuration
     │
     ▼
Expected Exceptions
```

For example, `clamp()` should be tested with:

* Values below the minimum.

* Values at the minimum.

* Values inside the range.

* Values at the maximum.

* Values above the maximum.

* Invalid minimum/maximum relationships.

Similarly, `reverse_translation_direction()` should be tested with:

* English-to-Morse.

* Morse-to-English.

* Invalid directions.

# Extending the Utilities Package

New utility functionality should only be added to this package when it is genuinely reusable across multiple parts of the application.

For example, a future utility could provide a reusable timestamp function:

```text
utils/
├── __init__.py
├── constants.py
├── helpers.py
└── datetime_utils.py
```

However, a new module should only be created when the functionality becomes substantial enough to justify separation.

Small related helpers should generally remain in `helpers.py`.

New utilities should:

1. Have a focused responsibility.

2. Avoid duplicating existing functionality.

3. Use type hints where appropriate.

4. Validate parameters consistently.

5. Follow the project's `#` comment documentation style.

6. Define `__all__` when exposing a module-level public API.

7. Be exported through `utils/__init__.py` when appropriate.

8. Include automated tests.

9. Be documented in `docs/utils.md`.

10. Avoid unnecessary dependencies on higher-level packages.

# Dependency Guidelines

The utilities package should maintain a simple dependency structure.

```text
constants.py
     │
     ▼
helpers.py
     │
     ▼
Application Packages
```

`constants.py` should remain independent of application-level modules.

`helpers.py` may use shared constants when necessary.

Higher-level packages can depend on `utils`.

The reverse relationship should generally be avoided.

For example:

```text
Good:

interface → utils
history   → utils
core      → utils

Avoid:

utils → interface
utils → history
utils → gui
```

This keeps the utility layer reusable.

# Maintainability

The utilities package is intentionally designed to be small and predictable.

Its primary maintainability goals are:

* Centralized configuration.

* Minimal duplication.

* Focused helper functions.

* Clear naming.

* Consistent error handling.

* Low coupling.

* Reusable functionality.

* Easy unit testing.

Because utility functions are used throughout the application, changes to this package should be made carefully.

A seemingly small change to a shared constant or helper can affect multiple packages.

# Future Expansion

The utilities package can be expanded if the project grows.

Potential future additions include:

* Date and time utilities.

* File path utilities.

* Configuration loading.

* Application environment detection.

* Clipboard utilities.

* Logging helpers.

* Serialization helpers.

* Performance timing utilities.

* Random identifier generation.

However, functionality should only be added when it provides a clear benefit.

The project is intentionally designed to remain manageable for a freshman-to-sophomore-level Python application.

# Summary

The `utils/` package provides the shared foundation used by the rest of the Morse Translator.

Its responsibilities are divided between:

```text
utils/

│
├── constants.py
│       │
│       └── Shared application configuration
│
└── helpers.py
        │
        └── Reusable general-purpose functions
```

`constants.py` centralizes values such as:

```text
Application Information
Translation Directions
Morse Separators
GUI Configuration
History Configuration
Validation Messages
Supported Characters
File Configuration
Utility Defaults
```

`helpers.py` provides reusable operations such as:

```text
Type Checking
Text Inspection
Text Comparison
Direction Handling
Morse Inspection
Safe Conversion
Collection Utilities
Display Helpers
Range Utilities
```

The package deliberately avoids implementing the application's major business logic.

```text
                 Morse Translator

                       │
                       ▼
                     utils
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
      core        validation       formatting
       │               │                │
       └───────────────┼────────────────┘
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
           history          interface
              │                 │
              └────────┬────────┘
                       │
                       ▼
                     tests
```

This separation keeps the project modular and prevents common constants and simple helper operations from being duplicated throughout the application.

The `utils/` package therefore acts as a **shared support layer** for the Morse Translator, providing common building blocks while leaving translation, validation, formatting, history, and interface responsibilities to their dedicated packages.


