# __init__.py
# Graphical user interface package for the Morse Translator

# Contains the main Tkinter application window, reusable interface
# components, application styling, visual configuration, and GUI
# construction utilities used throughout the Morse Translator project

# The interface package acts as the presentation layer of the application.
# It coordinates user interaction with the core translation, validation,
# formatting, and history packages without implementing their underlying logic.

# Modules

# gui - Main application window, event handling, translation workflow,
#       history interaction, clipboard operations, and application lifecycle

# components - Reusable Tkinter interface components used to construct
#              input areas, output areas, controls, and history displays

# styles - Centralized colors, fonts, dimensions, widget configuration,
#          theme configuration, and visual styling utilities


# Main GUI Application

from .gui import (
    MorseTranslatorGUI,
    create_application,
    launch,
)


# Reusable GUI Components

from .components import (
    create_label,
    create_button,
    create_text_area,
    create_direction_selector,
    create_history_list,
)


# Visual Styles and Configuration

from .styles import (
    # Window Configuration
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,

    # Colors
    BACKGROUND_COLOR,
    SURFACE_COLOR,
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    TEXT_COLOR,
    MUTED_TEXT_COLOR,
    BORDER_COLOR,
    SUCCESS_COLOR,
    ERROR_COLOR,
    WARNING_COLOR,
    INPUT_BACKGROUND_COLOR,
    OUTPUT_BACKGROUND_COLOR,

    # Fonts
    FONT_FAMILY,
    TITLE_FONT,
    SUBTITLE_FONT,
    HEADING_FONT,
    LABEL_FONT,
    BODY_FONT,
    MONOSPACE_FONT,
    BUTTON_FONT,
    STATUS_FONT,

    # Spacing
    WINDOW_PADDING,
    SECTION_PADDING,
    SMALL_PADDING,
    MEDIUM_PADDING,
    LARGE_PADDING,
    BUTTON_PADDING_X,
    BUTTON_PADDING_Y,
    LABEL_SPACING,
    SECTION_SPACING,

    # Dimensions
    TEXT_AREA_HEIGHT,
    TEXT_AREA_WIDTH,
    HISTORY_HEIGHT,
    BUTTON_WIDTH,
    DIRECTION_SELECTOR_WIDTH,

    # Borders
    BORDER_WIDTH,
    CORNER_RADIUS,

    # Style Names
    STYLE_FRAME,
    STYLE_LABEL,
    STYLE_TITLE,
    STYLE_SUBTITLE,
    STYLE_HEADING,
    STYLE_STATUS,
    STYLE_BUTTON,
    STYLE_PRIMARY_BUTTON,
    STYLE_SECONDARY_BUTTON,
    STYLE_COMBOBOX,

    # Theme Configuration
    DEFAULT_THEME,
    configure_theme,
    configure_styles,
    configure_root_window,
    center_window,

    # Widget Configuration
    configure_text_widget,
    configure_history_list,

    # Status Styling
    get_status_color,
    apply_status_style,
)


# Public Module Interface

__all__ = [

    # Main GUI Application
    "MorseTranslatorGUI",
    "create_application",
    "launch",

    # Reusable GUI Components
    "create_label",
    "create_button",
    "create_text_area",
    "create_direction_selector",
    "create_history_list",

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

    # Theme Configuration
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

