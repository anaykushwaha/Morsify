# Formatting Package Documentation

## Overview

The `formatting/` package contains the text and Morse Code formatting utilities used throughout the Morse Translator.

It is responsible for taking valid text or Morse Code and preparing it into a clean, consistent, and readable representation for translation workflows, terminal output, graphical interfaces, and other application-level components.

The package is intentionally separate from the `core/` and `validation/` packages. The core package determines **what a translation is**, the validation package determines **whether input is acceptable**, and the formatting package determines **how that input or output should be represented**.

```text
formatting/

│

├── __init__.py
├── formatter.py
└── morse_formatter.py
```

# Package Responsibilities

The `formatting/` package is responsible for:

* Cleaning unnecessary whitespace.
* Normalizing text.
* Normalizing text case.
* Formatting multiline text.
* Formatting translation output.
* Creating labeled input/output representations.
* Truncating long text for display.
* Padding text for aligned output.
* Formatting individual Morse Code sequences.
* Formatting Morse Code words.
* Normalizing Morse Code spacing.
* Normalizing Morse Code word separators.
* Splitting Morse Code into words.
* Splitting Morse Code into character sequences.
* Joining Morse Code characters and words.
* Counting Morse Code characters and words.
* Preparing formatted output for other application layers.

The package does **not** handle:

* Translation.
* English-to-Morse conversion.
* Morse-to-English conversion.
* Input validation.
* Translation history.
* GUI rendering.
* Command-line menus.
* File management.
* Persistent storage.
* Application configuration.

Those responsibilities belong to other packages in the project.

# Module Structure

## `__init__.py`

The package initializer provides the public interface for the `formatting/` package.

Rather than requiring other parts of the project to know the location of every formatting function, commonly used functionality can be imported directly from the package.

The initializer exposes functionality from:

* `formatter`
* `morse_formatter`

It also organizes the public API into logical categories such as:

* General text formatting.
* General output formatting.
* Text display helpers.
* Morse formatting constants.
* Morse normalization.
* Morse character formatting.
* Morse word formatting.
* Morse output formatting.
* Morse formatting utilities.

### Purpose

The initializer creates a centralized public API while allowing the individual modules to remain internally organized.

For example:

```python
from formatting import normalize_text
from formatting import normalize_morse
```

instead of requiring every caller to know the internal module structure.

# `formatter.py`

`formatter.py` contains general-purpose text formatting utilities.

The module is not specifically tied to Morse Code. Its functionality can therefore be reused for English input, translated output, GUI text fields, command-line output, and other text-processing operations.

The module focuses on **presentation and normalization**, rather than determining whether the text is valid.

## Text Normalization

### `normalize_text()`

Normalizes a string by:

* Removing unnecessary surrounding whitespace.
* Replacing repeated whitespace with single spaces.
* Producing a consistent text representation.

For example:

```text
"   Hello     World   "
```

becomes:

```text
"Hello World"
```

This provides a consistent representation before text is passed to other components.

### `normalize_case()`

Converts text to uppercase.

For example:

```text
"Hello World"
```

becomes:

```text
"HELLO WORLD"
```

This is particularly useful because the Morse mapping is defined using uppercase English characters.

The function does not modify the meaning of numbers, whitespace, or punctuation.

### `clean_text()`

Removes unnecessary whitespace from the beginning and end of a string.

For example:

```text
"   Hello World   "
```

becomes:

```text
"Hello World"
```

Unlike `normalize_text()`, it does not collapse meaningful internal whitespace.

# Spacing and Display Formatting

## `normalize_spaces()`

Replaces consecutive whitespace characters with a single space.

For example:

```text
"Hello     World"
```

becomes:

```text
"Hello World"
```

This is useful when input originates from user interfaces or other sources where inconsistent spacing may occur.

## `preserve_line_breaks()`

Cleans individual lines while preserving the original line structure.

For example:

```text
"  Hello World  \n  Morse Translator  "
```

can become:

```text
"Hello World
Morse Translator"
```

This is useful when multiline input needs to remain multiline.

## `format_multiline_text()`

Formats an entire multiline text block.

It:

* Removes unnecessary surrounding whitespace.
* Removes unnecessary whitespace around individual lines.
* Preserves line boundaries.

