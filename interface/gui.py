# gui.py
# Main graphical user interface for the Morse Translator

# Contains the primary application window, translation controls,
# input and output areas, history display, status messages, and
# event handling used to provide the graphical Morse translation
# experience


import tkinter as tk
from tkinter import messagebox, ttk
from typing import Optional

from core.translator import MorseTranslator
from core.translation import TranslationDirection

from validation.validator import Validator
from validation.english_validator import validate_english
from validation.morse_validator import validate_morse

from formatting.formatter import (
    normalize_text,
    format_translation_output,
)

from formatting.morse_formatter import (
    normalize_morse,
)

from history.history_manager import HistoryManager
from history.translation_record import TranslationRecord

from .components import (
    create_label,
    create_button,
    create_text_area,
    create_direction_selector,
    create_history_list,
)

from .styles import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_PADDING,
    SECTION_PADDING,
    MEDIUM_PADDING,
    LARGE_PADDING,
    TEXT_AREA_HEIGHT,
    TEXT_AREA_WIDTH,
    HISTORY_HEIGHT,
    BUTTON_WIDTH,
    DIRECTION_SELECTOR_WIDTH,
    BACKGROUND_COLOR,
    SURFACE_COLOR,
    TEXT_COLOR,
    MUTED_TEXT_COLOR,
    PRIMARY_COLOR,
    ERROR_COLOR,
    SUCCESS_COLOR,
    configure_theme,
    configure_root_window,
    configure_text_widget,
    configure_history_list,
)


# Main GUI Application

