# Interface Package Documentation

## Overview

The `interface/` package contains the graphical user interface layer of the Morse Translator.

It provides the application's Tkinter-based desktop interface, reusable graphical components, visual styling, window configuration, user interaction handling, translation controls, clipboard functionality, and translation history display.

The package is responsible for presenting functionality from the core, validation, formatting, and history packages to the user through a graphical interface.

The interface package does **not** implement the underlying Morse Code algorithms, validation rules, formatting logic, or history storage logic. Those responsibilities remain separated into their respective packages.

```text
interface/

│
├── __init__.py
├── gui.py
├── components.py
└── styles.py
```

# Package Responsibilities

The `interface/` package is responsible for:

* Creating the graphical application window.

* Displaying the Morse Translator interface.

* Providing reusable Tkinter components.

* Managing English-to-Morse and Morse-to-English selection.

* Accepting user input.

* Displaying translated output.

* Connecting GUI actions to the translation engine.

* Displaying translation history.

* Allowing users to load previous translations.

* Allowing users to clear translation history.

* Providing clipboard functionality.

* Displaying application status messages.

* Managing keyboard shortcuts.

* Applying consistent visual styling.

* Managing window dimensions and appearance.

* Coordinating interactions between presentation-layer components.

The package does **not** handle:

* Morse Code mapping logic.

* Encoding algorithms.

* Decoding algorithms.

* Translation data-model implementation.

* Input validation rules.

* Text normalization rules.

* History storage logic.

* Command-line interaction.

* Automated testing.

Those responsibilities belong to other packages in the project.

# Module Structure

## `__init__.py`

The package initializer exposes the public interface functionality to the rest of the Morse Translator application.

It provides a centralized import location for the main GUI application, reusable components, visual constants, and styling utilities.

The initializer exposes functionality from:

* `gui`

* `components`

* `styles`

The initializer also defines the package's `__all__` list so that the intended public API remains clearly documented.

### Purpose

The initializer allows other parts of the application to import GUI functionality without needing to know the internal organization of every interface module.

For example:

```python
from interface import MorseTranslatorGUI
```

or:

```python
from interface import launch
```

This creates a clean public boundary around the presentation layer.

# `gui.py`

`gui.py` contains the main graphical application for the Morse Translator.

It acts as the primary integration point between the user interface and the rest of the application.

The module uses Tkinter to create the application window and provides controls for entering text, selecting a translation direction, performing translations, viewing results, copying output, and interacting with translation history.

## Main Class

### `MorseTranslatorGUI`

`MorseTranslatorGUI` represents the complete Morse Translator graphical application.

The class owns the primary Tkinter window and coordinates all major GUI operations.

Its responsibilities include:

* Initializing the application window.

* Connecting the translation engine.

* Connecting the history manager.

* Building the graphical interface.

* Handling translation events.

* Handling direction changes.

* Managing input and output widgets.

* Managing translation history.

* Updating status messages.

* Handling clipboard operations.

* Handling application shutdown.

### Constructor

```python
MorseTranslatorGUI(
    root,
    translator=None,
    history_manager=None,
)
```

Creates a new graphical application.

The constructor accepts a Tkinter root window and optionally allows custom translator and history-manager instances to be supplied.

This makes the GUI easier to test and allows the application to provide alternate implementations when necessary.

# Application Configuration

## `_configure_application()`

Configures the application's visual theme, window properties, and shutdown behavior.

It uses the styling utilities from `styles.py` rather than defining all window configuration directly inside the GUI.

The method:

* Configures the ttk theme.

* Configures the root window.

* Registers the window-close handler.

## `_create_variables()`

Creates the Tkinter variables used by the graphical interface.

These variables include:

* Translation direction.

* Status message.

Tkinter variables allow widgets to automatically reflect changes made by the application.

# Interface Construction

The graphical interface is divided into several logical sections.

```text
Morse Translator Window

┌──────────────────────────────────────────────┐
│              Morse Translator                │
│   Translate English and Morse Code           │
├──────────────────────┬───────────────────────┤
│ Input                │ Output                │
│                      │                       │
│ User Text            │ Translation Result    │
│                      │                       │
├──────────────────────┴───────────────────────┤
│ Direction     Translate  Clear  Copy Output   │
├──────────────────────────────────────────────┤
│ Translation History                          │
│                                              │
│ Previous translations                        │
│                                              │
├──────────────────────────────────────────────┤
│ Status Message                               │
└──────────────────────────────────────────────┘
```

