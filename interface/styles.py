# styles.py
# Visual styling configuration for the Morse Translator interface

# Contains centralized colors, fonts, dimensions, spacing, widget
# configuration values, and ttk style configuration utilities used
# throughout the graphical interface


import tkinter as tk
from tkinter import ttk
from typing import Optional


# Window Configuration

WINDOW_TITLE = "Morse Translator"

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

MIN_WINDOW_WIDTH = 700
MIN_WINDOW_HEIGHT = 550


# Color Configuration

BACKGROUND_COLOR = "#F5F7FA"
SURFACE_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#2F6FED"
SECONDARY_COLOR = "#5B6472"
TEXT_COLOR = "#202124"
MUTED_TEXT_COLOR = "#6B7280"
BORDER_COLOR = "#D9DEE7"
SUCCESS_COLOR = "#2E7D32"
ERROR_COLOR = "#C62828"
WARNING_COLOR = "#ED8B00"
INPUT_BACKGROUND_COLOR = "#FFFFFF"
OUTPUT_BACKGROUND_COLOR = "#F8FAFC"


# Font Configuration

FONT_FAMILY = "Segoe UI"

TITLE_FONT = (
    FONT_FAMILY,
    24,
    "bold",
)

SUBTITLE_FONT = (
    FONT_FAMILY,
    11,
)

HEADING_FONT = (
    FONT_FAMILY,
    14,
    "bold",
)

LABEL_FONT = (
    FONT_FAMILY,
    10,
    "bold",
)

BODY_FONT = (
    FONT_FAMILY,
    10,
)

MONOSPACE_FONT = (
    "Consolas",
    11,
)

BUTTON_FONT = (
    FONT_FAMILY,
    10,
    "bold",
)

STATUS_FONT = (
    FONT_FAMILY,
    9,
)


# Spacing Configuration

WINDOW_PADDING = 20

SECTION_PADDING = 15

SMALL_PADDING = 5

MEDIUM_PADDING = 10

LARGE_PADDING = 20

BUTTON_PADDING_X = 15
BUTTON_PADDING_Y = 8

LABEL_SPACING = 5

SECTION_SPACING = 15


# Component Dimensions

TEXT_AREA_HEIGHT = 8
TEXT_AREA_WIDTH = 70

HISTORY_HEIGHT = 8

BUTTON_WIDTH = 14

DIRECTION_SELECTOR_WIDTH = 20


# Border Configuration

BORDER_WIDTH = 1

CORNER_RADIUS = 6


# Style Names

STYLE_FRAME = "Morse.TFrame"
STYLE_LABEL = "Morse.TLabel"
STYLE_TITLE = "Morse.Title.TLabel"
STYLE_SUBTITLE = "Morse.Subtitle.TLabel"
STYLE_HEADING = "Morse.Heading.TLabel"
STYLE_STATUS = "Morse.Status.TLabel"
STYLE_BUTTON = "Morse.TButton"
STYLE_PRIMARY_BUTTON = "Morse.Primary.TButton"
STYLE_SECONDARY_BUTTON = "Morse.Secondary.TButton"
STYLE_COMBOBOX = "Morse.TCombobox"


# Theme Configuration

DEFAULT_THEME = "clam"


def configure_theme(
    root: tk.Misc,
    theme: Optional[str] = None,
) -> None:
    # Configures the ttk theme and applies the Morse Translator
    # visual styles to the supplied root window

    if root is None:
        raise ValueError("Root widget cannot be None.")

    if theme is not None and not isinstance(theme, str):
        raise ValueError("Theme must be a string or None.")

    style = ttk.Style(root)

    selected_theme = theme or DEFAULT_THEME

    if selected_theme not in style.theme_names():
        raise ValueError(
            f"Unsupported ttk theme: {selected_theme}"
        )

    style.theme_use(selected_theme)

    configure_styles(style)


