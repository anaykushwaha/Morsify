# main.py
# Main entry point for the Morse Translator application

# Starts the Morse Translator graphical interface and provides
# the application's top-level execution flow


# Imports

from interface import MorseTranslatorGUI


# Application Entry Point

def main() -> None:
    # Starts the Morse Translator application
    # Creates the main GUI window and begins the Tkinter event loop

    application = MorseTranslatorGUI()

    application.run()


# Script Execution

if __name__ == "__main__":
    main()

