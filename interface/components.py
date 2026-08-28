# components.py
# Reusable graphical interface components for the Morse Translator

# Contains reusable Tkinter widgets and interface components used
# throughout the Morse Translator GUI, including input areas, output
# areas, buttons, labels, frames, status displays, and translation
# control components


import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional


# Base Interface Components

class BaseFrame(ttk.Frame):
    # Provides a reusable base frame for organizing related GUI widgets
    # and supports consistent padding and layout configuration

    def __init__(
        self,
        parent: tk.Misc,
        padding: int = 10,
        **kwargs,
    ) -> None:
        # Initializes the base frame with the supplied parent and padding

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        if not isinstance(padding, int):
            raise ValueError("Padding must be an integer.")

        if padding < 0:
            raise ValueError("Padding cannot be negative.")

        super().__init__(
            parent,
            padding=padding,
            **kwargs,
        )


class SectionFrame(BaseFrame):
    # Provides a labeled container for grouping related interface
    # elements into visually distinct sections

    def __init__(
        self,
        parent: tk.Misc,
        title: str = "",
        padding: int = 10,
        **kwargs,
    ) -> None:
        # Initializes a section frame with an optional title

        if not isinstance(title, str):
            raise ValueError("Title must be a string.")

        super().__init__(
            parent,
            padding=padding,
            **kwargs,
        )

        self.title = title.strip()

        if self.title:
            self.configure(
                relief="groove",
                borderwidth=1,
            )

            self.title_label = ttk.Label(
                self,
                text=self.title,
            )

            self.title_label.grid(
                row=0,
                column=0,
                sticky="w",
                padx=5,
                pady=(0, 8),
            )

            self.content_frame = ttk.Frame(self)

            self.content_frame.grid(
                row=1,
                column=0,
                sticky="nsew",
            )

            self.columnconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)

        else:
            self.content_frame = self


# Text Input Components

