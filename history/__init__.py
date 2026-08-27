# __init__.py
# Translation history package for the Morse Translator

# Contains the data model and management system used to record,
# retrieve, search, filter, organize, serialize, and remove previous
# Morse Code translations throughout the application

# The history package is intentionally separated from the core
# translation engine so that translation logic does not need to
# manage storage, retrieval, or presentation of previous translations


# Modules
# translation_record - Data model representing an individual translation
# history_manager - Storage, retrieval, search, filtering, and management
#                   functionality for translation history


# Translation Record
# Provides the structured representation of a single history entry

from .translation_record import (
    TranslationRecord,
)


# History Management
# Provides the primary interface for managing collections of records

from .history_manager import (
    HistoryManager,
)


# Public Package Interface

# These names represent the functionality intended to be used by
# other packages throughout the Morse Translator project

# Internal implementation details remain accessible through their
# individual modules when specialized functionality is required

__all__ = [

    # Translation Record
    "TranslationRecord",

    # History Management
    "HistoryManager",

]