## `_build_interface()`

Coordinates the construction of all major interface sections.

It creates:

* The main container.

* The application header.

* The translation area.

* The control section.

* The history section.

* The status section.

This keeps the initialization process organized instead of placing every widget directly inside the constructor.

# Main Container

## `_create_main_container()`

Creates the main frame used to organize the entire graphical interface.

The container provides:

* Application padding.

* Grid-based layout.

* Expandable columns.

* Expandable translation areas.

The method establishes the basic layout structure used by the remaining GUI sections.

# Header

## `_create_header()`

Creates the application's title and subtitle.

The header communicates the application's purpose immediately to the user.

The title is:

```text
Morse Translator
```

The subtitle explains that the application supports translation between English and Morse Code.

The header uses styling values from `styles.py` to maintain visual consistency.

# Translation Section

## `_create_translation_section()`

Creates the main input and output region.

The section contains two side-by-side areas:

```text
Input                         Output

English Text                  Morse Code

or                            or

Morse Code                    English Text
```

The translation section uses a two-column layout so that the user can easily compare their input and translated output.

# Input Area

## `_create_input_area()`

Creates the editable text widget used for user input.

The input area includes:

* An input label.

* A multiline Tkinter text widget.

* Monospace formatting.

* Consistent padding.

* Standard border configuration.

The widget accepts multiline input and can be used for either English or Morse Code depending on the selected translation direction.

The input widget also supports the keyboard shortcut:

```text
Ctrl + Enter
```

which performs a translation.

# Output Area

## `_create_output_area()`

Creates the read-only output text area.

The output area displays the result of the translation operation.

Users cannot directly edit the translated result.

The output widget is temporarily enabled internally when the application needs to update its contents and then returned to read-only mode.

This prevents accidental modification of translated output.

# Control Section

## `_create_control_section()`

Creates the controls used to operate the translator.

The control section includes:

* Translation direction selector.

* Translate button.

* Clear button.

* Copy Output button.

The controls provide the main interaction points between the user and the translation engine.

# Translation Direction

The application supports two directions:

```text
English → Morse
```

and:

```text
Morse → English
```

## `_handle_direction_change()`

Updates the application's internal translation direction when the user selects a different mode.

The method also updates the input and output labels.

For example:

```text
English → Morse

English Input
Morse Output
```

becomes:

```text
Morse → English

Morse Input
English Output
```

This provides immediate visual feedback about the selected operation.

# Translation Processing

## `translate()`

The `translate()` method is the main event handler for the Translate button.

It:

1. Retrieves the input.

2. Checks whether input exists.

3. Determines the selected direction.

4. Calls the appropriate translation method.

5. Handles expected translation errors.

6. Handles unexpected application errors.

7. Updates the status message.

The method acts as a high-level controller rather than implementing translation algorithms itself.

# `_translate_to_morse()`

Handles English-to-Morse translation.

The general processing flow is:

```text
English Input

      │

      ▼

English Validation

      │

      ▼

Text Normalization

      │

      ▼

Morse Translator

      │

      ▼

Output Formatting

      │

      ▼

Display Output

      │

      ▼

Record History
```

The method uses the validation, formatting, core translation, and history packages rather than duplicating their logic.

# `_translate_to_english()`

Handles Morse-to-English translation.

The general processing flow is:

```text
Morse Input

      │

      ▼

Morse Normalization

      │

      ▼

Morse Validation

      │

      ▼

Morse Translator

      │

      ▼

Output Formatting

      │

      ▼

Display Output

      │

      ▼

Record History
```

This keeps the reverse translation workflow consistent with English-to-Morse processing.

# Input and Output Management

## `_get_input_text()`

Retrieves the current contents of the input text widget.

The method removes unnecessary surrounding whitespace before returning the value.

## `_display_output()`

Replaces the contents of the output widget with a translated result.

The method temporarily changes the widget state so that the application can insert the new output.

Afterward, the widget is returned to read-only mode.

## `clear()`

Clears both input and output areas.

It also updates the application status message.

## `copy_output()`

Copies the current output to the system clipboard.

If no output exists, the application displays an error status instead of attempting to copy an empty value.

# History Management

The GUI integrates with the `history/` package to provide a visible translation history.

## `_record_translation()`

Creates a `TranslationRecord` and passes it to the `HistoryManager`.

The GUI does not implement history storage itself.

Its responsibility is only to connect a completed translation with the history system.

