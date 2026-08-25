# __init__.py

# Translation history package for the Morse Translator

# Contains translation history records, history management functionality,
# history retrieval, record removal, and history clearing utilities used
# throughout the application

# Modules
# translation_record - Data model representing an individual translation
# history_manager - Management and storage of translation history

from .translation_record import (
    TranslationRecord,
)

from .history_manager import (
    HistoryManager,
)

__all__ = [
    # Translation Record
    "TranslationRecord",
    # History Management
    "HistoryManager"
]

