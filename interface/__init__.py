# __init__.py
# Graphical user interface package for the Morse Translator

# Contains the main Tkinter application window, reusable interface
# components, event-handling functionality, and visual styling
# used throughout the Morse Translator application

# Modules

# gui - Main application window and GUI coordination
# components - Reusable Tkinter interface components
# styles - Application-wide GUI styling and visual constants


from .gui import (
    MorseTranslatorGUI,
)

from .components import (
    InputPanel,
    OutputPanel,
    TranslationControls,
    HistoryPanel,
)

from .styles import (
    COLORS,
    FONTS,
    DIMENSIONS,
)


__all__ = [
    # Main GUI
    "MorseTranslatorGUI",
    # GUI Components
    "InputPanel",
    "OutputPanel",
    "TranslationControls",
    "HistoryPanel",
    # Styles
    "COLORS",
    "FONTS",
    "DIMENSIONS",
]