This provides a clean representation for multiline text fields.

# Output Formatting

## `format_translation_output()`

Prepares translated text for display.

The function removes unnecessary whitespace around the translated result without modifying the actual content.

It is intended for use when translation output needs to be passed to a CLI, GUI, or other presentation layer.

## `format_labeled_output()`

Creates a simple labeled representation of text.

For example:

```text
Input: Hello World
```

The function receives the label and content separately and combines them into a consistent display string.

## `format_input_output()`

Creates a standardized two-line representation containing an input and its corresponding output.

Example:

```text
Input: Hello World
Output: .... . .-.. .-.. ---
```

This can be useful for:

* CLI output.
* Translation history previews.
* Debugging.
* GUI result displays.

# Length and Display Helpers

## `truncate_text()`

Limits text to a specified maximum length.

If the text exceeds the limit, the function shortens it and adds a suffix.

Example:

```text
This is a very long translation...
```

This is particularly useful for interfaces where displaying an entire translation could consume excessive screen space.

The suffix can be customized.

## `pad_text()`

Pads text to a requested width.

Supported alignment modes are:

* `left`
* `right`
* `center`

For example:

```text
Hello
```

can be padded to produce consistently sized output fields.

This is useful when displaying structured information in a terminal.

# General Formatting Checks

## `is_empty_text()`

Determines whether a string contains no meaningful content.

Whitespace-only strings are considered empty.

For example:

```text
""
```

and:

```text
"     "
```

are treated as empty.

This function is intentionally a lightweight formatting helper rather than the project's primary validation system.

## `has_multiple_lines()`

Determines whether text contains more than one line.

This can be useful when deciding whether a display component needs multiline formatting.

# `morse_formatter.py`

`morse_formatter.py` contains formatting functionality specifically designed for Morse Code.

Morse Code has a formatting structure that differs from ordinary English text.

A typical Morse representation uses:

```text
.-
```

for an individual character,

```text
.- -...
```

for multiple characters, and:

```text
.- -... / -.-.
```

to distinguish words.

The module standardizes this representation throughout the application.

# Morse Formatting Constants

## `MORSE_SYMBOLS`

Contains the two symbols used by Morse Code:

```text
.
-
```

These symbols represent dots and dashes.

The constant is used by formatting functions when checking whether a Morse sequence contains appropriate symbols.

## `MORSE_CHARACTER_SEPARATOR`

Defines the separator between individual Morse character sequences.

Its standard value is:

```text
" "
```

Therefore:

```text
.... . .-.. .-.. ---
```

represents multiple Morse characters separated by spaces.

## `MORSE_WORD_SEPARATOR`

Defines the standard separator between Morse words.

Its value is:

```text
" / "
```

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

represents:

```text
HELLO WORLD
```

# Morse Sequence Formatting

## `normalize_morse_spacing()`

Normalizes whitespace within Morse Code.

It ensures that:

* Individual Morse characters are separated consistently.
* Word separators are represented consistently.
* Unnecessary surrounding whitespace is removed.

For example:

```text
"  ....   .   .-..  /  .--  ---  "
```

can be normalized into:

```text
".... . .-.. / .-- ---"
```

This prevents inconsistent user input from producing inconsistent output formatting.

## `normalize_morse_word_separator()`

Normalizes forward-slash word separators.

Different input forms such as:

```text
".... . / .--"
```

and:

```text
".... ./ .--"
```

can be represented using the project's standard word separator:

```text
".... . / .--"
```

## `normalize_morse()`

Provides the primary normalization interface for Morse Code.

It combines the necessary Morse spacing behavior into a single operation.

Other components can therefore call:

```python
normalize_morse(text)
```

without needing to manually perform individual formatting steps.

# Morse Character Formatting

## `format_morse_character()`

Formats an individual Morse Code character sequence.

For example:

```text
"  .-  "
```

becomes:

```text
".-"
```

The function also ensures that the sequence contains only Morse symbols.

This function is concerned with formatting an individual sequence rather than an entire Morse message.

## `format_morse_word()`

Formats a group of Morse character sequences representing a single word.

For example:

```text
"  ....   .   .-..   .-..   --- "
```

becomes:

```text
".... . .-.. .-.. ---"
```

This creates a consistent representation before words are combined into a complete Morse message.

# Morse Word Formatting

## `split_morse_words()`

Splits a Morse message into individual word groups.

The forward slash represents the boundary between words.

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

is divided into:

```text
.... . .-.. .-.. ---
```

and:

```text
.-- --- .-. .-.. -..
```

The function returns the resulting groups as a list.

## `join_morse_words()`

Performs the opposite operation.

It takes a list of Morse word groups and combines them using the standard word separator.

Conceptually:

```text
[
    ".... . .-.. .-.. ---",
    ".-- --- .-. .-.. -.."
]
```

becomes:

```text
".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

# Morse Character Grouping

## `split_morse_characters()`

Splits a Morse word into individual character sequences.

For example:

```text
".... . .-.. .-.. ---"
```

becomes:

```text
[
    "....",
    ".",
    ".-..",
    ".-..",
    "---"
]
```

This is useful when individual Morse sequences need to be inspected or processed separately.

## `join_morse_characters()`

Performs the reverse operation.

Given:

```text
[
    "....",
    ".",
    ".-..",
    ".-..",
    "---"
]
```

it produces:

```text
".... . .-.. .-.. ---"
```

This provides a consistent way to reconstruct a Morse word.

# Morse Display Formatting

## `format_morse_output()`

Prepares Morse Code for display.

It applies the package's standard Morse formatting and normalization rules.

This function is useful when translated Morse Code needs to be displayed by another component.

## `format_morse_labeled_output()`

Creates a labeled Morse output string.

For example:

```text
Morse: .... . .-.. .-.. ---
```

This is useful for interfaces that need to display a result alongside a descriptive label.

## `format_morse_input_output()`

Creates a two-line representation containing Morse input and its translated output.

For example:

```text
Input: .... . .-.. .-.. ---
Output: HELLO
```

This provides a convenient representation for CLI output, history previews, and debugging.

# Morse Formatting Utilities

## `count_morse_characters()`

Counts the individual Morse character sequences contained in a message.

For example:

```text
.... . .-.. .-.. ---
```

contains five Morse character sequences.

The function works across multiple Morse words.

## `count_morse_words()`

Counts the number of Morse word groups in a message.

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

contains two Morse words.

## `is_morse_text_empty()`

Determines whether Morse input contains meaningful content.

Empty strings and whitespace-only strings are considered empty.

This provides a lightweight check before formatting operations are performed.

# Formatting Architecture

The formatting package follows a simple two-layer structure.

```text
                    formatting/
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
       formatter.py        morse_formatter.py
              │                     │
              ▼                     ▼
       General Text          Morse-Specific
        Formatting             Formatting
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                 Application Layer
```

The two modules share the same overall purpose but operate at different levels.

`formatter.py` handles general text.

`morse_formatter.py` handles the special formatting requirements of Morse Code.

# Formatting Processing Flow

A typical English-to-Morse workflow can be represented as:

```text
User Input
    │
    ▼
Validation
    │
    ▼
Core Encoder
    │
    ▼
Morse Output
    │
    ▼
Morse Formatter
    │
    ▼
Formatted Morse
    │
    ▼
Interface
```

A Morse-to-English workflow follows:

```text
User Input
    │
    ▼
Validation
    │
    ▼
Morse Formatter
    │
    ▼
Normalized Morse
    │
    ▼
Core Decoder
    │
    ▼
English Output
    │
    ▼
General Formatter
    │
    ▼
Interface
```

The formatting package does not perform the actual translation.

# Relationship With Other Packages

The `formatting/` package works closely with several other parts of the Morse Translator.

```text
                    Morse Translator
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
      core            validation         formatting
        │                  │                  │
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                     interface
```

## `core/`

The `core/` package performs the actual translation.

Formatting can prepare its input and output but should not duplicate translation logic.

For example:

```text
core.encoder
     │
     ▼
Morse Translation
     │
     ▼
formatting.morse_formatter
     │
     ▼
Readable Morse Output
```

## `validation/`

The `validation/` package determines whether input is acceptable.

Formatting should not replace validation.

For example:

```text
Input
  │
  ▼