## `_load_history()`

Loads existing history into the GUI when the application starts.

It delegates the actual retrieval operation to the history manager.

## `_refresh_history()`

Rebuilds the visible history list using the records returned by the history manager.

This ensures that the GUI reflects the current state of the history system.

## `_format_history_record()`

Converts a translation record into a compact human-readable representation suitable for the history list.

For example:

```text
EN → MORSE | HELLO WORLD
```

or:

```text
MORSE → EN | .... . .-.. .-.. ---
```

Long input values can be shortened so that they do not overwhelm the history display.

# History Selection

## `_handle_history_selection()`

Handles double-clicking a history entry.

When a history item is selected, the method retrieves the corresponding record and places its input and output into the translation interface.

This allows users to revisit previous translations.

The interaction flow is:

```text
History Entry

      │

      ▼

User Double-Clicks

      │

      ▼

Retrieve Record

      │

      ├──────────────► Input Area
      │
      └──────────────► Output Area
```

# Clearing History

## `clear_history()`

Allows the user to remove all stored translation history.

Before clearing the history, the GUI displays a confirmation dialog.

The general workflow is:

```text
Clear History

      │

      ▼

Are You Sure?

   ┌──┴──┐

   │     │

  Yes    No

   │     │

   ▼     ▼

Clear   Cancel
```

This prevents accidental deletion of translation records.

# Status Management

## `_set_status()`

Updates the status message displayed at the bottom of the application.

Status messages provide feedback about operations such as:

* Successful translation.

* Missing input.

* Invalid input.

* Clipboard operations.

* History operations.

* Clearing the interface.

Status messages can also use different colors to communicate the type of event.

For example:

```text
Success → Green

Error → Red

Warning → Orange

Information → Muted text
```

The actual color values are centralized in `styles.py`.

# Keyboard Shortcuts

## `_handle_translate_shortcut()`

Handles:

```text
Ctrl + Enter
```

The shortcut performs the same translation operation as clicking the Translate button.

Returning `"break"` prevents Tkinter from performing additional default processing for the key event.

# Application Lifecycle

## `_handle_close()`

Handles application shutdown.

The method destroys the main Tkinter window and ends the graphical application.

## `run()`

Starts the Tkinter event loop.

The method calls:

```python
root.mainloop()
```

This allows Tkinter to continuously process:

* Mouse events.

* Keyboard events.

* Button clicks.

* Widget updates.

* Window events.

# Application Factory

## `create_application()`

Creates and returns a configured `MorseTranslatorGUI` instance.

The function optionally accepts an existing Tkinter root window.

This is useful when another part of the application needs to control the root window or when testing the GUI.

## `launch()`

Provides a simple entry point for launching the graphical application.

It:

1. Creates the application.

2. Starts the GUI event loop.

This allows the GUI to be launched with a simple function call.

# `components.py`

`components.py` contains reusable Tkinter component-construction utilities.

The purpose of the module is to keep repeated widget creation logic separate from the main application window.

This helps prevent `gui.py` from becoming responsible for every low-level widget configuration detail.

## Component Responsibilities

The module provides reusable functionality for creating:

* Labels.

* Buttons.

* Text areas.

* Direction selectors.

* History lists.

These utilities establish a consistent interface for constructing common graphical components.

# `create_label()`

Creates a configured label widget.

The function provides a reusable way to construct labels without repeating standard configuration throughout the GUI.

Typical uses include:

* Section titles.

* Input labels.

* Output labels.

* Status labels.

# `create_button()`

Creates a configured button.

The function provides consistent button construction while allowing individual buttons to specify their displayed text and callback behavior.

Buttons are used for actions such as:

* Translate.

* Clear.

* Copy Output.

* Clear History.

# `create_text_area()`

Creates a configured text input or output area.

The component supports common text-widget configuration such as:

* Size.

* Font.

* Read-only behavior.

* Text wrapping.

* Padding.

The actual visual configuration is coordinated with `styles.py`.

# `create_direction_selector()`

Creates the control used to select the translation direction.

The selector provides the two supported modes:

```text
English → Morse
Morse → English
```

Using a reusable component keeps direction-selection behavior consistent across the interface.

# `create_history_list()`

Creates the Listbox used to display translation history.

The component is responsible for creating the underlying widget while the GUI controls how history records are retrieved and displayed.

# `styles.py`

`styles.py` contains centralized visual configuration for the Morse Translator interface.