class MorseTranslatorGUI:
    # Main graphical application class responsible for coordinating
    # user interaction with the Morse Translator system

    def __init__(
        self,
        root: tk.Tk,
        translator: Optional[MorseTranslator] = None,
        history_manager: Optional[HistoryManager] = None,
    ) -> None:
        # Initializes the graphical interface and connects the GUI
        # to the translation and history-management components

        if root is None:
            raise ValueError("Root window cannot be None.")

        if not isinstance(root, tk.Tk):
            raise ValueError("Root must be a tkinter Tk instance.")

        self.root = root

        self.translator = translator or MorseTranslator()

        self.history_manager = (
            history_manager
            or HistoryManager()
        )

        self.current_direction = (
            TranslationDirection.ENGLISH_TO_MORSE
        )

        self.status_message = tk.StringVar(
            value="Ready to translate."
        )

        self.direction_variable = tk.StringVar(
            value="English → Morse"
        )

        self._configure_application()
        self._create_variables()
        self._build_interface()
        self._load_history()

    # Application Configuration

    def _configure_application(self) -> None:
        # Configures the main application window and ttk visual theme

        configure_theme(self.root)

        configure_root_window(self.root)

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self._handle_close,
        )

    def _create_variables(self) -> None:
        # Creates Tkinter variables used by interface controls

        self.direction_variable = tk.StringVar(
            value="English → Morse"
        )

        self.status_message = tk.StringVar(
            value="Ready to translate."
        )

    # Interface Construction

    def _build_interface(self) -> None:
        # Builds all major sections of the Morse Translator interface

        self._create_main_container()
        self._create_header()
        self._create_translation_section()
        self._create_control_section()
        self._create_history_section()
        self._create_status_section()

    def _create_main_container(self) -> None:
        # Creates the primary container used to organize all interface sections

        self.main_frame = tk.Frame(
            self.root,
            background=BACKGROUND_COLOR,
            padx=WINDOW_PADDING,
            pady=WINDOW_PADDING,
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
        )

        self.main_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        self.main_frame.grid_rowconfigure(
            2,
            weight=1,
        )

    def _create_header(self) -> None:
        # Creates the application title and descriptive subtitle

        self.header_frame = tk.Frame(
            self.main_frame,
            background=BACKGROUND_COLOR,
        )

        self.header_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, LARGE_PADDING),
        )

        self.title_label = tk.Label(
            self.header_frame,
            text="Morse Translator",
            background=BACKGROUND_COLOR,
            foreground=TEXT_COLOR,
            font=("Segoe UI", 24, "bold"),
        )

        self.title_label.pack(
            anchor="w",
        )

        self.subtitle_label = tk.Label(
            self.header_frame,
            text=(
                "Translate English text to Morse Code "
                "and Morse Code back to English."
            ),
            background=BACKGROUND_COLOR,
            foreground=MUTED_TEXT_COLOR,
            font=("Segoe UI", 11),
        )

        self.subtitle_label.pack(
            anchor="w",
            pady=(4, 0),
        )

    def _create_translation_section(self) -> None:
        # Creates the input and output text areas used for translation

        self.translation_frame = tk.Frame(
            self.main_frame,
            background=BACKGROUND_COLOR,
        )

        self.translation_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=(0, SECTION_PADDING),
        )

        self.translation_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        self.translation_frame.grid_columnconfigure(
            1,
            weight=1,
        )

        self._create_input_area()
        self._create_output_area()

    def _create_input_area(self) -> None:
        # Creates the input label and editable text area

        self.input_container = tk.Frame(
            self.translation_frame,
            background=BACKGROUND_COLOR,
        )

        self.input_container.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, MEDIUM_PADDING),
        )

        self.input_label = tk.Label(
            self.input_container,
            text="Input",
            background=BACKGROUND_COLOR,
            foreground=TEXT_COLOR,
            font=("Segoe UI", 10, "bold"),
        )

        self.input_label.pack(
            anchor="w",
            pady=(0, 5),
        )

        self.input_text = tk.Text(
            self.input_container,
            height=TEXT_AREA_HEIGHT,
            width=TEXT_AREA_WIDTH,
        )

        configure_text_widget(
            self.input_text,
        )

        self.input_text.pack(
            fill="both",
            expand=True,
        )

        self.input_text.bind(
            "<Control-Return>",
            self._handle_translate_shortcut,
        )

    def _create_output_area(self) -> None:
        # Creates the output label and read-only translated text area

        self.output_container = tk.Frame(
            self.translation_frame,
            background=BACKGROUND_COLOR,
        )

        self.output_container.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(MEDIUM_PADDING, 0),
        )

        self.output_label = tk.Label(
            self.output_container,
            text="Output",
            background=BACKGROUND_COLOR,
            foreground=TEXT_COLOR,
            font=("Segoe UI", 10, "bold"),
        )

        self.output_label.pack(
            anchor="w",
            pady=(0, 5),
        )

        self.output_text = tk.Text(
            self.output_container,
            height=TEXT_AREA_HEIGHT,
            width=TEXT_AREA_WIDTH,
        )

        configure_text_widget(
            self.output_text,
            read_only=True,
        )

        self.output_text.pack(
            fill="both",
            expand=True,
        )

    # Control Section

    def _create_control_section(self) -> None:
        # Creates direction selection and translation control buttons

        self.control_frame = tk.Frame(
            self.main_frame,
            background=BACKGROUND_COLOR,
        )

        self.control_frame.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(0, SECTION_PADDING),
        )

        self.direction_label = tk.Label(
            self.control_frame,
            text="Translation Direction",
            background=BACKGROUND_COLOR,
            foreground=TEXT_COLOR,
            font=("Segoe UI", 10, "bold"),
        )

        self.direction_label.grid(
            row=0,
            column=0,
            padx=(0, MEDIUM_PADDING),
            pady=(0, 8),
            sticky="w",
        )

        self.direction_selector = ttk.Combobox(
            self.control_frame,
            textvariable=self.direction_variable,
            values=[
                "English → Morse",
                "Morse → English",
            ],
            state="readonly",
            width=DIRECTION_SELECTOR_WIDTH,
        )

        self.direction_selector.grid(
            row=0,
            column=1,
            padx=(0, MEDIUM_PADDING),
            pady=(0, 8),
            sticky="w",
        )

        self.direction_selector.bind(
            "<<ComboboxSelected>>",
            self._handle_direction_change,
        )

        self.translate_button = tk.Button(
            self.control_frame,
            text="Translate",
            command=self.translate,
            width=BUTTON_WIDTH,
            background=PRIMARY_COLOR,
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6,
        )

        self.translate_button.grid(
            row=0,
            column=2,
            padx=(0, MEDIUM_PADDING),
            pady=(0, 8),
        )

        self.clear_button = tk.Button(
            self.control_frame,
            text="Clear",
            command=self.clear,
            width=BUTTON_WIDTH,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6,
        )

        self.clear_button.grid(
            row=0,
            column=3,
            padx=(0, MEDIUM_PADDING),
            pady=(0, 8),
        )

        self.copy_button = tk.Button(
            self.control_frame,
            text="Copy Output",
            command=self.copy_output,
            width=BUTTON_WIDTH,
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=6,
        )

        self.copy_button.grid(
            row=0,
            column=4,
            pady=(0, 8),
        )

    # History Section

    def _create_history_section(self) -> None:
        # Creates the translation history area and history controls

        self.history_frame = tk.Frame(
            self.main_frame,
            background=BACKGROUND_COLOR,
        )

        self.history_frame.grid(
            row=3,
            column=0,
            sticky="nsew",
            pady=(0, SECTION_PADDING),
        )

        self.history_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        self.history_title = tk.Label(
            self.history_frame,
            text="Translation History",
            background=BACKGROUND_COLOR,
            foreground=TEXT_COLOR,
            font=("Segoe UI", 14, "bold"),
        )

        self.history_title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 8),
        )

        self.history_list = tk.Listbox(
            self.history_frame,
            height=HISTORY_HEIGHT,
        )

        configure_history_list(
            self.history_list,
        )

        self.history_list.grid(
            row=1,
            column=0,
            sticky="nsew",
        )

        self.history_list.bind(
            "<Double-Button-1>",
            self._handle_history_selection,
        )

        self.history_scrollbar = ttk.Scrollbar(
            self.history_frame,
            orient="vertical",
            command=self.history_list.yview,
        )

        self.history_scrollbar.grid(
            row=1,
            column=1,
            sticky="ns",
        )

        self.history_list.configure(
            yscrollcommand=self.history_scrollbar.set,
        )

        self.clear_history_button = tk.Button(
            self.history_frame,
            text="Clear History",
            command=self.clear_history,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            cursor="hand2",
            padx=10,
            pady=5,
        )

        self.clear_history_button.grid(
            row=2,
            column=0,
            sticky="e",
            pady=(8, 0),
        )

    # Status Section

    def _create_status_section(self) -> None:
        # Creates the status bar used to provide feedback to the user

        self.status_frame = tk.Frame(
            self.main_frame,
            background=BACKGROUND_COLOR,
        )

        self.status_frame.grid(
            row=4,
            column=0,
            sticky="ew",
        )

        self.status_label = tk.Label(
            self.status_frame,
            textvariable=self.status_message,
            background=BACKGROUND_COLOR,
            foreground=MUTED_TEXT_COLOR,
            font=("Segoe UI", 9),
            anchor="w",
        )

        self.status_label.pack(
            fill="x",
        )

    # Translation Operations

    def translate(self) -> None:
        # Reads the input, validates it, performs the selected translation,
        # displays the result, records the translation, and updates the status

        input_text = self._get_input_text()

        if not input_text:
            self._set_status(
                "Please enter some text to translate.",
                ERROR_COLOR,
            )
            return

        try:
            if self.current_direction == (
                TranslationDirection.ENGLISH_TO_MORSE
            ):
                self._translate_to_morse(input_text)
            else:
                self._translate_to_english(input_text)

        except (ValueError, KeyError) as error:
            self._set_status(
                str(error),
                ERROR_COLOR,
            )

        except Exception:
            self._set_status(
                "An unexpected error occurred during translation.",
                ERROR_COLOR,
            )

    def _translate_to_morse(
        self,
        input_text: str,
    ) -> None:
        # Validates and translates English input into Morse Code

        validation_result = validate_english(
            input_text,
        )

        if not validation_result.is_valid:
            self._set_status(
                validation_result.message,
                ERROR_COLOR,
            )
            return

        normalized_input = normalize_text(
            input_text,
        )

        result = self.translator.translate(
            normalized_input,
            TranslationDirection.ENGLISH_TO_MORSE,
        )

        output = format_translation_output(
            result.output,
        )

        self._display_output(output)

        self._record_translation(
            normalized_input,
            output,
            TranslationDirection.ENGLISH_TO_MORSE,
        )

        self._set_status(
            "Translation completed successfully.",
            SUCCESS_COLOR,
        )

    def _translate_to_english(
        self,
        input_text: str,
    ) -> None:
        # Validates and translates Morse Code input into English

        normalized_input = normalize_morse(
            input_text,
        )

        validation_result = validate_morse(
            normalized_input,
        )

        if not validation_result.is_valid:
            self._set_status(
                validation_result.message,
                ERROR_COLOR,
            )
            return

        result = self.translator.translate(
            normalized_input,
            TranslationDirection.MORSE_TO_ENGLISH,
        )

        output = format_translation_output(
            result.output,
        )

        self._display_output(output)

        self._record_translation(
            normalized_input,
            output,
            TranslationDirection.MORSE_TO_ENGLISH,
        )

        self._set_status(
            "Translation completed successfully.",
            SUCCESS_COLOR,
        )

    # Direction Management

    def _handle_direction_change(
        self,
        event: Optional[tk.Event] = None,
    ) -> None:
        # Updates the internal translation direction when the user
        # changes the selected translation mode

        selected_direction = self.direction_variable.get()

        if selected_direction == "English → Morse":
            self.current_direction = (
                TranslationDirection.ENGLISH_TO_MORSE
            )

            self.input_label.configure(
                text="English Input",
            )

            self.output_label.configure(
                text="Morse Output",
            )

        else:
            self.current_direction = (
                TranslationDirection.MORSE_TO_ENGLISH
            )

            self.input_label.configure(
                text="Morse Input",
            )

            self.output_label.configure(
                text="English Output",
            )

        self._set_status(
            "Translation direction changed.",
            MUTED_TEXT_COLOR,
        )

    # Input and Output Management

    def _get_input_text(self) -> str:
        # Retrieves the current input text from the input widget

        return self.input_text.get(
            "1.0",
            "end-1c",
        ).strip()

    def _display_output(
        self,
        output: str,
    ) -> None:
        # Replaces the output widget contents with the supplied
        # translated text

        self.output_text.configure(
            state="normal",
        )

        self.output_text.delete(
            "1.0",
            tk.END,
        )

        self.output_text.insert(
            "1.0",
            output,
        )

        self.output_text.configure(
            state="disabled",
        )

    def clear(self) -> None:
        # Clears both the input and output areas

        self.input_text.delete(
            "1.0",
            tk.END,
        )

        self.output_text.configure(
            state="normal",
        )

        self.output_text.delete(
            "1.0",
            tk.END,
        )

        self.output_text.configure(
            state="disabled",
        )

        self._set_status(
            "Input and output cleared.",
            MUTED_TEXT_COLOR,
        )

    def copy_output(self) -> None:
        # Copies the current translated output to the system clipboard

        output = self.output_text.get(
            "1.0",
            "end-1c",
        )

        if not output.strip():
            self._set_status(
                "There is no output to copy.",
                ERROR_COLOR,
            )
            return

        self.root.clipboard_clear()
        self.root.clipboard_append(output)
        self.root.update()

        self._set_status(
            "Output copied to clipboard.",
            SUCCESS_COLOR,
        )

    # History Management

    def _record_translation(
        self,
        input_text: str,
        output_text: str,
        direction: TranslationDirection,
    ) -> None:
        # Creates and stores a translation history record

        try:
            record = TranslationRecord(
                input_text=input_text,
                output_text=output_text,
                direction=direction,
            )

            self.history_manager.add_record(
                record,
            )

            self._refresh_history()

        except (ValueError, TypeError):
            self._set_status(
                "Translation completed, but history could not be updated.",
                ERROR_COLOR,
            )

    def _load_history(self) -> None:
        # Loads existing translation history into the history display

        self._refresh_history()

    def _refresh_history(self) -> None:
        # Refreshes the visible history list using records managed
        # by the history manager

        self.history_list.delete(
            0,
            tk.END,
        )

        try:
            records = self.history_manager.get_all()

        except AttributeError:
            records = []

        for record in records:
            display_text = self._format_history_record(
                record,
            )

            self.history_list.insert(
                tk.END,
                display_text,
            )

    def _format_history_record(
        self,
        record: TranslationRecord,
    ) -> str:
        # Creates a compact display representation for a history record

        input_text = getattr(
            record,
            "input_text",
            "",
        )

        output_text = getattr(
            record,
            "output_text",
            "",
        )

        direction = getattr(
            record,
            "direction",
            None,
        )

        if direction == TranslationDirection.ENGLISH_TO_MORSE:
            direction_text = "EN → MORSE"
        else:
            direction_text = "MORSE → EN"

        shortened_input = input_text.replace(
            "\n",
            " ",
        )

        if len(shortened_input) > 35:
            shortened_input = (
                shortened_input[:32]
                + "..."
            )

        return (
            f"{direction_text} | "
            f"{shortened_input}"
        )

    def _handle_history_selection(
        self,
        event: Optional[tk.Event] = None,
    ) -> None:
        # Loads the selected history record into the input and output
        # areas when the user double-clicks a history entry

        selection = self.history_list.curselection()

        if not selection:
            return

        selected_index = selection[0]

        try:
            records = self.history_manager.get_all()
            record = records[selected_index]

        except (AttributeError, IndexError):
            return

        input_text = getattr(
            record,
            "input_text",
            "",
        )

        output_text = getattr(
            record,
            "output_text",
            "",
        )

        self.input_text.delete(
            "1.0",
            tk.END,
        )

        self.input_text.insert(
            "1.0",
            input_text,
        )

        self._display_output(
            output_text,
        )

        self._set_status(
            "History entry loaded.",
            MUTED_TEXT_COLOR,
        )

    def clear_history(self) -> None:
        # Removes all stored translation history after confirmation

        records = self.history_manager.get_all()

        if not records:
            self._set_status(
                "Translation history is already empty.",
                MUTED_TEXT_COLOR,
            )
            return

        confirmed = messagebox.askyesno(
            "Clear History",
            "Are you sure you want to clear all translation history?",
            parent=self.root,
        )

        if not confirmed:
            return

        try:
            self.history_manager.clear()
            self._refresh_history()

            self._set_status(
                "Translation history cleared.",
                SUCCESS_COLOR,
            )

        except AttributeError:
            self._set_status(
                "Unable to clear translation history.",
                ERROR_COLOR,
            )

    # Status Management

    def _set_status(
        self,
        message: str,
        color: str = MUTED_TEXT_COLOR,
    ) -> None:
        # Updates the status message and its display color

        if not isinstance(message, str):
            raise ValueError("Status message must be a string.")

        self.status_message.set(
            message,
        )

        self.status_label.configure(
            foreground=color,
        )

    # Keyboard Shortcuts

    def _handle_translate_shortcut(
        self,
        event: Optional[tk.Event] = None,
    ) -> str:
        # Handles Ctrl+Enter as a keyboard shortcut for translation

        self.translate()

        return "break"

    # Application Lifecycle

    def _handle_close(self) -> None:
        # Handles application shutdown and closes the main window

        self.root.destroy()

    def run(self) -> None:
        # Starts the Tkinter event loop and runs the graphical application

        self.root.mainloop()


# Application Factory

def create_application(
    root: Optional[tk.Tk] = None,
) -> MorseTranslatorGUI:
    # Creates and returns a configured Morse Translator GUI instance

    application_root = root or tk.Tk()

    return MorseTranslatorGUI(
        application_root,
    )


def launch() -> None:
    # Creates and launches the Morse Translator graphical application

    application = create_application()

    application.run()


# Public Module Interface

__all__ = [
    "MorseTranslatorGUI",
    "create_application",
    "launch",
]

