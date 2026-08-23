# Morse Translator

A modular Python Morse Code translator supporting **English ↔ Morse Code translation**, input validation, translation history, automated testing, and a Tkinter graphical interface.

---

## Overview

**Morse Translator** is a Python application that converts text between English and Morse Code in both directions.

The project is designed as a practical software-development project rather than a simple dictionary-based converter. It separates translation, validation, formatting, history management, and user-interface functionality into independent modules.

The project also includes automated tests and detailed technical documentation covering the architecture and individual components.

---

## Features

### Translation

* English → Morse Code
* Morse Code → English
* Support for letters
* Support for numbers
* Support for selected punctuation
* Word separation
* Character separation

### Input Validation

* English input validation
* Morse Code validation
* Invalid character detection
* Invalid Morse sequence detection
* Empty-input handling
* User-friendly error handling

### Translation History

* Store previous translations
* View recent translations
* Clear translation history
* Associate translations with their direction and timestamp

### Graphical Interface

* Tkinter-based GUI
* Translation direction selection
* Input text area
* Output text area
* Translate functionality
* Clear functionality
* Copy-to-clipboard functionality
* Translation history display

### Development

* Modular Python architecture
* Unit tests
* Centralized constants
* Detailed architecture documentation
* Package-level documentation
* Clean separation of responsibilities

---

## Example

### English → Morse

**Input:**

```text
HELLO WORLD
```

**Output:**

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Morse → English

**Input:**

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

**Output:**

```text
HELLO WORLD
```

---

## Project Structure

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

## Architecture

The application is divided into several packages, each responsible for a specific part of the system.

```text
                         ┌─────────────┐
                         │   main.py   │
                         └──────┬──────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    interface/  │
                       │    Tkinter GUI │
                       └────────┬────────┘
                                │
                ┌───────────────┼────────────────┐
                │               │                │
                ▼               ▼                ▼
         ┌────────────┐  ┌────────────┐  ┌────────────┐
         │ validation │  │    core    │  │  history   │
         └────────────┘  └─────┬──────┘  └────────────┘
                               │
                    ┌──────────┼──────────┐
                    ▼          ▼          ▼
                 Encoder    Decoder   Morse Map
                    │          │          │
                    └──────────┼──────────┘
                               ▼
                        ┌─────────────┐
                        │ formatting/ │
                        └─────────────┘
```

The main translation engine is independent of the graphical interface, allowing the core functionality to be tested and potentially reused by another interface in the future.

For a detailed explanation of the architecture, see [`docs/architecture.md`](docs/architecture.md).

---

## Technologies

### Language

**Python 3**

### GUI

**Tkinter**

Tkinter is included with standard Python installations and is used to create the desktop interface.

### Testing

Python's testing tools will be used to verify the behavior of the translation engine, validators, formatting utilities, and history system.

### Project Management

* Git
* GitHub
* Markdown
* Python virtual environments

---

## Requirements

The project is designed to rely primarily on Python's standard library.

Recommended:

```text
Python 3.11+
```

No external GUI framework is required because the application uses Tkinter.

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Enter the project directory

```bash
cd morse-translator
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the application using:

```bash
python main.py
```

The Tkinter interface will open and allow you to select a translation direction and enter text.

---

## Running Tests

Run the project's automated tests with:

```bash
python -m unittest discover
```

Individual test modules can also be executed separately.

Example:

```bash
python -m unittest tests.test_translator
```

---

## Supported Morse Code

The initial implementation is intended to support:

### Letters

```text
A B C D E F G H I J K L M
N O P Q R S T U V W X Y Z
```

### Numbers

```text
0 1 2 3 4 5 6 7 8 9
```

### Punctuation

Common punctuation can be supported as the project develops.

The exact supported character set is maintained by the Morse Code mapping and validation modules.

---

## Translation Rules

The application uses standard Morse Code representations.

Characters within a word are separated by spaces:

```text
.... . .-.. .-.. ---
```

Words are separated using:

```text
/
```

For example:

```text
HELLO WORLD
```

becomes:

```text
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

---

## Design Philosophy

The project intentionally uses a modular architecture.

Instead of placing the entire application inside one large Python file, functionality is separated into focused packages:

```text
core/
```

Handles translation.

```text
validation/
```

Handles input checking.

```text
formatting/
```

Handles text and Morse formatting.

```text
history/
```

Handles previous translations.

```text
interface/
```

Handles the graphical interface.

```text
utils/
```

Contains shared constants and helper functionality.

```text
tests/
```

Contains automated tests.

```text
docs/
```

Contains detailed technical documentation.

This structure makes the project easier to understand, test, maintain, and extend.

---

## Documentation

Detailed documentation is available in the `docs/` directory.

| Document          | Description                             |
| ----------------- | --------------------------------------- |
| `architecture.md` | Overall project architecture and design |
| `core.md`         | Translation engine documentation        |
| `validation.md`   | Input validation documentation          |
| `formatting.md`   | Formatting system documentation         |
| `history.md`      | Translation history documentation       |
| `interface.md`    | Tkinter GUI documentation               |
| `utils.md`        | Shared utilities documentation          |
| `tests.md`        | Testing architecture and strategy       |

---

## Testing Strategy

Testing focuses on individual components as well as the behavior of the translation system.

Important test cases include:

* Basic English-to-Morse translation
* Basic Morse-to-English translation
* Single characters
* Words
* Sentences
* Numbers
* Supported punctuation
* Invalid English input
* Invalid Morse input
* Empty input
* History operations
* Formatting behavior

The goal is to ensure that translation results are correct while also verifying that invalid input is handled safely.

---

## Future Improvements

Potential future additions include:

* Morse Code audio playback
* Morse Code audio decoding
* Command-line interface
* Dark mode
* Keyboard shortcuts
* Export translation history
* Import translation history
* Translation statistics
* Customizable GUI themes
* Expanded punctuation support
* Additional automated tests

Future features will only be added when they provide meaningful functionality without unnecessarily complicating the application.

---

## Learning Objectives

This project is intended to provide practical experience with:

* Python dictionaries
* String manipulation
* Functions
* Object-oriented programming
* Python modules and packages
* Input validation
* Error handling
* GUI development with Tkinter
* Unit testing
* Software architecture
* Code organization
* Documentation
* Git and GitHub workflows

The project is intentionally designed to remain understandable while demonstrating more advanced organization than a basic single-file Python application.

---

## License

This project is distributed under the **MIT License**.

See [`LICENSE`](LICENSE) for the complete license text.

---

## Author

Created as a personal Python software-development project while transitioning from freshman to sophomore year as a Computer Science student.