class TextInput(ttk.Frame):
    # Provides a reusable multiline text-input component for entering
    # English text or Morse Code input

    def __init__(
        self,
        parent: tk.Misc,
        height: int = 8,
        width: int = 60,
        placeholder: str = "",
        **kwargs,
    ) -> None:
        # Initializes the text-input area with configurable dimensions
        # and an optional placeholder value

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        if not isinstance(height, int):
            raise ValueError("Height must be an integer.")

        if not isinstance(width, int):
            raise ValueError("Width must be an integer.")

        if height <= 0:
            raise ValueError("Height must be greater than zero.")

        if width <= 0:
            raise ValueError("Width must be greater than zero.")

        if not isinstance(placeholder, str):
            raise ValueError("Placeholder must be a string.")

        super().__init__(
            parent,
            **kwargs,
        )

        self.placeholder = placeholder
        self._placeholder_active = False

        self.text_widget = tk.Text(
            self,
            height=height,
            width=width,
            wrap="word",
        )

        self.text_widget.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.text_widget.yview,
        )

        self.scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        self.text_widget.configure(
            yscrollcommand=self.scrollbar.set,
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        if self.placeholder:
            self._set_placeholder()

            self.text_widget.bind(
                "<FocusIn>",
                self._remove_placeholder,
            )

            self.text_widget.bind(
                "<FocusOut>",
                self._restore_placeholder,
            )

    def _set_placeholder(self, event=None) -> None:
        # Displays the configured placeholder when the input area is empty

        if self._placeholder_active:
            return

        if self.text_widget.get("1.0", "end-1c").strip():
            return

        self.text_widget.insert(
            "1.0",
            self.placeholder,
        )

        self._placeholder_active = True

    def _remove_placeholder(self, event=None) -> None:
        # Removes the placeholder when the user focuses the input area

        if not self._placeholder_active:
            return

        self.text_widget.delete(
            "1.0",
            "end",
        )

        self._placeholder_active = False

    def _restore_placeholder(self, event=None) -> None:
        # Restores the placeholder when the input area loses focus empty

        if self.text_widget.get("1.0", "end-1c").strip():
            return

        self._set_placeholder()

    def get(self) -> str:
        # Returns the current text contained in the input area

        if self._placeholder_active:
            return ""

        return self.text_widget.get(
            "1.0",
            "end-1c",
        )

    def set(self, text: str) -> None:
        # Replaces the current input with the supplied text

        if not isinstance(text, str):
            raise ValueError("Text must be a string.")

        self.text_widget.delete(
            "1.0",
            "end",
        )

        self._placeholder_active = False

        if text:
            self.text_widget.insert(
                "1.0",
                text,
            )
        elif self.placeholder:
            self._set_placeholder()

    def clear(self) -> None:
        # Removes all text from the input area

        self.text_widget.delete(
            "1.0",
            "end",
        )

        self._placeholder_active = False

        if self.placeholder:
            self._set_placeholder()


class TextOutput(ttk.Frame):
    # Provides a reusable read-only multiline output component for
    # displaying translated English text or Morse Code

    def __init__(
        self,
        parent: tk.Misc,
        height: int = 8,
        width: int = 60,
        **kwargs,
    ) -> None:
        # Initializes the output area with configurable dimensions

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        if not isinstance(height, int):
            raise ValueError("Height must be an integer.")

        if not isinstance(width, int):
            raise ValueError("Width must be an integer.")

        if height <= 0:
            raise ValueError("Height must be greater than zero.")

        if width <= 0:
            raise ValueError("Width must be greater than zero.")

        super().__init__(
            parent,
            **kwargs,
        )

        self.text_widget = tk.Text(
            self,
            height=height,
            width=width,
            wrap="word",
            state="disabled",
        )

        self.text_widget.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.text_widget.yview,
        )

        self.scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        self.text_widget.configure(
            yscrollcommand=self.scrollbar.set,
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def get(self) -> str:
        # Returns the text currently displayed in the output area

        return self.text_widget.get(
            "1.0",
            "end-1c",
        )

    def set(self, text: str) -> None:
        # Replaces the current output with the supplied translated text

        if not isinstance(text, str):
            raise ValueError("Text must be a string.")

        self.text_widget.configure(
            state="normal",
        )

        self.text_widget.delete(
            "1.0",
            "end",
        )

        self.text_widget.insert(
            "1.0",
            text,
        )

        self.text_widget.configure(
            state="disabled",
        )

    def clear(self) -> None:
        # Removes all content from the output area

        self.set("")


# Button Components

class ActionButton(ttk.Button):
    # Provides a reusable button for triggering translator actions

    def __init__(
        self,
        parent: tk.Misc,
        text: str,
        command: Optional[Callable[[], None]] = None,
        **kwargs,
    ) -> None:
        # Initializes the button with display text and an optional callback

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        if not isinstance(text, str):
            raise ValueError("Button text must be a string.")

        if not text.strip():
            raise ValueError("Button text cannot be empty.")

        if command is not None and not callable(command):
            raise ValueError("Command must be callable.")

        super().__init__(
            parent,
            text=text,
            command=command,
            **kwargs,
        )


class ClearButton(ActionButton):
    # Provides a specialized button for clearing input and output fields

    def __init__(
        self,
        parent: tk.Misc,
        command: Optional[Callable[[], None]] = None,
        **kwargs,
    ) -> None:
        # Initializes the clear button with a standard label

        super().__init__(
            parent,
            text="Clear",
            command=command,
            **kwargs,
        )


class TranslateButton(ActionButton):
    # Provides a specialized button for starting a translation operation

    def __init__(
        self,
        parent: tk.Misc,
        command: Optional[Callable[[], None]] = None,
        **kwargs,
    ) -> None:
        # Initializes the translation button with a standard label

        super().__init__(
            parent,
            text="Translate",
            command=command,
            **kwargs,
        )


# Label Components

class StatusLabel(ttk.Label):
    # Displays the current status of a translation or interface operation

    def __init__(
        self,
        parent: tk.Misc,
        text: str = "",
        **kwargs,
    ) -> None:
        # Initializes the status label with optional starting text

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        if not isinstance(text, str):
            raise ValueError("Status text must be a string.")

        super().__init__(
            parent,
            text=text,
            **kwargs,
        )

    def set_status(self, text: str) -> None:
        # Updates the displayed status message

        if not isinstance(text, str):
            raise ValueError("Status text must be a string.")

        self.configure(
            text=text,
        )

    def clear_status(self) -> None:
        # Removes the current status message

        self.configure(
            text="",
        )


class CharacterCountLabel(ttk.Label):
    # Displays the number of characters currently present in a text area

    def __init__(
        self,
        parent: tk.Misc,
        **kwargs,
    ) -> None:
        # Initializes the character-count display

        super().__init__(
            parent,
            text="Characters: 0",
            **kwargs,
        )

    def update_count(self, text: str) -> None:
        # Updates the character count using the supplied text

        if not isinstance(text, str):
            raise ValueError("Text must be a string.")

        self.configure(
            text=f"Characters: {len(text)}",
        )


# Translation Control Components

class DirectionSelector(ttk.Frame):
    # Provides a reusable control for selecting the direction of
    # translation between English and Morse Code

    DIRECTIONS = (
        "English → Morse",
        "Morse → English",
    )

    def __init__(
        self,
        parent: tk.Misc,
        **kwargs,
    ) -> None:
        # Initializes the translation-direction selection control

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        super().__init__(
            parent,
            **kwargs,
        )

        self.variable = tk.StringVar(
            value=self.DIRECTIONS[0],
        )

        self.label = ttk.Label(
            self,
            text="Direction:",
        )

        self.label.grid(
            row=0,
            column=0,
            padx=(0, 8),
        )

        self.selector = ttk.Combobox(
            self,
            textvariable=self.variable,
            values=self.DIRECTIONS,
            state="readonly",
            width=20,
        )

        self.selector.grid(
            row=0,
            column=1,
        )

    def get(self) -> str:
        # Returns the currently selected translation direction

        return self.variable.get()

    def set(self, direction: str) -> None:
        # Selects the supplied translation direction

        if not isinstance(direction, str):
            raise ValueError("Direction must be a string.")

        if direction not in self.DIRECTIONS:
            raise ValueError(
                "Unsupported translation direction."
            )

        self.variable.set(direction)

    def is_english_to_morse(self) -> bool:
        # Determines whether English-to-Morse translation is selected

        return self.get() == "English → Morse"

    def is_morse_to_english(self) -> bool:
        # Determines whether Morse-to-English translation is selected

        return self.get() == "Morse → English"


# Translation Panel

class TranslationPanel(SectionFrame):
    # Provides a reusable grouped interface containing input, output,
    # direction selection, and translation controls

    def __init__(
        self,
        parent: tk.Misc,
        title: str = "Translation",
        **kwargs,
    ) -> None:
        # Initializes the complete translation panel

        super().__init__(
            parent,
            title=title,
            **kwargs,
        )

        self.direction_selector = DirectionSelector(
            self.content_frame,
        )

        self.direction_selector.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 10),
        )

        self.input_label = ttk.Label(
            self.content_frame,
            text="Input",
        )

        self.input_label.grid(
            row=1,
            column=0,
            sticky="w",
            pady=(0, 4),
        )

        self.input_area = TextInput(
            self.content_frame,
            placeholder="Enter English text or Morse Code...",
        )

        self.input_area.grid(
            row=2,
            column=0,
            sticky="nsew",
        )

        self.output_label = ttk.Label(
            self.content_frame,
            text="Output",
        )

        self.output_label.grid(
            row=3,
            column=0,
            sticky="w",
            pady=(12, 4),
        )

        self.output_area = TextOutput(
            self.content_frame,
        )

        self.output_area.grid(
            row=4,
            column=0,
            sticky="nsew",
        )

        self.button_frame = ttk.Frame(
            self.content_frame,
        )

        self.button_frame.grid(
            row=5,
            column=0,
            sticky="w",
            pady=(12, 0),
        )

        self.translate_button = TranslateButton(
            self.button_frame,
        )

        self.translate_button.grid(
            row=0,
            column=0,
            padx=(0, 8),
        )

        self.clear_button = ClearButton(
            self.button_frame,
        )

        self.clear_button.grid(
            row=0,
            column=1,
        )

        self.status_label = StatusLabel(
            self.content_frame,
        )

        self.status_label.grid(
            row=6,
            column=0,
            sticky="w",
            pady=(8, 0),
        )

        self.character_count = CharacterCountLabel(
            self.content_frame,
        )

        self.character_count.grid(
            row=7,
            column=0,
            sticky="w",
            pady=(4, 0),
        )

        self.content_frame.columnconfigure(
            0,
            weight=1,
        )

        self.content_frame.rowconfigure(
            2,
            weight=1,
        )

        self.content_frame.rowconfigure(
            4,
            weight=1,
        )

    def get_input(self) -> str:
        # Returns the current translation input

        return self.input_area.get()

    def set_input(self, text: str) -> None:
        # Sets the translation input text

        self.input_area.set(text)
        self.character_count.update_count(text)

    def get_output(self) -> str:
        # Returns the current translation output

        return self.output_area.get()

    def set_output(self, text: str) -> None:
        # Sets the translation output text

        self.output_area.set(text)

    def clear(self) -> None:
        # Clears the translation input, output, status, and character count

        self.input_area.clear()
        self.output_area.clear()
        self.status_label.clear_status()
        self.character_count.update_count("")

    def set_status(self, text: str) -> None:
        # Updates the translation panel status message

        self.status_label.set_status(text)

    def set_translate_command(
        self,
        command: Callable[[], None],
    ) -> None:
        # Assigns the callback executed by the translation button

        if not callable(command):
            raise ValueError("Command must be callable.")

        self.translate_button.configure(
            command=command,
        )

    def set_clear_command(
        self,
        command: Callable[[], None],
    ) -> None:
        # Assigns the callback executed by the clear button

        if not callable(command):
            raise ValueError("Command must be callable.")

        self.clear_button.configure(
            command=command,
        )


