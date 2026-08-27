# History Package Documentation

## Overview

The `history/` package contains the translation-history system used throughout the Morse Translator.

It provides the data model and management functionality required to record completed translations, retrieve previous translations, search and filter history, remove individual records, clear stored history, and convert history records into serializable data.

The package is intentionally separated from the `core/` translation package. The core package is responsible for performing translations, while the history package is responsible for remembering and organizing translations that have already been performed.

```text
history/

├── __init__.py
├── history_manager.py
└── translation_record.py
```

# Package Responsibilities

The `history/` package is responsible for:

* Representing individual translation-history records.
* Assigning unique identifiers to history records.
* Storing completed translations.
* Retrieving individual records.
* Retrieving the newest records.
* Retrieving the oldest records.
* Searching through translation history.
* Filtering records using custom conditions.
* Filtering records by translation direction.
* Removing individual records.
* Clearing the complete history.
* Limiting the number of stored records.
* Automatically removing the oldest records when the history limit is exceeded.
* Converting records into dictionary representations.
* Loading history from serialized dictionary data.
* Providing basic history statistics.
* Providing human-readable history summaries.
* Exposing the history API to other packages.

The package does **not** handle:

* Performing Morse Code translations.
* Encoding English into Morse Code.
* Decoding Morse Code into English.
* Validating translation input.
* Formatting translation output.
* Rendering the graphical interface.
* Managing GUI components.
* Handling application styling.
* Running the command-line application.
* Persisting history directly to files or databases.

Those responsibilities belong to other packages in the project.

# Module Structure

## `__init__.py`

The package initializer provides the public interface for the `history/` package.

It exposes the primary classes required by other parts of the Morse Translator.

The initializer provides access to:

* `TranslationRecord`
* `HistoryManager`

### Purpose

The initializer provides a centralized package-level interface while keeping the implementation separated into individual modules.

Other parts of the application can therefore import the history functionality without needing to understand the internal organization of the package.

For example:

```python
from history import HistoryManager, TranslationRecord
```

Specialized functionality can still be imported directly from its corresponding module when necessary.

# `translation_record.py`

`translation_record.py` contains the `TranslationRecord` data model.

A `TranslationRecord` represents one completed translation performed by the Morse Translator.

It stores the information necessary to describe and later retrieve a translation-history entry.

## `TranslationRecord`

The `TranslationRecord` class is the primary data structure of the history package.

A record contains information such as:

* Original input.
* Translation output.
* Translation direction.
* Timestamp.
* Record ID.
* Character count.
* Word count.
* Additional metadata.

Conceptually, a record can be represented as:

```text
TranslationRecord

├── record_id
├── input_text
├── output_text
├── direction
├── timestamp
├── character_count
├── word_count
└── metadata
```

## Record Attributes

### `input_text`

Stores the original text supplied to the translator.

For English-to-Morse translation, this would contain the original English text.

For Morse-to-English translation, this would contain the original Morse Code input.

### `output_text`

Stores the result produced by the translation process.

### `direction`

Stores the direction of the translation.

Examples include:

```text
English → Morse
Morse → English
```

The exact direction representation is determined by the core translation system.

### `timestamp`

Stores the date and time at which the history record was created.

The default timestamp is generated automatically when a `TranslationRecord` is created.

### `record_id`

Stores the unique identifier assigned to the history record.

The ID can initially be `None` and is normally assigned by `HistoryManager` when the record is added to history.

### `character_count`

Stores the number of characters associated with the translation.

This allows the history manager to provide aggregate character statistics.

### `word_count`

Stores the number of words associated with the translation.

This allows the history manager to provide aggregate word statistics.

### `metadata`

Stores optional additional information associated with the translation.

Metadata can be used to store application-specific information without changing the primary structure of the record.

For example:

```python
{
    "source": "GUI",
    "language": "English",
}
```

## `TranslationRecord` Validation

The record performs basic structural validation when it is created.

This includes checking that:

* Input text is a string.
* Output text is a string.
* Direction is a string.
* Timestamp is a `datetime`.
* Record IDs are valid integers when provided.
* Character counts are non-negative integers.
* Word counts are non-negative integers.
* Metadata is stored as a dictionary.
* Translation direction is not empty.

This validation protects the integrity of history records.

