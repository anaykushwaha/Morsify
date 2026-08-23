# Morse Translator — Architecture

## 1. Overview

Morse Translator is a modular Python application designed to translate text between English and Morse Code in both directions. The project separates translation logic, validation, formatting, history management, and the graphical interface into independent packages.

The architecture is intentionally modular without being unnecessarily complex. Each package has a clearly defined responsibility, allowing individual components to be developed, tested, and maintained independently.

The application uses Python's standard library wherever possible, with Tkinter providing the graphical interface.

---

## 2. Architectural Goals

The project architecture is designed around the following goals:

* Keep translation logic independent from the user interface.
* Separate encoding and decoding responsibilities.
* Validate input before attempting translation.
* Keep formatting logic independent from translation logic.
* Maintain translation history separately from the translation engine.
* Make individual components easy to unit test.
* Keep shared constants and helper functions centralized.
* Provide a clear structure that can be extended in the future.
* Keep the overall design understandable for a beginner/intermediate Python developer.

---

## 3. High-Level Architecture

The application follows a layered, modular structure:

```text
                    ┌────────────────────┐
                    │      main.py       │
                    │  Application Entry │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     interface/     │
                    │    Tkinter GUI     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    validation/     │
                    │    Input Checks    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │       core/        │
                    │ Translation Engine │
                    └─────────┬──────────┘
                              │
              ┌───────────────┼────────────────┐
              │               │                │
              ▼               ▼                ▼
        ┌───────────┐   ┌───────────┐   ┌─────────────┐
        │  Encoder  │   │  Decoder  │   │ Morse Code  │
        └───────────┘   └───────────┘   │   Mapping   │
                                        └─────────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │    formatting/     │
                    │ Output Formatting  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      history/      │
                    │ History Management │
                    └────────────────────┘
```

The `tests/` package operates independently of the runtime flow and tests the behavior of the individual components.

---

# 4. Project Structure

```text
morse-translator/
│
├── main.py
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── .gitignore
│
├── core/
│   ├── __init__.py
│   ├── translator.py
│   ├── encoder.py
│   ├── decoder.py
│   ├── morse_code.py
│   └── translation.py
│
├── validation/
│   ├── __init__.py
│   ├── validator.py
│   ├── english_validator.py
│   └── morse_validator.py
│
├── formatting/
│   ├── __init__.py
│   ├── formatter.py
│   └── morse_formatter.py
│
├── history/
│   ├── __init__.py
│   ├── history_manager.py
│   └── translation_record.py
│
├── interface/
│   ├── __init__.py
│   ├── gui.py
│   ├── components.py
│   └── styles.py
│
├── utils/
│   ├── __init__.py
│   ├── constants.py
│   └── helpers.py
│
├── tests/
│   ├── __init__.py
│   ├── test_translator.py
│   ├── test_encoder.py
│   ├── test_decoder.py
│   ├── test_validator.py
│   ├── test_history.py
│   └── test_helpers.py
│
└── docs/
    ├── architecture.md
    ├── core.md
    ├── validation.md
    ├── formatting.md
    ├── history.md
    ├── interface.md
    ├── utils.md
    └── tests.md
```

---

# 5. Application Entry Point

## `main.py`

`main.py` is responsible for starting the application.

It should contain minimal application logic. Its primary responsibility is to initialize the required components and launch the graphical interface.

The entry point should not contain:

* Morse translation algorithms
* Input validation rules
* GUI component definitions
* History management logic
* Morse Code mappings

Keeping `main.py` small makes the application's starting point easy to understand.

---

# 6. Core Translation Layer

The `core/` package contains the central translation functionality.

## `core/morse_code.py`

This module stores the Morse Code mappings used by the application.

The project maintains mappings for supported characters, potentially including:

* Letters A–Z
* Numbers 0–9
* Supported punctuation

The mappings are kept separate from the translation algorithms so that the data can be modified without changing the encoder or decoder implementation.

---

## `core/encoder.py`

The encoder is responsible for converting English text into Morse Code.

Example:

```text
HELLO
```

becomes:

```text
.... . .-.. .-.. ---
```

The encoder should focus exclusively on the English-to-Morse process.

---

## `core/decoder.py`

The decoder performs the opposite operation.

Example:

```text
.... . .-.. .-.. ---
```

becomes:

```text
HELLO
```

The decoder should not be responsible for validating whether the input is valid. Validation belongs to the `validation/` package.

---

## `core/translator.py`

`translator.py` acts as the high-level interface to the translation system.

Instead of requiring the GUI to interact directly with individual encoder and decoder implementations, it can interact with the translator.

Conceptually:

```text
GUI
 │
 ▼
Translator
 ├── Encoder
 └── Decoder
```

This reduces coupling between the user interface and the lower-level translation components.

---

## `core/translation.py`

This module represents the result or metadata associated with a translation.

A translation record can contain information such as:

```text
Original Text
Translated Text
Translation Direction
Timestamp
```

This object can later be used by the history system.

---

# 7. Validation Layer

The `validation/` package ensures that input is appropriate before it reaches the translation engine.

## `validation/validator.py`

Provides general validation functionality and acts as a common interface for validation operations.

---

## `validation/english_validator.py`

Handles validation of English input.

Possible checks include:

* Empty input
* Unsupported characters
* Invalid formatting
* Characters outside the application's supported alphabet

---

## `validation/morse_validator.py`

Handles Morse Code validation.

Possible checks include:

* Invalid Morse symbols
* Invalid character sequences
* Incorrect separators
* Empty input
* Unsupported Morse patterns

Validation should occur before translation whenever appropriate.

---

# 8. Formatting Layer

The `formatting/` package controls how input and output are represented.

## `formatting/formatter.py`

Provides general formatting functionality shared by the application.

It may handle tasks such as:

* Removing unnecessary whitespace
* Normalizing text
* Preparing output for display

---

## `formatting/morse_formatter.py`

Contains formatting logic specifically related to Morse Code.

This can include:

* Character separators
* Word separators
* Morse output spacing
* Consistent output representation

Keeping formatting separate from translation prevents the encoder and decoder from becoming responsible for presentation concerns.

---

# 9. History Layer

The `history/` package manages previous translations.

## `history/translation_record.py`

Represents an individual translation stored in history.

A record may contain:

```text
Original:
Hello World

Translation:
.... . .-.. .-.. --- / .-- --- .-. .-.. -..

Direction:
English → Morse

Timestamp:
2026-08-23 20:00
```

---

## `history/history_manager.py`

Manages the collection of translation records.

Possible operations include:

```text
add_translation()
get_history()
clear_history()
remove_translation()
```

The history manager should not perform translation itself.

Its responsibility is only to store and manage translation records.

---

# 10. Interface Layer

The `interface/` package contains the Tkinter graphical user interface.

## `interface/gui.py`

Contains the main application window and coordinates interactions between the GUI and the underlying application components.

The GUI should request operations from other packages rather than implementing translation algorithms itself.

---

## `interface/components.py`

Contains reusable GUI components.

Potential components include:

* Input text box
* Output text box
* Translation direction selector
* Translate button
* Clear button
* Copy button
* History display

Separating components from the main GUI keeps the interface easier to maintain.

---

## `interface/styles.py`

Contains visual constants and styling information.

Potential values include:

* Window dimensions
* Fonts
* Button configuration
* Padding
* Text sizes
* Colors

Centralizing these values makes it easier to modify the appearance of the application.

---

# 11. Utility Layer

The `utils/` package contains functionality shared by multiple parts of the project.

## `utils/constants.py`

Contains application-wide constants.

Examples:

```text
APPLICATION_NAME
SUPPORTED_CHARACTERS
MAX_HISTORY_SIZE
MORSE_WORD_SEPARATOR
```

Constants should be centralized instead of repeatedly defined throughout the project.

---

## `utils/helpers.py`

Contains small general-purpose helper functions that do not belong specifically to the translation, validation, formatting, history, or interface layers.

Helper functions should remain limited in scope to avoid turning this module into a miscellaneous collection of unrelated functionality.

---

