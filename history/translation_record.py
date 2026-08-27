# translation_record.py
# Translation history record model for the Morse Translator

# Contains the data structure used to represent a single translation
# performed by the application, including the original input, translated
# output, translation direction, timestamp, and optional metadata

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional


# Translation Record

# A TranslationRecord represents one completed translation and provides
# a consistent structure for storing translation history.

@dataclass
class TranslationRecord:
    """
    Represents a single Morse Translator translation-history entry.

    A record stores the original input, resulting output, translation
    direction, timestamp, and optional metadata about the operation.
    """

    input_text: str
    output_text: str
    direction: str
    timestamp: datetime = field(default_factory=datetime.now)
    record_id: Optional[int] = None
    character_count: int = 0
    word_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Normalize and validate the values stored in the record.

        Basic structural validation is performed here so that history
        entries remain internally consistent. Full translation input
        validation remains the responsibility of the validation package.
        """

        if not isinstance(self.input_text, str):
            raise TypeError("Input text must be a string.")

        if not isinstance(self.output_text, str):
            raise TypeError("Output text must be a string.")

        if not isinstance(self.direction, str):
            raise TypeError("Translation direction must be a string.")

        if not isinstance(self.timestamp, datetime):
            raise TypeError("Timestamp must be a datetime object.")

        if self.record_id is not None:
            if not isinstance(self.record_id, int):
                raise TypeError("Record ID must be an integer or None.")

            if self.record_id < 0:
                raise ValueError("Record ID cannot be negative.")

        if not isinstance(self.character_count, int):
            raise TypeError("Character count must be an integer.")

        if self.character_count < 0:
            raise ValueError("Character count cannot be negative.")

        if not isinstance(self.word_count, int):
            raise TypeError("Word count must be an integer.")

        if self.word_count < 0:
            raise ValueError("Word count cannot be negative.")

        if not isinstance(self.metadata, dict):
            raise TypeError("Metadata must be a dictionary.")

        self.direction = self.direction.strip()

        if not self.direction:
            raise ValueError("Translation direction cannot be empty.")

    # Record Information

    def is_empty(self) -> bool:
        """
        Determine whether the record contains an empty input or output.

        Returns:
            True if either the input or output is empty after stripping
            surrounding whitespace, otherwise False.
        """

        return not self.input_text.strip() or not self.output_text.strip()

    def has_metadata(self) -> bool:
        """
        Determine whether the record contains additional metadata.

        Returns:
            True when at least one metadata entry exists.
        """

        return bool(self.metadata)

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add or update a metadata value.

        Args:
            key: Metadata key.
            value: Value associated with the key.
        """

        if not isinstance(key, str):
            raise TypeError("Metadata key must be a string.")

        key = key.strip()

        if not key:
            raise ValueError("Metadata key cannot be empty.")

        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a metadata value.

        Args:
            key: Metadata key to retrieve.
            default: Value returned when the key does not exist.

        Returns:
            The stored metadata value or the supplied default.
        """

        return self.metadata.get(key, default)

    def remove_metadata(self, key: str) -> bool:
        """
        Remove a metadata value from the record.

        Args:
            key: Metadata key to remove.

        Returns:
            True if the key existed and was removed, otherwise False.
        """

        if key in self.metadata:
            del self.metadata[key]
            return True

        return False

    # Serialization

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the translation record into a dictionary.

        The timestamp is converted to ISO 8601 format so that the result
        can be serialized safely to JSON or another storage format.

        Returns:
            Dictionary representation of the translation record.
        """

        return {
            "record_id": self.record_id,
            "input_text": self.input_text,
            "output_text": self.output_text,
            "direction": self.direction,
            "timestamp": self.timestamp.isoformat(),
            "character_count": self.character_count,
            "word_count": self.word_count,
            "metadata": dict(self.metadata),
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "TranslationRecord":
        """
        Create a TranslationRecord from a dictionary.

        Args:
            data: Dictionary containing serialized record information.

        Returns:
            A reconstructed TranslationRecord instance.
        """

        if not isinstance(data, dict):
            raise TypeError("Record data must be a dictionary.")

        timestamp = data.get("timestamp")

        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)

        elif timestamp is None:
            timestamp = datetime.now()

        elif not isinstance(timestamp, datetime):
            raise TypeError(
                "Timestamp must be an ISO-formatted string or datetime."
            )

        return cls(
            record_id=data.get("record_id"),
            input_text=data.get("input_text", ""),
            output_text=data.get("output_text", ""),
            direction=data.get("direction", ""),
            timestamp=timestamp,
            character_count=data.get("character_count", 0),
            word_count=data.get("word_count", 0),
            metadata=dict(data.get("metadata", {})),
        )

    # Display Formatting

    def summary(self) -> str:
        """
        Return a short human-readable description of the record.

        Returns:
            A concise summary suitable for history displays.
        """

        return (
            f"{self.direction}: "
            f"{self.input_text} → {self.output_text}"
        )

    def __str__(self) -> str:
        """
        Return a readable representation of the translation record.
        """

        return self.summary()

    def __repr__(self) -> str:
        """
        Return a developer-oriented representation of the record.
        """

        return (
            "TranslationRecord("
            f"record_id={self.record_id!r}, "
            f"input_text={self.input_text!r}, "
            f"output_text={self.output_text!r}, "
            f"direction={self.direction!r}, "
            f"timestamp={self.timestamp!r}"
            ")"
        )


# Public Module Interface

__all__ = [
    "TranslationRecord",
]

