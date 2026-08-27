# history_manager.py
# Translation history management for the Morse Translator

# Contains the HistoryManager class used to store, retrieve, search,
# remove, clear, and organize TranslationRecord objects created by
# the translation workflow


from typing import Callable, List, Optional

from .translation_record import TranslationRecord


# History Manager
# Provides the main interface for managing translation history.
# Records are stored in memory and maintained in chronological order.

class HistoryManager:

    # Initializes the history manager.
    #
    # max_records determines the maximum number of records that can
    # be stored at one time. None allows unlimited history.

    def __init__(
        self,
        max_records: Optional[int] = 100,
    ) -> None:

        if max_records is not None:

            if not isinstance(max_records, int):
                raise TypeError(
                    "Maximum records must be an integer or None."
                )

            if isinstance(max_records, bool):
                raise TypeError(
                    "Maximum records must be an integer or None."
                )

            if max_records <= 0:
                raise ValueError(
                    "Maximum records must be greater than zero."
                )

        self._max_records = max_records
        self._records: List[TranslationRecord] = []
        self._next_id = 1


    # Properties

    @property
    def max_records(self) -> Optional[int]:
        # Returns the maximum number of records allowed.
        #
        # None indicates that the history has no size limit.

        return self._max_records


    @property
    def record_count(self) -> int:
        # Returns the number of translation records currently stored.

        return len(self._records)


    @property
    def is_empty(self) -> bool:
        # Determines whether the translation history is empty.

        return not self._records


    # Record Management

    def add_record(
        self,
        record: TranslationRecord,
    ) -> TranslationRecord:

        # Adds a TranslationRecord to the history.
        #
        # If the record does not have an ID, a unique ID is assigned.
        #
        # When a maximum history size is configured, the oldest records
        # are automatically removed when the limit is exceeded.

        if not isinstance(record, TranslationRecord):
            raise TypeError(
                "Record must be a TranslationRecord instance."
            )

        if record.record_id is None:
            record.record_id = self._next_id

        self._next_id = max(
            self._next_id,
            record.record_id + 1,
        )

        self._records.append(record)

        self._enforce_limit()

        return record


    def create_record(
        self,
        input_text: str,
        output_text: str,
        direction: str,
        character_count: int = 0,
        word_count: int = 0,
        metadata: Optional[dict] = None,
    ) -> TranslationRecord:

        # Creates a TranslationRecord and immediately adds it to history.
        #
        # This method provides a convenient alternative to manually
        # creating a TranslationRecord before calling add_record().

        record = TranslationRecord(
            input_text=input_text,
            output_text=output_text,
            direction=direction,
            character_count=character_count,
            word_count=word_count,
            metadata=metadata or {},
        )

        return self.add_record(record)


    def remove_record(
        self,
        record_id: int,
    ) -> bool:

        # Removes a translation record using its unique record ID.
        #
        # Returns True when a record was removed and False when no
        # matching record exists.

        record = self.get_record(record_id)

        if record is None:
            return False

        self._records.remove(record)

        return True


    def clear(self) -> None:

        # Removes every translation record from the history.
        #
        # The record ID counter is also reset so a new history begins
        # with record ID 1.

        self._records.clear()
        self._next_id = 1


    # Record Retrieval

    def get_record(
        self,
        record_id: int,
    ) -> Optional[TranslationRecord]:

        # Retrieves a translation record using its unique ID.
        #
        # Returns the matching TranslationRecord or None when the
        # requested record does not exist.

        if not isinstance(record_id, int):
            raise TypeError(
                "Record ID must be an integer."
            )

        for record in self._records:

            if record.record_id == record_id:
                return record

        return None


    def get_records(self) -> List[TranslationRecord]:

        # Returns all translation records currently stored.
        #
        # A copy of the internal list is returned so callers cannot
        # directly modify the manager's record collection.

        return list(self._records)


    def get_latest(
        self,
        count: int = 1,
    ) -> List[TranslationRecord]:

        # Returns the most recently added translation records.
        #
        # Records are returned from newest to oldest.

        if not isinstance(count, int):
            raise TypeError(
                "Count must be an integer."
            )

        if count < 0:
            raise ValueError(
                "Count cannot be negative."
            )

        if count == 0:
            return []

        return list(
            reversed(
                self._records[-count:]
            )
        )


    def get_oldest(
        self,
        count: int = 1,
    ) -> List[TranslationRecord]:

        # Returns the oldest translation records.
        #
        # Records are returned from oldest to newest.

        if not isinstance(count, int):
            raise TypeError(
                "Count must be an integer."
            )

        if count < 0:
            raise ValueError(
                "Count cannot be negative."
            )

        return list(
            self._records[:count]
        )


    # Search and Filtering

    def search(
        self,
        query: str,
    ) -> List[TranslationRecord]:
        # Searches translation history using a text query
        # The search checks the original input, translated output,
        # and translation direction
        # Matching is case-insensitive

        if not isinstance(query, str):
            raise TypeError(
                "Search query must be a string."
            )

        query = query.strip().lower()

        if not query:
            return []

        return [
            record
            for record in self._records
            if (
                query in record.input_text.lower()
                or query in record.output_text.lower()
                or query in record.direction.lower()
            )
        ]


    def filter(
        self,
        predicate: Callable[[TranslationRecord], bool],
    ) -> List[TranslationRecord]:
        # Filters translation records using a custom predicate function
        # The predicate receives each TranslationRecord and determines
        # whether that record should be included in the result

        if not callable(predicate):
            raise TypeError(
                "Predicate must be callable."
            )

        return [
            record
            for record in self._records
            if predicate(record)
        ]


    def get_by_direction(
        self,
        direction: str,
    ) -> List[TranslationRecord]:
        # Returns all records matching a translation direction
        # Direction comparison is case-insensitive

        if not isinstance(direction, str):
            raise TypeError(
                "Direction must be a string."
            )

        normalized_direction = direction.strip().lower()

        if not normalized_direction:
            return []

        return [
            record
            for record in self._records
            if record.direction.lower() == normalized_direction
        ]


    # History Configuration

    def set_max_records(
        self,
        max_records: Optional[int],
    ) -> None:
        # Changes the maximum number of records retained by the manager
        # None removes the history size limit
        # If the new limit is smaller than the current history size,
        # the oldest records are removed automatically

        if max_records is not None:

            if not isinstance(max_records, int):
                raise TypeError(
                    "Maximum records must be an integer or None."
                )

            if isinstance(max_records, bool):
                raise TypeError(
                    "Maximum records must be an integer or None."
                )

            if max_records <= 0:
                raise ValueError(
                    "Maximum records must be greater than zero."
                )

        self._max_records = max_records

        self._enforce_limit()


    def _enforce_limit(self) -> None:
        # Internal helper that ensures the history does not exceed
        # the configured maximum number of records
        # The oldest records are removed first when necessary

        if self._max_records is None:
            return

        excess = (
            len(self._records)
            - self._max_records
        )

        if excess > 0:
            del self._records[:excess]


    # Serialization

    def to_list(self) -> List[dict]:
        # Converts every translation record into a dictionary
        # The resulting list can be passed to a JSON or other
        # persistent storage system

        return [
            record.to_dict()
            for record in self._records
        ]


    def load_from_list(
        self,
        data: List[dict],
    ) -> None:
        # Replaces the current history with serialized record data
        # Existing history is cleared before the new records are loaded

        if not isinstance(data, list):
            raise TypeError(
                "History data must be a list."
            )

        self.clear()
        for record_data in data:

            record = TranslationRecord.from_dict(
                record_data
            )

            self.add_record(record)


    # Statistics

    def total_characters(self) -> int:
        # Returns the total number of characters represented across
        # all translation records

        return sum(
            record.character_count
            for record in self._records
        )


    def total_words(self) -> int:
        # Returns the total number of words represented across
        # all translation records

        return sum(
            record.word_count
            for record in self._records
        )


    # Display Utilities

    def summaries(self) -> List[str]:
        # Returns human-readable summaries for every translation record
        # The summaries are returned in chronological order

        return [
            record.summary()
            for record in self._records
        ]


    # Python Protocol Methods

    def __len__(self) -> int:
        # Returns the number of translation records currently stored

        return len(self._records)


    def __iter__(self):
        # Allows the HistoryManager to be iterated over directly
        # Records are returned from oldest to newest

        return iter(self._records)


    def __contains__(
        self,
        record_id: int,
    ) -> bool:
        # Determines whether a record with the supplied ID exists
        # in the translation history.

        return any(
            record.record_id == record_id
            for record in self._records
        )


# Public Module Interface

__all__ = [
    "HistoryManager",
]