def configure_styles(
    style: ttk.Style,
) -> None:
    # Configures all reusable ttk styles used throughout the
    # Morse Translator graphical interface

    if not isinstance(style, ttk.Style):
        raise ValueError("Style must be a ttk.Style instance.")

    style.configure(
        STYLE_FRAME,
        background=BACKGROUND_COLOR,
    )

    style.configure(
        STYLE_LABEL,
        background=BACKGROUND_COLOR,
        foreground=TEXT_COLOR,
        font=BODY_FONT,
    )

    style.configure(
        STYLE_TITLE,
        background=BACKGROUND_COLOR,
        foreground=TEXT_COLOR,
        font=TITLE_FONT,
    )

    style.configure(
        STYLE_SUBTITLE,
        background=BACKGROUND_COLOR,
        foreground=MUTED_TEXT_COLOR,
        font=SUBTITLE_FONT,
    )

    style.configure(
        STYLE_HEADING,
        background=BACKGROUND_COLOR,
        foreground=TEXT_COLOR,
        font=HEADING_FONT,
    )

    style.configure(
        STYLE_STATUS,
        background=BACKGROUND_COLOR,
        foreground=MUTED_TEXT_COLOR,
        font=STATUS_FONT,
    )

    style.configure(
        STYLE_BUTTON,
        font=BUTTON_FONT,
        padding=(
            BUTTON_PADDING_X,
            BUTTON_PADDING_Y,
        ),
    )

    style.configure(
        STYLE_PRIMARY_BUTTON,
        font=BUTTON_FONT,
        padding=(
            BUTTON_PADDING_X,
            BUTTON_PADDING_Y,
        ),
    )

    style.configure(
        STYLE_SECONDARY_BUTTON,
        font=BUTTON_FONT,
        padding=(
            BUTTON_PADDING_X,
            BUTTON_PADDING_Y,
        ),
    )

    style.configure(
        STYLE_COMBOBOX,
        font=BODY_FONT,
        padding=SMALL_PADDING,
    )


def configure_root_window(
    root: tk.Tk,
) -> None:
    # Applies the standard window title, size, minimum dimensions,
    # background color, and initial positioning

    if root is None:
        raise ValueError("Root window cannot be None.")

    if not isinstance(root, tk.Tk):
        raise ValueError("Root must be a tkinter Tk instance.")

    root.title(WINDOW_TITLE)

    root.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
    )

    root.minsize(
        MIN_WINDOW_WIDTH,
        MIN_WINDOW_HEIGHT,
    )

    root.configure(
        background=BACKGROUND_COLOR,
    )

    center_window(root)


def center_window(
    root: tk.Tk,
) -> None:
    # Centers the supplied application window on the user's screen

    if root is None:
        raise ValueError("Root window cannot be None.")

    if not isinstance(root, tk.Tk):
        raise ValueError("Root must be a tkinter Tk instance.")

    root.update_idletasks()

    window_width = root.winfo_width()
    window_height = root.winfo_height()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = max(
        (screen_width - window_width) // 2,
        0,
    )

    y_position = max(
        (screen_height - window_height) // 2,
        0,
    )

    root.geometry(
        f"{window_width}x{window_height}"
        f"+{x_position}+{y_position}"
    )


# Text Widget Configuration

def configure_text_widget(
    widget: tk.Text,
    read_only: bool = False,
) -> None:
    # Applies the standard visual configuration to a Tkinter Text
    # widget used for translation input or output

    if widget is None:
        raise ValueError("Text widget cannot be None.")

    if not isinstance(widget, tk.Text):
        raise ValueError("Widget must be a tkinter Text instance.")

    if not isinstance(read_only, bool):
        raise ValueError("read_only must be a boolean.")

    widget.configure(
        background=INPUT_BACKGROUND_COLOR,
        foreground=TEXT_COLOR,
        insertbackground=TEXT_COLOR,
        font=MONOSPACE_FONT,
        relief="solid",
        borderwidth=BORDER_WIDTH,
        highlightthickness=0,
        padx=MEDIUM_PADDING,
        pady=MEDIUM_PADDING,
        wrap="word",
    )

    if read_only:
        widget.configure(
            state="disabled",
            background=OUTPUT_BACKGROUND_COLOR,
        )