The module prevents visual constants from being scattered throughout the GUI implementation.

It provides:

* Window dimensions.

* Colors.

* Fonts.

* Spacing.

* Widget dimensions.

* Border settings.

* ttk style names.

* Theme configuration.

* Widget styling utilities.

# Window Configuration

The module defines constants including:

```text
WINDOW_TITLE
WINDOW_WIDTH
WINDOW_HEIGHT
MIN_WINDOW_WIDTH
MIN_WINDOW_HEIGHT
```

These values control the basic application window configuration.

The default title is:

```text
Morse Translator
```

# Color Configuration

The interface uses centralized color constants including:

```text
BACKGROUND_COLOR
SURFACE_COLOR
PRIMARY_COLOR
SECONDARY_COLOR
TEXT_COLOR
MUTED_TEXT_COLOR
BORDER_COLOR
SUCCESS_COLOR
ERROR_COLOR
WARNING_COLOR
INPUT_BACKGROUND_COLOR
OUTPUT_BACKGROUND_COLOR
```

Centralizing these values makes it possible to modify the application's appearance without editing individual GUI components.

# Font Configuration

The module provides centralized font definitions including:

```text
FONT_FAMILY
TITLE_FONT
SUBTITLE_FONT
HEADING_FONT
LABEL_FONT
BODY_FONT
MONOSPACE_FONT
BUTTON_FONT
STATUS_FONT
```

Monospace fonts are particularly useful for Morse Code because dots and dashes are easier to visually distinguish when displayed using consistent character spacing.

# Spacing Configuration

The module provides reusable spacing values such as:

```text
WINDOW_PADDING
SECTION_PADDING
SMALL_PADDING
MEDIUM_PADDING
LARGE_PADDING
BUTTON_PADDING_X
BUTTON_PADDING_Y
LABEL_SPACING
SECTION_SPACING
```

These values help maintain consistent visual spacing throughout the application.

# Component Dimensions

Common widget dimensions are centralized through values such as:

```text
TEXT_AREA_HEIGHT
TEXT_AREA_WIDTH
HISTORY_HEIGHT
BUTTON_WIDTH
DIRECTION_SELECTOR_WIDTH
```

This allows the application's layout to be adjusted from one location.

# Style Names

The module defines reusable ttk style names such as:

```text
STYLE_FRAME
STYLE_LABEL
STYLE_TITLE
STYLE_SUBTITLE
STYLE_HEADING
STYLE_STATUS
STYLE_BUTTON
STYLE_PRIMARY_BUTTON
STYLE_SECONDARY_BUTTON
STYLE_COMBOBOX
```

This prevents style names from being duplicated throughout the application.

# Theme Configuration

## `configure_theme()`

Configures the ttk theme used by the application.

The default theme is defined by:

```text
DEFAULT_THEME
```

The function also applies the project's custom styles.

## `configure_styles()`

Configures reusable ttk styles.

It defines the visual appearance of common interface components.

Keeping this logic centralized makes the GUI easier to maintain.

# Window Styling

## `configure_root_window()`

Applies the standard application configuration to the Tkinter root window.

The configuration includes:

* Window title.

* Window dimensions.

* Minimum dimensions.

* Background color.

* Initial window positioning.

## `center_window()`

Centers the application window on the user's screen.

This improves the initial presentation of the application without requiring the user to manually reposition the window.

# Widget Styling

## `configure_text_widget()`

Applies standard formatting to Tkinter text widgets.

The function configures properties such as:

* Background.

* Foreground.

* Font.

* Border.

* Padding.

* Wrapping.

It also supports read-only output widgets.

## `configure_history_list()`

Applies standard styling to the history Listbox.

This keeps the history display visually consistent with the rest of the application.

# Status Styling

## `get_status_color()`

Returns the appropriate color for a status category.

Supported categories include:

```text
success
error
warning
info
```

If an unknown status is supplied, the function falls back to the standard muted text color.

## `apply_status_style()`

Applies the appropriate status color to a Tkinter label.

This allows status feedback to be visually distinguished without embedding color-selection logic inside the GUI workflow.

# Interface Architecture

The `interface/` package follows a presentation-layer architecture.

```text
                    interface/

                        │

          ┌─────────────┼─────────────┐

          │             │             │

          ▼             ▼             ▼

         gui       components      styles

          │             │             │

          └─────────────┼─────────────┘

                        │

                        ▼

                Application Layer

                        │

        ┌───────────────┼────────────────┐

        │               │                │

        ▼               ▼                ▼

      core          validation       formatting

        │

        ▼

      history
```

