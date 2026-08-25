# __init__.py

# Input validation package for the Morse Translator

# Contains validation logic for English text and Morse Code input,
# general validation interfaces, and validation utilities used
# throughout the translation workflow

# Modules
# validator - General validation interface and shared validation logic
# english_validator - Validation for English text input
# morse_validator - Validation for Morse Code input

from .validator import (
Validator,
ValidationResult,
)

from .english_validator import (
validate_english,
is_valid_english,
)

from .morse_validator import (
validate_morse,
is_valid_morse,
)

**all** = [

```
# General Validation
"Validator",
"ValidationResult",

# English Validation
"validate_english",
"is_valid_english",

# Morse Validation
"validate_morse",
"is_valid_morse",
```

]