def configure_history_list(
    widget: tk.Listbox,
) -> None:
    # Applies the standard visual configuration to a history Listbox

    if widget is None:
        raise ValueError("History list widget cannot be None.")

    if not isinstance(widget, tk.Listbox):
        raise ValueError(
            "Widget must be a tkinter Listbox instance."
        )

    widget.configure(
        background=SURFACE_COLOR,
        foreground=TEXT_COLOR,
        font=BODY_FONT,
        relief="solid",
        borderwidth=BORDER_WIDTH,
        highlightthickness=0,
        selectborderwidth=0,
    )


# Status Styling

def get_status_color(status: str) -> str:
    # Returns the appropriate text color for a standard application
    # status category

    if not isinstance(status, str):
        raise ValueError("Status must be a string.")

    normalized_status = status.strip().lower()

    status_colors = {
        "success": SUCCESS_COLOR,
        "error": ERROR_COLOR,
        "warning": WARNING_COLOR,
        "info": MUTED_TEXT_COLOR,
    }

    return status_colors.get(
        normalized_status,
        MUTED_TEXT_COLOR,
    )


def apply_status_style(
    label: ttk.Label,
    status: str,
) -> None:
    # Applies a status-specific foreground color to a status label

    if label is None:
        raise ValueError("Label cannot be None.")

    if not isinstance(label, ttk.Label):
        raise ValueError("Label must be a ttk.Label instance.")

    if not isinstance(status, str):
        raise ValueError("Status must be a string.")

    label.configure(
        foreground=get_status_color(status),
    )


# Public Module Interface

__all__ = [
    # Window Configuration
    "WINDOW_TITLE",
    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "MIN_WINDOW_WIDTH",
    "MIN_WINDOW_HEIGHT",

    # Colors
    "BACKGROUND_COLOR",
    "SURFACE_COLOR",
    "PRIMARY_COLOR",
    "SECONDARY_COLOR",
    "TEXT_COLOR",
    "MUTED_TEXT_COLOR",
    "BORDER_COLOR",
    "SUCCESS_COLOR",
    "ERROR_COLOR",
    "WARNING_COLOR",
    "INPUT_BACKGROUND_COLOR",
    "OUTPUT_BACKGROUND_COLOR",

    # Fonts
    "FONT_FAMILY",
    "TITLE_FONT",
    "SUBTITLE_FONT",
    "HEADING_FONT",
    "LABEL_FONT",
    "BODY_FONT",
    "MONOSPACE_FONT",
    "BUTTON_FONT",
    "STATUS_FONT",

    # Spacing
    "WINDOW_PADDING",
    "SECTION_PADDING",
    "SMALL_PADDING",
    "MEDIUM_PADDING",
    "LARGE_PADDING",
    "BUTTON_PADDING_X",
    "BUTTON_PADDING_Y",
    "LABEL_SPACING",
    "SECTION_SPACING",

    # Dimensions
    "TEXT_AREA_HEIGHT",
    "TEXT_AREA_WIDTH",
    "HISTORY_HEIGHT",
    "BUTTON_WIDTH",
    "DIRECTION_SELECTOR_WIDTH",

    # Borders
    "BORDER_WIDTH",
    "CORNER_RADIUS",

    # Style Names
    "STYLE_FRAME",
    "STYLE_LABEL",
    "STYLE_TITLE",
    "STYLE_SUBTITLE",
    "STYLE_HEADING",
    "STYLE_STATUS",
    "STYLE_BUTTON",
    "STYLE_PRIMARY_BUTTON",
    "STYLE_SECONDARY_BUTTON",
    "STYLE_COMBOBOX",

    # Theme
    "DEFAULT_THEME",
    "configure_theme",
    "configure_styles",
    "configure_root_window",
    "center_window",

    # Widget Configuration
    "configure_text_widget",
    "configure_history_list",

    # Status Styling
    "get_status_color",
    "apply_status_style",
]