Validation
  │
  ├── Invalid → Error
  │
  └── Valid
        │
        ▼
    Formatting
```

This separation keeps the responsibilities clear.

## `history/`

The history package can store formatted input and output representations when displaying previous translations.

Formatting should provide the representation, while history is responsible for storing and retrieving it.

## `interface/`

The interface package uses formatting utilities when presenting information to users.

For example, a GUI result panel could use:

```python
format_morse_output()
```

to prepare Morse Code before displaying it.

## `utils/`

The utilities package can provide constants and generic helper functions that support formatting without becoming formatting-specific.

## `tests/`

The testing package verifies that formatting functions behave correctly for normal, unusual, and invalid inputs.

# Design Principles

## Separation of Concerns

The formatting package should focus exclusively on representation and normalization.

For example:

```text
core
    → What does the message translate to?

validation
    → Is the input acceptable?

formatting
    → How should the message be represented?

history
    → What translations should be remembered?

interface
    → How should the information be presented?
```

This keeps the overall application modular.

## Consistency

All Morse Code output should follow the same formatting conventions.

The project uses:

```text
Single Morse character
    → individual dot/dash sequence

Morse characters
    → separated by spaces

Morse words
    → separated by " / "
```

For example:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

This consistency prevents different parts of the application from producing incompatible representations.

## Reusability

Formatting functions should be reusable by multiple application layers.

The same function can potentially be used by:

* GUI components.
* CLI output.
* Translation history.
* Tests.
* Debugging tools.
* Future API components.

The formatting module should therefore avoid making assumptions about where its output will ultimately be displayed.

## Testability

Formatting functions are designed to be small and deterministic.

For a given input, the same formatting operation should consistently produce the same output.

Tests should cover:

* Normal text.
* Empty strings.
* Whitespace-only input.
* Repeated whitespace.
* Uppercase text.
* Lowercase text.
* Multiline text.
* Individual Morse sequences.
* Multiple Morse characters.
* Multiple Morse words.
* Irregular Morse spacing.
* Invalid Morse symbols.
* Long text.
* Different padding alignments.
* Truncation boundaries.

# Error Handling

Formatting functions validate basic argument types before processing.

For example, functions expecting text require a string.

Invalid types should produce clear errors rather than allowing unexpected Python behavior to propagate through the application.

Examples include:

```text
Text must be a string.
Morse text must be a string.
Morse sequence must be a string.
Maximum length must be an integer.
Alignment must be 'left', 'right', or 'center'.
```

The formatting package should not generally be responsible for determining whether a complete user input is semantically valid.

That responsibility belongs to `validation/`.

# Public API

The formatting package exposes the following general text functionality:

```text
normalize_text
normalize_case
clean_text
normalize_spaces
preserve_line_breaks
format_multiline_text
format_translation_output
format_labeled_output
format_input_output
truncate_text
pad_text
is_empty_text
has_multiple_lines
```

The Morse-specific API includes:

```text
MORSE_SYMBOLS
MORSE_CHARACTER_SEPARATOR
MORSE_WORD_SEPARATOR

normalize_morse_spacing
normalize_morse_word_separator
normalize_morse

format_morse_character
format_morse_word

split_morse_words
join_morse_words

split_morse_characters
join_morse_characters

format_morse_output
format_morse_labeled_output
format_morse_input_output

count_morse_characters
count_morse_words
is_morse_text_empty
```

These functions are exposed through `formatting/__init__.py`.

# Example Usage

## General Text Formatting

```python
from formatting import normalize_text

text = "   Hello     World   "

formatted = normalize_text(text)

print(formatted)
```

Result:

```text
Hello World
```

## Text Case Normalization

```python
from formatting import normalize_case

text = "Hello World"

formatted = normalize_case(text)

print(formatted)
```

Result:

```text
HELLO WORLD
```

## Morse Formatting

```python
from formatting import normalize_morse

morse = "  ....   .   .-..   .-..   ---  "

formatted = normalize_morse(morse)

print(formatted)
```

Result:

```text
.... . .-.. .-.. ---
```

## Morse Word Formatting

```python
from formatting import format_morse_word

word = "  ....   .   .-..   .-..   --- "

formatted = format_morse_word(word)