It does not replace the application's dedicated validation package.

# Record Information Methods

## `is_empty()`

Determines whether the record contains an empty input or output.

The method checks the input and output after removing surrounding whitespace.

It returns:

```text
True
```

when either side is empty.

Otherwise it returns:

```text
False
```

This provides a simple way for the history system to identify incomplete records.

## `has_metadata()`

Determines whether additional metadata has been stored in the record.

It returns `True` when the metadata dictionary contains at least one entry.

## `add_metadata()`

Adds a metadata value to the record.

If the specified key already exists, its value is replaced.

For example:

```python
record.add_metadata(
    "source",
    "GUI",
)
```

## `get_metadata()`

Retrieves a metadata value using its key.

A default value can be supplied when the key does not exist.

## `remove_metadata()`

Removes a metadata entry from the record.

The method returns `True` when an entry was successfully removed and `False` when the requested key did not exist.

# Serialization

## `to_dict()`

Converts a `TranslationRecord` into a dictionary.

The method converts the timestamp into ISO 8601 string format so the resulting structure can be serialized into formats such as JSON.

Conceptually:

```text
TranslationRecord
       │
       ▼
    to_dict()
       │
       ▼
 Dictionary
       │
       ▼
 JSON / Storage
```

This creates a clean boundary between the application's object-oriented history system and external storage formats.

## `from_dict()`

Creates a `TranslationRecord` from dictionary data.

It performs the reverse operation of `to_dict()`.

Conceptually:

```text
JSON / Storage
       │
       ▼
 Dictionary
       │
       ▼
  from_dict()
       │
       ▼
TranslationRecord
```

This allows previously serialized history records to be reconstructed.

# Display Methods

## `summary()`

Creates a short human-readable representation of the translation.

The summary contains the translation direction, original input, and translated output.

For example:

```text
English → Morse: Hello → .... . .-.. .-.. ---
```

The summary is useful for displaying compact history entries.

## `__str__()`

Provides the normal string representation of a `TranslationRecord`.

It uses the record's summary representation.

## `__repr__()`

Provides a developer-oriented representation of the record.

This is useful when debugging or inspecting records during development.

# `history_manager.py`

`history_manager.py` contains the `HistoryManager` class.

The manager provides the main system for storing and manipulating multiple `TranslationRecord` objects.

While `TranslationRecord` represents one translation, `HistoryManager` represents the collection of translations.

Conceptually:

```text
TranslationRecord
       │
       │
       ▼
HistoryManager
       │
       ├── Add
       ├── Retrieve
       ├── Search
       ├── Filter
       ├── Remove
       ├── Clear
       └── Serialize
```

# `HistoryManager`

The `HistoryManager` class maintains translation records in chronological order.

The manager stores records in memory and provides controlled methods for interacting with them.

It also supports an optional maximum history size.

The default maximum is:

```text
100 records
```

The limit can be changed or disabled.

# History Configuration

## `max_records`

Stores the maximum number of records the history manager should retain.

For example:

```python
manager = HistoryManager(
    max_records=50
)
```

This limits history to 50 records.

An unlimited history can be configured with:

```python
manager = HistoryManager(
    max_records=None
)
```

## `record_count`

Returns the current number of records stored by the manager.

For example:

```python
count = manager.record_count
```

## `is_empty`

Determines whether the history currently contains any records.

This provides a convenient way for interfaces to determine whether there is history to display.

# Adding Records

## `add_record()`

Adds an existing `TranslationRecord` to the history.

If the record does not have an ID, the manager assigns one automatically.

The method also enforces the configured history limit.

For example:

```python
manager.add_record(record)
```

## `create_record()`

Creates a new `TranslationRecord` and immediately adds it to the history.

This is a convenience method that avoids requiring callers to manually create a record first.

For example:

```python
record = manager.create_record(
    input_text="SOS",
    output_text="... --- ...",
    direction="English → Morse",
)
```

The resulting record is automatically stored in the manager.

# Record Retrieval

## `get_record()`

Retrieves a record using its unique ID.

For example:

```python
record = manager.get_record(3)
```

If the ID does not exist, the method returns:

```text
None
```

## `get_records()`

Returns all records currently stored in the manager.

A copy of the internal list is returned rather than exposing the internal collection directly.