# History Components

class HistoryList(ttk.Frame):
    # Provides a reusable list-based component for displaying previous
    # translation records

    def __init__(
        self,
        parent: tk.Misc,
        height: int = 8,
        **kwargs,
    ) -> None:
        # Initializes the history list and its scrollbar

        if parent is None:
            raise ValueError("Parent widget cannot be None.")

        if not isinstance(height, int):
            raise ValueError("Height must be an integer.")

        if height <= 0:
            raise ValueError("Height must be greater than zero.")

        super().__init__(
            parent,
            **kwargs,
        )

        self.listbox = tk.Listbox(
            self,
            height=height,
            selectmode="browse",
        )

        self.listbox.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.listbox.yview,
        )

        self.scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        self.listbox.configure(
            yscrollcommand=self.scrollbar.set,
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def add_item(self, text: str) -> None:
        # Adds a new history entry to the list

        if not isinstance(text, str):
            raise ValueError("History item must be a string.")

        self.listbox.insert(
            "end",
            text,
        )

    def set_items(self, items: list[str]) -> None:
        # Replaces the current history entries with the supplied items

        if not isinstance(items, list):
            raise ValueError("Items must be provided as a list.")

        if not all(isinstance(item, str) for item in items):
            raise ValueError("All history items must be strings.")

        self.clear()

        for item in items:
            self.add_item(item)

    def get_selected(self) -> Optional[str]:
        # Returns the currently selected history entry

        selection = self.listbox.curselection()

        if not selection:
            return None

        return self.listbox.get(
            selection[0],
        )

    def clear(self) -> None:
        # Removes all entries from the history list

        self.listbox.delete(
            0,
            "end",
        )

    def count(self) -> int:
        # Returns the number of entries currently displayed

        return self.listbox.size()


# Public Module Interface

__all__ = [
    # Base Components
    "BaseFrame",
    "SectionFrame",

    # Text Components
    "TextInput",
    "TextOutput",

    # Button Components
    "ActionButton",
    "ClearButton",
    "TranslateButton",

    # Label Components
    "StatusLabel",
    "CharacterCountLabel",

    # Translation Components
    "DirectionSelector",
    "TranslationPanel",

    # History Components
    "HistoryList",
]