print(formatted)
```

Result:

```text
.... . .-.. .-.. ---
```

## Splitting Morse Characters

```python
from formatting import split_morse_characters

morse_word = ".... . .-.. .-.. ---"

characters = split_morse_characters(morse_word)

print(characters)
```

Result:

```text
[
    "....",
    ".",
    ".-..",
    ".-..",
    "---"
]
```

## Joining Morse Characters

```python
from formatting import join_morse_characters

characters = [
    "....",
    ".",
    ".-..",
    ".-..",
    "---",
]

morse_word = join_morse_characters(characters)

print(morse_word)
```

Result:

```text
.... . .-.. .-.. ---
```

## Formatting Translation Output

```python
from formatting import format_input_output

result = format_input_output(
    "Hello World",
    ".... . .-.. .-.. --- / .-- --- .-. .-.. -..",
)

print(result)
```

Result:

```text
Input: Hello World
Output: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

# Module Dependency Guidelines

The formatting package should maintain a lightweight dependency structure.

```text
                 formatting/
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   formatter.py          morse_formatter.py
          │                       │
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
               Application Layer
```

The formatting modules should primarily depend on:

* Python standard library functionality.
* Shared project constants when genuinely necessary.
* Basic data types.

They should avoid depending directly on:

* GUI components.
* CLI menus.
* History managers.
* File managers.
* Application startup logic.

This minimizes coupling.

# Formatting and Validation Relationship

Formatting and validation are related but distinct.

A useful distinction is:

```text
Validation
    │
    ▼
"Is this acceptable?"

Formatting
    │
    ▼
"How should this be represented?"
```

For example, a Morse input might contain irregular spacing:

```text
"....   .   .-.."
```

The formatting layer can normalize it to:

```text
".... . .-.."
```

The validation layer can then determine whether the resulting sequences are supported by the translator.

Neither package should take over the other's responsibility.

# Formatting and Translation Relationship

The formatting package should not perform translation itself.

The encoder and decoder remain responsible for the transformation:

```text
English
   │
   ▼
Encoder
   │
   ▼
Morse
```

or:

```text
Morse
   │
   ▼
Decoder
   │
   ▼
English
```

Formatting can operate before or after those transformations:

```text
Input
  │
  ▼
Formatter
  │
  ▼
Validator
  │
  ▼
Translator
  │
  ▼
Formatter
  │
  ▼
Output
```

This prevents formatting logic from becoming intertwined with translation logic.

# Future Expansion

The formatting package can be expanded if the project eventually requires more sophisticated presentation features.

Potential future additions include:

* HTML output formatting.
* Rich terminal formatting.
* Table formatting.
* Translation summary formatting.
* Colored Morse display.
* Character-by-character Morse formatting.
* Compact Morse representations.
* Alternative word separator formats.
* Export-specific formatting.
* GUI-specific formatting adapters.

These should only be introduced when the application actually needs them.

The package should not be expanded simply to increase the number of files or functions.

# Summary

The `formatting/` package provides the **representation and normalization layer** of the Morse Translator.

Its primary purpose is to ensure that English text and Morse Code are presented consistently throughout the application without becoming responsible for translation or validation.

Its structure is:

```text
formatting/

├── __init__.py
│
├── formatter.py
│   │
│   ├── Text normalization
│   ├── Whitespace handling
│   ├── Multiline formatting
│   ├── Output formatting
│   ├── Text truncation
│   ├── Text padding
│   └── Formatting checks
│
└── morse_formatter.py
    │
    ├── Morse normalization
    ├── Morse character formatting
    ├── Morse word formatting
    ├── Morse character grouping
    ├── Morse word grouping
    ├── Morse output formatting
    └── Morse statistics
```

The overall architecture remains:

```text
                    Morse Translator
                           │
                           ▼
                      User Input
                           │
                           ▼
                       Validation
                           │
                           ▼
                          Core
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                 Encoder       Decoder
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                       Formatting
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
              General Text      Morse
                Formatting    Formatting
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                       Interface
```

This separation gives the project a clean architecture in which translation, validation, formatting, history, utilities, and presentation each have clearly defined responsibilities.

The `formatting/` package therefore acts as the **presentation-preparation layer** between the translator's underlying operations and the parts of the application that need to display or store those results.