The GUI acts as the coordinator while the other packages retain ownership of their respective responsibilities.

# GUI Processing Flow

A typical translation initiated through the GUI follows this process:

```text
User

 │

 ▼

GUI Input Area

 │

 ▼

Translation Direction

 │

 ▼

Input Validation

 │

 ▼

Core Translator

 │

 ▼

Output Formatting

 │

 ▼

GUI Output Area

 │

 ├──────────────► Clipboard

 │

 └──────────────► History Manager
```

This flow demonstrates the separation between presentation logic and application logic.

# Relationship With Other Packages

The `interface/` package depends on several lower-level packages.

```text
                    Morse Translator

                           │

                           ▼

                       interface

                           │

          ┌────────────────┼────────────────┐

          │                │                │

          ▼                ▼                ▼

         core         validation        formatting

          │                │                │

          └────────────────┼────────────────┘

                           │

                           ▼

                        history
```

## `core/`

The GUI uses the core package to perform the actual Morse Code translation.

The GUI should not implement Morse Code mappings or encoding/decoding algorithms itself.

## `validation/`

The GUI uses validation functionality to determine whether user input can be processed.

This prevents GUI code from duplicating validation rules.

## `formatting/`

The GUI uses formatting utilities to normalize and prepare input and output for consistent presentation.

## `history/`

The GUI communicates with the history package to store and retrieve previous translations.

## `utils/`

The interface may use shared constants and helper utilities when appropriate.

## `tests/`

The interface package should be tested through the project's automated testing system.

# Separation of Responsibilities

The interface architecture follows a clear separation of responsibilities.

```text
gui.py

    ↓

Coordinates application interaction


components.py

    ↓

Creates reusable GUI components


styles.py

    ↓

Controls visual presentation
```

Meanwhile:

```text
core/

    ↓

Translation logic


validation/

    ↓

Input validation


formatting/

    ↓

Input/output formatting


history/

    ↓

Translation history
```

This prevents the graphical interface from becoming tightly coupled to the internal implementation of the translation system.

# Design Principles

## Separation of Concerns

The interface package focuses on presentation and interaction.

Translation algorithms remain in `core/`.

Validation remains in `validation/`.

Formatting remains in `formatting/`.

History remains in `history/`.

This separation keeps the project modular.

## Reusability

Reusable widgets and styling utilities are separated from the main GUI.

This makes it easier to create new screens or expand the existing interface.

## Centralized Styling

Visual constants are stored in `styles.py`.

This prevents values such as colors, fonts, and dimensions from being duplicated throughout the application.

## Testability

The GUI accepts optional translator and history-manager instances.

This makes it possible to substitute controlled objects during testing.

The underlying translation functionality can also be tested independently without launching the GUI.

## Maintainability

The GUI is divided into logical sections rather than implementing every operation in a single large method.

The major responsibilities are separated into:

```text
Window Configuration
        │
        ▼
Interface Construction
        │
        ▼
Translation Controls
        │
        ▼
Translation Processing
        │
        ▼
History Management
        │
        ▼
Status Management
```

# Public API

The `interface/` package exposes the main GUI application through its initializer.

The primary public API includes:

```python
MorseTranslatorGUI
create_application
launch
```

Reusable components include:

```python
create_label
create_button
create_text_area
create_direction_selector
create_history_list
```

Styling functionality includes:

```python
configure_theme
configure_styles
configure_root_window
center_window
configure_text_widget
configure_history_list
get_status_color
apply_status_style
```

The package also exposes its centralized visual constants through `__init__.py`.

# Example Usage

## Launching the Application

The simplest way to launch the GUI is:

```python
from interface import launch

launch()
```

This creates the application and starts the Tkinter event loop.

## Creating the Application Manually

The application can also be created explicitly:

```python
import tkinter as tk

from interface import MorseTranslatorGUI

root = tk.Tk()

application = MorseTranslatorGUI(
    root,
)

application.run()
```

This approach provides more control over the root window.

## Using the Application Factory

The factory function can be used when an application needs access to the GUI object:

```python
from interface import create_application

application = create_application()

application.run()
```

# Typical User Workflow

The graphical application is designed around a simple workflow:

```text
1. Launch application

        │

        ▼

2. Select translation direction

        │

        ▼

3. Enter text

        │

        ▼

4. Click Translate

        │

        ▼

5. Input is validated

        │

        ▼

6. Translation is performed

        │

        ▼

7. Result is formatted

        │

        ▼

8. Result is displayed

        │

        ▼

9. Translation is added to history
```

The user can then:

```text
Copy Output
      │
      ▼
Clipboard


Load History
      │
      ▼
Input / Output


Clear
      │
      ▼
Reset Translation


Clear History
      │
      ▼
Remove Stored Records
```

# Error Handling

The GUI handles expected errors without terminating the application.

Typical errors include:

* Empty input.

* Invalid English input.

* Invalid Morse Code.

* Unsupported characters.

* Invalid translation parameters.

* History-management failures.

The GUI communicates these problems through status messages rather than exposing Python tracebacks directly to the user.

Unexpected exceptions are also caught during translation so that a single failed operation does not immediately terminate the application.

# Interface Testing

The interface should be tested at both the component and integration levels.

Important test scenarios include:

* Application creation.

* Window initialization.

* English-to-Morse translation.

* Morse-to-English translation.

* Empty input.

* Invalid input.

* Direction changes.

* Clearing input and output.

* Copying output.

* Loading history.

* Selecting history entries.

* Clearing history.

* Status message updates.

* Keyboard shortcuts.

* Application shutdown.

GUI testing can be more involved than testing pure translation functions because it requires interaction with Tkinter widgets.

For this reason, the underlying translation, validation, formatting, and history systems should remain independently testable.

# Extending the Interface Package

New interface functionality should be added without moving core application logic into the GUI.

For example, if a settings panel is added in the future, it could be implemented as:

```text
interface/

├── __init__.py
├── gui.py
├── components.py
├── styles.py
└── settings_panel.py
```

The new module should:

1. Have a clearly defined responsibility.

2. Reuse existing styling utilities.

3. Avoid duplicating translation logic.

4. Avoid implementing validation rules directly.

5. Use reusable components where appropriate.

6. Remain compatible with the existing GUI architecture.

7. Be exposed through `interface/__init__.py` if it becomes part of the public API.

8. Be covered by appropriate tests.

9. Be documented in `docs/interface.md`.

# Future Interface Expansion

The current interface provides the foundation for additional features.

Potential future improvements include:

* Dark mode.

* Custom themes.

* Translation history search.

* History export.

* Larger history management controls.

* Morse playback using audio.

* Morse Code visual animations.

* Keyboard-only navigation.

* Customizable fonts.

* Adjustable text-area sizes.

* Copy-input functionality.

* Swap-direction button.

* Translation statistics.

* File-based translation.

* Drag-and-drop text input.

* Accessibility improvements.

These features should be implemented as additions to the presentation layer while continuing to keep core functionality independent.

# Example Future Architecture

A larger interface could eventually look like:

```text
interface/

├── __init__.py
├── gui.py
├── components.py
├── styles.py
├── dialogs.py
├── settings_panel.py
├── history_panel.py
└── audio_controls.py
```

The main `gui.py` file would remain responsible for coordinating these components rather than implementing every feature directly.

# Interface Design Philosophy

The interface package follows several important principles:

```text
Simple UI
    │
    ▼
Clear User Actions
    │
    ▼
Reusable Components
    │
    ▼
Centralized Styling
    │
    ▼
Separated Application Logic
```

The graphical interface should make the translator easy to understand without exposing the user to the internal complexity of the project.

A user should be able to open the application and immediately understand:

* Where to enter text.

* What direction is selected.

* Where the result appears.

* How to perform a translation.

* How to clear the current translation.

* How to copy the result.

* How to access previous translations.

# Summary

The `interface/` package forms the **presentation layer** of the Morse Translator.

Its primary responsibility is to provide a clean graphical experience while delegating translation, validation, formatting, and history functionality to their respective packages.

The package is structured around:

```text
Graphical Application

        │

        ▼

      gui.py
        │
        ├── User interaction
        ├── Translation workflow
        ├── History interaction
        ├── Clipboard operations
        └── Application lifecycle

        │

        ├───────────────┐
        │               │
        ▼               ▼

 components.py       styles.py
        │               │
        ▼               ▼
 Reusable widgets   Visual system
```

The resulting architecture keeps the GUI organized while allowing the rest of the Morse Translator to remain independent of Tkinter.

This separation makes the application easier to maintain, test, extend, and eventually adapt to additional interfaces or presentation technologies.

