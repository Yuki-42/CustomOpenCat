"""
The main injection point for the program. This file is responsible for creating the UI and starting the program.
"""

# Kyle Pannan
# Independent Spite Rewrite
# 21st July 2023

# Imports
from utils import create_logger, Translator, Config
from tkinter import Tk, PhotoImage, Menu, Label
from tkinter.font import Font
from platform import system as system_platform  # The platform function is renamed to system_platform because the name

# system is too generic and could cause issues if it is used elsewhere in the program.

"""
Requirements: 
    The app must be able to run on Windows, Mac and Linux
    The app must be able to be translated into different languages
    The app must be able to be used by people who are not programmers
    The app must be able to be used by people who are not familiar with the Nybble
    The program must be written in an asynchronous manner to allow for the UI to be responsive
"""

NaJoints = {
    'Nybble': [3, 4, 5, 6, 7],
    'Bittle': [1, 2, 3, 4, 5, 6, 7],
    'DoF16': []
}  # TODO: Find out what the fuck this actually means


class MainWindow:
    """
    The main window of the program, used to select different sub-apps to use. Users can change the language of the app
    from here too.
    """

    def __init__(self):
        """
        The initialisation method of the MainWindow class. This method is responsible for creating the window and the
        buttons that are used to select the different sub-apps.
        """
        self.logger = create_logger("MainWindow", "MainWindow", "MainWindow_", "DEBUG")

        self.logger.info("Initializing MainWindow")
        self.logger.debug("Initializing Config")

        self.config = Config()

        self.logger.debug("Config Initialised")

        self.logger.debug("Initializing Translator")
        self.translator = Translator(self.config.language)
        self.logger.debug("Translator Initialised")

        self.logger.debug("Initializing Window")
        self.window = Tk()

        # If the OS is Windows, the window is set to a specific size. This is because the window is too small on Windows
        # by default.
        if system_platform() == "Windows":
            self.window.geometry(self.config.windowsSize)
        else:
            self.window.geometry("300x300")

        # Set the window icon
        self.window.iconphoto(True, PhotoImage(file="assets/icon.png"))

        # Set the window title
        self.window.title = self.translator.getTranslation("uiTitle")

        # Set the font
        font = Font(family="Times New Roman", size=20, weight="bold")

        # Create the menu bar
        menuBar = Menu(self.window, background="ff8000", foreground="black", activebackground="white",
                       activeforeground="black")

        # Create the file menu
        fileMenu = Menu(menuBar, tearoff=0, background='#ffcc99', foreground='black')

        # Populate the file menu with NaJoints for some reason
        for key in NaJoints:  # This is used for changing the models; I don't know why it is named like that
            fileMenu.add_command(label=key, command=lambda key=key: self.updateModelLabel(key))

        # I do not know what self.menuBar.add_cascade does, but it is used in the original code, so I am keeping it
        menuBar.add_cascade(label=self.translator.getTranslation("Model"), menu=fileMenu)

        # Create the language menu
        languageMenu = Menu(menuBar, tearoff=0, background='#ffcc99', foreground='black')

        # Populate the language menu with languages
        for language in self.translator.languages:
            languageMenu.add_command(label=language, command=lambda language=language: self.updateLanguage(key))


        # Create the model label
        self.modelLabel = Label(self.window, text=self.config.model, font=font)

    def updateModelLabel(self, model):
        """
        Updates the model label to the given model.

        Args:
            model: The model to update the model label to.
        """
        self.modelLabel.config(text=model)
        self.config.model = model

    def updateLanguage(self, language):
        """
        Updates the language of the app to the given language.

        Args:
            language: The language to update the app to.
        """
        self.config.language = language
        self.translator.language = language

        # TODO: Update the UI to the new language


if __name__ == "__main__":
    MainWindow()