This prevents callers from accidentally modifying the manager's internal data structure.

## `get_latest()`

Returns the most recently stored records.

For example:

```python
latest = manager.get_latest(5)
```

The results are returned from newest to oldest.

## `get_oldest()`

Returns the oldest records currently stored.

For example:

```python
oldest = manager.get_oldest(5)
```

The results are returned from oldest to newest.

# Searching and Filtering

## `search()`

Searches the translation history using a text query.

The search checks:

* Original input.
* Translation output.
* Translation direction.

The search is case-insensitive.

For example:

```python
results = manager.search("hello")
```

This can find records where `"hello"` appears in the input, output, or direction.

An empty search query returns an empty result rather than returning every record.

## `filter()`

Allows callers to provide a custom filtering function.

For example:

```python
results = manager.filter(
    lambda record: record.character_count > 10
)
```

This makes the history system extensible without requiring additional built-in filtering methods for every possible condition.

## `get_by_direction()`

Returns records matching a particular translation direction.

For example:

```python
results = manager.get_by_direction(
    "English → Morse"
)
```

Direction comparison is case-insensitive.

# Removing History

## `remove_record()`

Removes a specific record using its record ID.

The method returns:

```text
True
```

when a record is successfully removed.

It returns:

```text
False
```

when no matching record exists.

## `clear()`

Removes every record from the history.

The record ID counter is also reset so that a newly created history begins again with record ID `1`.

Conceptually:

```text
Existing History

Record 1
Record 2
Record 3
Record 4

        │
        ▼

      clear()

        │
        ▼

Empty History
```

# History Limits

## `set_max_records()`

Changes the maximum number of records that can be retained.

For example:

```python
manager.set_max_records(25)
```

The manager immediately enforces the new limit.

If the history already contains more records than the new limit, the oldest records are removed first.

The limit can also be removed:

```python
manager.set_max_records(None)
```

This allows unlimited history.

## `_enforce_limit()`

`_enforce_limit()` is an internal helper used by the history manager.

It checks whether the current history exceeds the configured maximum.

When it does, the oldest records are removed until the history is within the limit.

The method is intentionally internal and is not part of the primary public API.

# Serialization

## `to_list()`

Converts the entire history into a list of dictionaries.

Each `TranslationRecord` is converted using its `to_dict()` method.

The resulting structure can be passed to a JSON-based storage system.

Conceptually:

```text
HistoryManager
      │
      ▼
  to_list()
      │
      ▼
List[Dictionary]
      │
      ▼
JSON / File Storage
```

## `load_from_list()`

Loads serialized history records from a list of dictionaries.

The existing history is cleared before the new records are loaded.

Each dictionary is reconstructed using:

```text
TranslationRecord.from_dict()
```

The resulting records are then added through the normal history-management process.

# History Statistics

## `total_characters()`

Returns the total number of characters represented across all stored records.

This can be useful for statistics or application dashboards.

For example:

```text
Record 1 → 5 characters
Record 2 → 8 characters
Record 3 → 4 characters

Total → 17 characters
```

## `total_words()`

Returns the total number of words represented across all stored records.

This provides a simple aggregate statistic for the translation history.

# Display Utilities

## `summaries()`

Returns a list of human-readable summaries for every stored translation record.

This is useful when an interface needs compact representations of history entries.

For example:

```text
English → Morse: SOS → ... --- ...

English → Morse: Hello → .... . .-.. .-.. ---

Morse → English: ... --- ... → SOS
```

# Python Protocol Methods

The `HistoryManager` implements several Python protocol methods to make the class easier to use.

## `__len__()`

Allows Python's built-in `len()` function to be used with the history manager.

For example:

```python
len(manager)
```

returns the number of stored records.

## `__iter__()`

Allows the history manager to be iterated over directly.

For example:

```python
for record in manager:
    print(record)
```

Records are returned from oldest to newest.

## `__contains__()`

Allows the `in` operator to be used to check whether a record ID exists.

For example:

```python
if 5 in manager:
    print("Record exists.")
```

# History Architecture

The history package follows a simple two-layer structure.

```text
                    history/

                       │

             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼

    translation_record.py   history_manager.py
             │                   │
             │                   │
             ▼                   ▼
    TranslationRecord      HistoryManager
             │                   │
             └─────────┬─────────┘
                       │
                       ▼
              Translation History
```

