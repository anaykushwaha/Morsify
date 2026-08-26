# validation_result.py
# Structured validation result model for the Morse Translator

# Contains the ValidationResult data model used throughout the validation
# package to represent whether input is valid, provide validation messages,
# identify invalid values, and store additional validation metadata

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# Validation Result Model

@dataclass
class ValidationResult:
    # Represents the result of a validation operation
    #
    # A ValidationResult contains:
    # - Whether the input is valid
    # - A descriptive validation message
    # - Invalid values detected during validation
    # - Optional validation metadata

    is_valid: bool
    message: str = ""
    invalid_values: List[Any] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __bool__(self) -> bool:
        # Allows ValidationResult objects to be used directly
        # in boolean expressions

        return self.is_valid

    def __repr__(self) -> str:
        # Returns a readable representation of the validation result

        return (
            "ValidationResult("
            f"is_valid={self.is_valid!r}, "
            f"message={self.message!r}, "
            f"invalid_values={self.invalid_values!r}, "
            f"metadata={self.metadata!r}"
            ")"
        )

    # Result Status

    def passed(self) -> bool:
        # Returns True when validation succeeded

        return self.is_valid

    def failed(self) -> bool:
        # Returns True when validation failed

        return not self.is_valid

    # Error Information

    def has_errors(self) -> bool:
        # Determines whether the validation result contains
        # invalid values or an error message

        return (
            not self.is_valid
            or bool(self.invalid_values)
            or bool(self.message)
        )

    def error_message(self) -> Optional[str]:
        # Returns the validation error message when validation failed
        #
        # Returns None when validation succeeded

        if self.is_valid:
            return None

        return self.message or "Validation failed."

    # Invalid Values

    def add_invalid_value(self, value: Any) -> None:
        # Adds an invalid value to the result if it is not already present

        if value not in self.invalid_values:
            self.invalid_values.append(value)

    def add_invalid_values(
        self,
        values: List[Any],
    ) -> None:
        # Adds multiple invalid values while preventing duplicates

        for value in values:
            self.add_invalid_value(value)

    def has_invalid_values(self) -> bool:
        # Determines whether invalid values were recorded

        return bool(self.invalid_values)

    # Metadata

    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        # Adds or updates a metadata value

        if not isinstance(key, str) or not key:
            raise ValueError(
                "Metadata key must be a non-empty string."
            )

        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        # Returns metadata associated with a key
        #
        # Returns the supplied default when the key does not exist

        return self.metadata.get(key, default)

    def has_metadata(self, key: str) -> bool:
        # Determines whether the specified metadata key exists

        return key in self.metadata

    # Result Conversion

    def to_dict(self) -> Dict[str, Any]:
        # Converts the validation result into a dictionary

        return {
            "is_valid": self.is_valid,
            "message": self.message,
            "invalid_values": list(self.invalid_values),
            "metadata": dict(self.metadata),
        }

    def summary(self) -> str:
        # Returns a concise human-readable validation summary

        if self.is_valid:
            if self.message:
                return f"Valid: {self.message}"

            return "Valid."

        if self.message:
            return f"Invalid: {self.message}"

        return "Invalid."

    # Result Factory Methods

    @classmethod
    def success(
        cls,
        message: str = "Validation successful.",
        metadata: Optional[Dict[str, Any]] = None,
    ) -> "ValidationResult":
        # Creates a successful ValidationResult

        return cls(
            is_valid=True,
            message=message,
            metadata=dict(metadata or {}),
        )

    @classmethod
    def failure(
        cls,
        message: str,
        invalid_values: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> "ValidationResult":
        # Creates a failed ValidationResult

        return cls(
            is_valid=False,
            message=message,
            invalid_values=list(invalid_values or []),
            metadata=dict(metadata or {}),
        )


# Validation Result Combination

def combine_results(
    *results: ValidationResult,
) -> ValidationResult:
    # Combines multiple validation results into a single result
    #
    # The combined result is valid only when every supplied result
    # is valid

    if not results:
        return ValidationResult.success(
            "No validation results were provided."
        )

    for result in results:
        if not isinstance(result, ValidationResult):
            raise ValueError(
                "All results must be ValidationResult objects."
            )

    invalid_values: List[Any] = []
    messages: List[str] = []
    metadata: Dict[str, Any] = {}

    is_valid = True

    for result in results:
        if not result.is_valid:
            is_valid = False

        if result.message:
            if result.message not in messages:
                messages.append(result.message)

        for value in result.invalid_values:
            if value not in invalid_values:
                invalid_values.append(value)

        metadata.update(result.metadata)

    if is_valid:
        message = "All validation checks passed."
    else:
        message = " ".join(messages)

    return ValidationResult(
        is_valid=is_valid,
        message=message,
        invalid_values=invalid_values,
        metadata=metadata,
    )


# Validation Result Factory Helpers

def valid_result(
    message: str = "Validation successful.",
    metadata: Optional[Dict[str, Any]] = None,
) -> ValidationResult:
    # Convenience function for creating successful validation results

    return ValidationResult.success(
        message=message,
        metadata=metadata,
    )


def invalid_result(
    message: str,
    invalid_values: Optional[List[Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> ValidationResult:
    # Convenience function for creating failed validation results

    return ValidationResult.failure(
        message=message,
        invalid_values=invalid_values,
        metadata=metadata,
    )


# Validation Result Verification

def is_validation_result(value: Any) -> bool:
    # Determines whether a value is a ValidationResult instance

    return isinstance(value, ValidationResult)


def ensure_validation_result(
    value: Any,
) -> ValidationResult:
    # Ensures that the supplied value is a ValidationResult
    # Raises TypeError when the value is not a ValidationResult

    if not isinstance(value, ValidationResult):
        raise TypeError(
            "Value must be a ValidationResult."
        )

    return value


# Public Module Interface

__all__ = [
    "ValidationResult",
    "combine_results",
    "valid_result",
    "invalid_result",
    "is_validation_result",
    "ensure_validation_result",
]