# 12. Testing Architecture

The `tests/` package contains automated tests for the application's components.

```text
tests/
├── test_translator.py
├── test_encoder.py
├── test_decoder.py
├── test_validator.py
├── test_history.py
└── test_helpers.py
```

Testing is organized around functionality rather than putting every test into one large file.

The test suite should verify:

* Correct English-to-Morse translation
* Correct Morse-to-English translation
* Individual encoder behavior
* Individual decoder behavior
* Invalid input handling
* History management
* Helper function behavior

Testing should focus on behavior and expected results rather than implementation details.

---

# 13. Documentation Architecture

The `docs/` directory contains detailed documentation for each major package.

```text
docs/
├── architecture.md
├── core.md
├── validation.md
├── formatting.md
├── history.md
├── interface.md
├── utils.md
└── tests.md
```

The documentation is intentionally separate from the source code.

Each document explains:

* Purpose of the package
* Files contained within it
* Responsibilities
* Important classes/functions
* Data flow
* Design decisions
* Testing considerations

`architecture.md` provides the overall project-level view, while the other documents provide deeper explanations of individual packages.

---

# 14. Data Flow

A typical English-to-Morse translation follows this process:

```text
User Input
    │
    ▼
GUI
    │
    ▼
English Validator
    │
    ├── Invalid ──► Error Message
    │
    ▼
Translator
    │
    ▼
Encoder
    │
    ▼
Morse Code Mapping
    │
    ▼
Morse Formatter
    │
    ▼
Translation Result
    │
    ├──────────────► GUI Output
    │
    ▼
History Manager
```

For Morse-to-English translation:

```text
User Input
    │
    ▼
GUI
    │
    ▼
Morse Validator
    │
    ├── Invalid ──► Error Message
    │
    ▼
Translator
    │
    ▼
Decoder
    │
    ▼
Morse Code Mapping
    │
    ▼
Text Formatter
    │
    ▼
Translation Result
    │
    ├──────────────► GUI Output
    │
    ▼
History Manager
```

---

# 15. Separation of Responsibilities

A major design principle of the project is separation of responsibilities.

| Package       | Responsibility          |
| ------------- | ----------------------- |
| `core/`       | Translation             |
| `validation/` | Input validation        |
| `formatting/` | Input/output formatting |
| `history/`    | Translation history     |
| `interface/`  | GUI                     |
| `utils/`      | Shared utilities        |
| `tests/`      | Automated testing       |
| `docs/`       | Documentation           |

For example, the GUI should never need to know how Morse Code is encoded.

Likewise, the encoder should not need to know how a Tkinter button works.

This reduces coupling and makes the application easier to modify.

---

# 16. Design Principles

The project follows several basic software engineering principles:

### Single Responsibility

Each module should have a focused purpose.

For example, `encoder.py` should encode text rather than handling GUI events or managing history.

### Separation of Concerns

Different concerns are separated into different packages.

### Reusability

Core translation functionality should be usable independently of the GUI.

This means a future command-line interface could potentially use the same translator.

### Testability

Core functionality should be accessible without launching the graphical interface, allowing it to be tested independently.

### Maintainability

Constants, formatting rules, validation rules, and GUI styling are separated so that changes can be made without modifying unrelated components.

---

# 17. Future Extensibility

The architecture leaves room for future improvements without requiring major restructuring.

Possible future features include:

* Command-line interface
* Morse Code audio playback
* Morse Code audio input
* Additional character sets
* Translation statistics
* Exporting translation history
* Importing translation history
* Theme selection
* Dark mode
* Keyboard shortcuts
* More advanced automated testing

These features should only be added if they provide meaningful value to the project.

---

# 18. Architectural Philosophy

The project intentionally avoids excessive complexity.

Although the application is divided into several modules, each module exists because it represents a distinct responsibility.

The goal is not to create an enterprise-level architecture for a simple translator. Instead, the goal is to create a project that demonstrates practical understanding of Python software organization, modular design, testing, and maintainability.

The architecture can therefore grow with the developer's understanding while remaining simple enough to fully understand and maintain.