`TranslationRecord` defines what a history entry looks like.

`HistoryManager` defines how multiple history entries are managed.

This separation keeps the data model independent from the collection-management logic.

# Translation History Flow

A normal translation-history workflow follows this structure:

```text
User Input
    │
    ▼
Core Translator
    │
    ▼
Translation Result
    │
    ▼
TranslationRecord
    │
    ▼
HistoryManager
    │
    ├── Store
    ├── Search
    ├── Retrieve
    ├── Filter
    └── Remove
    │
    ▼
Interface
```

The history package therefore operates **after** the translation has been performed.

It does not perform the translation itself.

# Relationship With Other Packages

The `history/` package interacts primarily with the `core/` and `interface/` packages.

```text
                    Morse Translator

                           │

                           ▼

                         core/
                           │
                           │
                    Translation Result
                           │
                           ▼
                       history/
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
            TranslationRecord   HistoryManager
                  │                 │
                  └────────┬────────┘
                           │
                           ▼
                      interface/
```

## `core/`

The `core/` package performs the actual English-to-Morse and Morse-to-English translation.

The history package can store the results produced by the core translation system.

The dependency should remain primarily one-directional:

```text
core
 │
 ▼
history
```

The history system should not contain translation algorithms.

## `validation/`

The validation package determines whether translation input is valid.

History records should contain already-processed translation information rather than replacing the application's validation system.

```text
Input
 │
 ▼
validation
 │
 ▼
core
 │
 ▼
history
```

## `formatting/`

The formatting package prepares text and Morse Code for consistent presentation.

History may store formatted translation results when appropriate, but formatting itself remains outside the history package.

## `interface/`

The interface package can use the history manager to display previous translations.

For example, a GUI could provide:

```text
Translation History

1. Hello → .... . .-.. .-.. ---
2. SOS → ... --- ...
3. Test → - . ... -
```

The interface should request information from `HistoryManager` rather than directly manipulating its internal record list.

## `utils/`

The utilities package can provide shared constants and helper functionality used by the history system.

## `tests/`

The test package verifies that the history system behaves correctly.

History tests should cover both individual records and manager behavior.

# Design Principles

## Separation of Concerns

The history system is separated from the translation engine.

```text
core/
    ↓
Translation

history/
    ↓
Translation Memory
```

The core package determines **what the translation is**.

The history package determines **what previous translations should be remembered**.

This prevents the translation engine from becoming responsible for storage and history management.

## Data Integrity

`TranslationRecord` performs structural validation before records enter the history system.

This helps ensure that history entries have consistent data.

## Encapsulation

`HistoryManager` keeps its internal record collection private.

The manager exposes methods such as:

```text
add_record()
get_record()
get_records()
remove_record()
clear()
search()
filter()
```

rather than requiring external components to manipulate the underlying list directly.

## Reusability

The history system can be used by multiple interfaces.

For example:

```text
             HistoryManager
              /     |     \
             /      |      \
           GUI     CLI    Tests
```

The same history functionality can therefore support different application interfaces.

## Extensibility

The use of metadata and custom filtering allows the history system to support additional functionality without requiring major changes to its core structure.

For example, future versions could store:

* Translation source.
* Application mode.
* Processing duration.
* Character statistics.
* User-selected settings.
* Formatting information.

# Example Usage

## Creating a History Manager

```python
from history import HistoryManager

history = HistoryManager()
```

The manager begins with an empty history.

## Creating a Record

```python
record = history.create_record(
    input_text="SOS",
    output_text="... --- ...",
    direction="English → Morse",
)
```

The record is automatically assigned an ID and stored in the history.

## Retrieving Records

```python
records = history.get_records()

for record in records:
    print(record)
```

## Getting the Latest Translation

```python
latest = history.get_latest()

if latest:
    print(latest[0])
```

## Searching History

```python
results = history.search("SOS")

for record in results:
    print(record)
```

## Removing a Record

```python
history.remove_record(1)
```

## Clearing History

```python
history.clear()
```

# Error Handling

The history package performs structural validation and raises appropriate Python exceptions when invalid values are supplied.

Typical validation includes:

* Ensuring records are `TranslationRecord` objects.
* Ensuring record IDs are integers.
* Ensuring history limits are valid.
* Ensuring search queries are strings.
* Ensuring filter predicates are callable.
* Ensuring serialized history data is supplied as a list.
* Ensuring record dictionaries contain valid values.

Examples of errors include:

```text
TypeError
ValueError
```

The history package focuses on errors related to history structures and operations.

Translation-specific input errors remain the responsibility of the `validation/` and `core/` packages.

# Testing Strategy

The history package should be tested for both normal and edge-case behavior.

Important test categories include:

* Creating translation records.
* Validating record attributes.
* Creating records through `HistoryManager`.
* Adding records.
* Automatically assigning IDs.
* Retrieving records.
* Retrieving the latest records.
* Retrieving the oldest records.
* Searching history.
* Filtering history.
* Filtering by direction.
* Removing records.
* Clearing history.
* Enforcing maximum history size.
* Changing the history limit.
* Serializing records.
* Reconstructing records.
* Loading serialized history.
* Calculating character totals.
* Calculating word totals.
* Generating summaries.
* Testing Python protocol methods.

Example:

```text
Test Input
    │
    ▼
HistoryManager
    │
    ▼
Expected Record
    │
    ▼
Assertion
```

# Future Expansion

The history package can be expanded as the Morse Translator becomes more sophisticated.

Potential future functionality includes:

* Persistent history files.
* JSON history storage.
* CSV history export.
* Importing previous translation sessions.
* History timestamps and date filtering.
* Favorites.
* Pinned translations.
* Translation categories.
* History statistics.
* History pagination.
* Duplicate detection.
* History sorting.
* Search highlighting.
* Exporting selected history entries.
* Automatic history cleanup.
* Session-based history.
* Undo and restore functionality.

Persistent storage should ideally be implemented in a separate module or package rather than placing file-handling logic directly inside `HistoryManager`.

This keeps the current in-memory history system simple while leaving room for future expansion.

# Module Dependency Guidelines

The history package should maintain a simple dependency structure.

```text
translation_record.py
        │
        ▼
history_manager.py
        │
        ▼
interface / application
```

`translation_record.py` should remain independent of `history_manager.py`.

`history_manager.py` may depend on `TranslationRecord`.

The package should avoid dependencies on:

```text
GUI
CLI
File storage
Application startup
```

This minimizes circular dependencies and keeps the history package reusable.

# Public API

The public history API consists primarily of:

```python
TranslationRecord
HistoryManager
```

These are exposed through:

```python
from history import (
    TranslationRecord,
    HistoryManager,
)
```

Individual modules remain available when direct access is necessary:

```python
from history.translation_record import TranslationRecord

from history.history_manager import HistoryManager
```

# Example Application Flow

A complete translation and history workflow can look like:

```text
User enters text
       │
       ▼
Input Validation
       │
       ▼
Core Translator
       │
       ▼
Translation Result
       │
       ▼
Create TranslationRecord
       │
       ▼
HistoryManager.add_record()
       │
       ▼
History Stored
       │
       ├──────────────► Display Current Result
       │
       └──────────────► Update History Interface
```

This architecture allows the user interface to display both the current translation and previous translations without placing history logic inside the translation engine.

# Summary

The `history/` package provides the **translation-history layer** of the Morse Translator.

Its primary components are:

```text
history/

├── __init__.py
│
├── translation_record.py
│       │
│       └── TranslationRecord
│
└── history_manager.py
        │
        └── HistoryManager
```

The package separates two important responsibilities:

```text
TranslationRecord
        │
        ▼
Defines one history entry


HistoryManager
        │
        ▼
Manages multiple history entries
```

The resulting architecture keeps the project modular:

```text
                     Morse Translator

                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
           core      validation   formatting
             │
             ▼
       Translation Result
             │
             ▼
          history
             │
       ┌─────┴─────┐
       │           │
       ▼           ▼
    Record      Manager
       │           │
       └─────┬─────┘
             │
             ▼
         interface
```

The history package therefore provides a clean and reusable way to preserve previous translations while keeping the core Morse Code translation system independent from history storage and presentation.

Its current implementation is intentionally lightweight and in-memory, while its structured records, metadata support, serialization methods, filtering system, and configurable history limits provide a solid foundation for future expansion.

